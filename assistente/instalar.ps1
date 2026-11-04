<#
  Instala o assistente (OpenJarvis + Claude + Telegram) no PC do Diogo.
  Correr numa PowerShell COMO ADMINISTRADOR, a partir desta pasta:
      Set-ExecutionPolicy -Scope Process Bypass; .\instalar.ps1
  Pode ser corrido de novo sem problema.
#>
$ErrorActionPreference = 'Stop'
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$cfgDir = Join-Path $env:USERPROFILE '.openjarvis'

function Passo($t) { Write-Host "`n==> $t" -ForegroundColor Cyan }

# 1. Segredos -----------------------------------------------------------------
Passo "Chaves (ficam guardadas só neste PC, como variáveis de ambiente)"
if (-not $env:ANTHROPIC_API_KEY) {
  $k = Read-Host "Cola a chave da API da Anthropic (começa por sk-ant-)"
  [Environment]::SetEnvironmentVariable('ANTHROPIC_API_KEY', $k.Trim(), 'User')
  $env:ANTHROPIC_API_KEY = $k.Trim()
}
if (-not $env:TELEGRAM_BOT_TOKEN) {
  $t = Read-Host "Cola o token do bot do Telegram (do @BotFather)"
  [Environment]::SetEnvironmentVariable('TELEGRAM_BOT_TOKEN', $t.Trim(), 'User')
  $env:TELEGRAM_BOT_TOKEN = $t.Trim()
}

# 2. Descobrir o teu chat id ----------------------------------------------------
Passo "Liga o bot a ti"
Write-Host "Abre o teu bot no Telegram e manda-lhe a mensagem: ola"
Read-Host "Depois carrega Enter aqui"
$upd = Invoke-RestMethod "https://api.telegram.org/bot$($env:TELEGRAM_BOT_TOKEN)/getUpdates"
$chatId = ($upd.result | Where-Object { $_.message } | Select-Object -Last 1).message.chat.id
if (-not $chatId) { throw "Não encontrei a tua mensagem. Manda 'ola' ao bot e corre o script outra vez." }
Write-Host "Chat id: $chatId" -ForegroundColor Green

# 3. Instalador oficial do OpenJarvis (com serviço que arranca com o Windows) ---
Passo "A instalar o OpenJarvis (pode demorar; pode pedir as Build Tools do Visual Studio)"
$env:OPENJARVIS_SERVICE = '1'
irm https://open-jarvis.github.io/OpenJarvis/install.ps1 | iex

# 4. Personalidade, perfil, memória e configuração ----------------------------
Passo "A copiar a personalidade e a configuração"
New-Item -ItemType Directory -Force -Path $cfgDir | Out-Null
foreach ($f in 'SOUL.md','USER.md','MEMORY.md') {
  $dst = Join-Path $cfgDir $f
  if (-not (Test-Path $dst)) { Copy-Item (Join-Path $here "persona\$f") $dst }
  else { Write-Host "  $f já existe — mantido (tem o que o Jarvis já aprendeu)" }
}
(Get-Content (Join-Path $here 'config.toml') -Raw).Replace('__CHAT_ID__', "$chatId") |
  Set-Content (Join-Path $cfgDir 'config.toml') -Encoding UTF8

# 5. PC sempre acordado quando ligado à corrente ------------------------------
Passo "A impedir o PC de adormecer (ligado à corrente)"
powercfg /change standby-timeout-ac 0
powercfg /change hibernate-timeout-ac 0

# 6. Arrancar e testar ----------------------------------------------------------
Passo "A reiniciar o serviço e a testar"
Get-ScheduledTask | Where-Object TaskName -like '*Jarvis*' | ForEach-Object {
  Stop-ScheduledTask $_.TaskName -ErrorAction SilentlyContinue; Start-ScheduledTask $_.TaskName }
$body = @{ chat_id = $chatId; text = "Olá Diogo. Já estou ligado. Fala comigo aqui quando quiseres." }
Invoke-RestMethod -Method Post "https://api.telegram.org/bot$($env:TELEGRAM_BOT_TOKEN)/sendMessage" -Body $body | Out-Null
Write-Host "`nFeito. Deves ter recebido uma mensagem no Telegram. Responde-lhe para testar." -ForegroundColor Green
Write-Host "Se ele não responder: abre PowerShell e corre  jarvis doctor  e depois  jarvis serve"
