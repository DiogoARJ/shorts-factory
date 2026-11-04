<#
  Instala o Jarvis (Claude Code + Telegram) no PC do Diogo. Usa a subscrição Claude Pro: sem API, sem custos extra.
  Correr numa PowerShell normal, a partir desta pasta:
      Set-ExecutionPolicy -Scope Process Bypass; .\instalar.ps1
#>
$ErrorActionPreference = 'Stop'
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
function Passo($t) { Write-Host "`n==> $t" -ForegroundColor Cyan }
function Refresh-Path { $env:Path = [Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [Environment]::GetEnvironmentVariable('Path','User') }

Passo "Claude Code"
if (-not (Get-Command claude -ErrorAction SilentlyContinue)) { irm https://claude.ai/install.ps1 | iex; Refresh-Path }
claude --version

Passo "Bun (o plugin do Telegram precisa dele)"
if (-not (Get-Command bun -ErrorAction SilentlyContinue)) { irm https://bun.sh/install.ps1 | iex; Refresh-Path }
bun --version

Passo "Git (para guardar a memória)"
if (-not (Get-Command git -ErrorAction SilentlyContinue)) { winget install --id Git.Git -e --silent; Refresh-Path }

Passo "Atalho para arrancar o Jarvis sempre que entras no Windows"
$startup = [Environment]::GetFolderPath('Startup')
$lnk = (New-Object -ComObject WScript.Shell).CreateShortcut((Join-Path $startup 'Jarvis.lnk'))
$lnk.TargetPath = 'powershell.exe'
$lnk.Arguments = "-NoExit -ExecutionPolicy Bypass -File `"$here\arrancar.ps1`""
$lnk.WorkingDirectory = $here
$lnk.Save()

Passo "PC sem adormecer quando ligado à corrente"
powercfg /change standby-timeout-ac 0
powercfg /change hibernate-timeout-ac 0

Write-Host @"

Falta a parte interativa (5 min). Na mesma janela:
  1. claude                      (entra com a tua conta Claude Pro, se pedir)
  2. /plugin install telegram@claude-plugins-official      (escolhe 'user scope')
  3. /telegram:configure O_TEU_TOKEN_DO_BOTFATHER
  4. /exit   e depois:   .\arrancar.ps1
  5. Manda uma mensagem ao teu bot no Telegram -> ele responde com um código
  6. No terminal:  /telegram:access pair CODIGO    e depois    /telegram:access policy allowlist
"@ -ForegroundColor Green
