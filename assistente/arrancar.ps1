# Arranca o Jarvis: Claude Code ligado ao Telegram, nesta pasta (lê CLAUDE.md e a memória).
Set-Location (Split-Path -Parent $MyInvocation.MyCommand.Path)
claude --channels plugin:telegram@claude-plugins-official "Arranca (segue CLAUDE.md, secção 'Ao arrancar')."
