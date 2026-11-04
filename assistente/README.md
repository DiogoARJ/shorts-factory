# Jarvis: assistente pessoal do Diogo

Falas com ele pelo **Telegram**: ele manda-te mensagens, tu respondes e ele faz as coisas.
Vai aprendendo à medida que falam.

**Custo extra: zero.** Usa o **Claude Code com a tua subscrição Claude Pro**, através dos *channels* oficiais
do Claude Code com o plugin do Telegram. Não usa a API.
(O OpenJarvis foi abandonado: com o Claude por dentro exigia a API paga.)

## Como funciona
- O Claude Code corre no teu PC ("Diogos"), nesta pasta, ligado ao teu bot do Telegram.
- A personalidade está em `CLAUDE.md` e `persona/SOUL.md`. O que sabe de ti está em `persona/USER.md`
  e as tuas regras em `persona/MEMORY.md`. Quando lhe dizes algo, ele atualiza estes ficheiros.
- Todas as manhãs manda-te o briefing pelo Telegram.
- **Limites:** o PC tem de estar ligado, e as conversas gastam os limites de uso do teu plano Pro.
  Os channels ainda estão em *research preview*.

Enquanto o PC não está montado, o **briefing da manhã na cloud** continua a chegar como notificação
da app do Claude. Lê e atualiza a mesma memória.

## Instalar no PC (≈15 min)

**1. No telemóvel (2 min, podes fazer já):** no Telegram abre o **@BotFather**, envia `/newbot`,
escolhe um nome (ex.: "Jarvis do Diogo") e um username acabado em `bot`. Guarda o **token**.

**2. No PC, numa PowerShell:**
```powershell
git clone https://github.com/diogoarj/shorts-factory
cd shorts-factory; git checkout ccr-7b16cb2d-vzbbx3; cd assistente
Set-ExecutionPolicy -Scope Process Bypass; .\instalar.ps1
```
O script instala o Claude Code, o Bun e o Git, faz o Jarvis arrancar sempre que entras no Windows
e impede o PC de adormecer quando está ligado à corrente.

**3. Parte interativa** (o script mostra-a no fim):
```
claude
/plugin install telegram@claude-plugins-official      (escolhe "user scope")
/telegram:configure <TOKEN>
/exit
.\arrancar.ps1
```
Manda uma mensagem ao bot. Ele responde com um código. No terminal:
```
/telegram:access pair <CODIGO>
/telegram:access policy allowlist
```
Nas primeiras respostas o Claude Code pode pedir permissão no terminal. Escolhe
**"sim, e não perguntar outra vez"**. Depois disso já não precisas do terminal.

## Personalizar
Fala com ele no Telegram. Exemplos:
- "Não me mandes nada ao fim de semana."
- "Emails do X são sempre prioritários."
- "Esquece o que disse sobre Y."

## Segurança
- Só a tua conta do Telegram passa (`allowlist`). Todas as outras mensagens são ignoradas.
- Enviar, publicar, apagar ou pagar só com o teu "sim".
