# Assistente pessoal (Jarvis)

O objetivo é um assistente que vem ter com o Diogo: manda mensagens, ele responde, e o assistente faz as coisas.
Vai aprendendo à medida que falam.

## Como está montado

| Fase | O quê | Onde | Estado |
|---|---|---|---|
| 1 | Briefing da manhã com notificação no telemóvel | Tarefa agendada no Claude (cloud) | **Ativo desde 2026-11-04** |
| 2 | Alertas ao fim do dia (só quando há algo) | Tarefa agendada no Claude | Depois de uns dias da fase 1 |
| 4 | Conversa nos dois sentidos pelo Telegram | OpenJarvis no PC do Diogo + API do Claude | **Dia 12/11**, com este kit |
| 5 | Chamadas telefónicas (urgências) | Twilio Voice | Opcional, mais tarde |

(A fase 3, só envio pelo Telegram via Zapier, foi saltada: a fase 4 substitui-a.)

A **memória é partilhada**. `persona/USER.md` e `persona/MEMORY.md` são lidos e atualizados pelo briefing
desde já. No dia 12 são copiados para o Jarvis, que continua a partir do que já aprendeu.

## Dia 12: instalar (≈30–60 min)

**Antes, no telemóvel (5 min):**
1. **Bot do Telegram.** No Telegram, abre o `@BotFather`, envia `/newbot`, dá-lhe um nome (ex.: "Jarvis do Diogo")
   e guarda o **token** que ele te dá.
2. **Chave da API do Claude.** Em console.anthropic.com cria a conta, carrega créditos (começa com 10–20 $)
   e cria uma **API key**. A API paga-se à parte da subscrição do Claude.

**No PC:**
1. Instala o Python 3.12 e o Git se ainda não estiverem instalados (o instalador tenta fazê-lo sozinho com o winget).
2. Abre a **PowerShell como Administrador** nesta pasta (`assistente`) e corre:
   ```powershell
   Set-ExecutionPolicy -Scope Process Bypass; .\instalar.ps1
   ```
3. O script pede o token e a chave, pede-te para mandares "ola" ao bot, instala o OpenJarvis, copia a
   personalidade e a memória, deixa o PC sem adormecer (quando ligado à corrente) e manda-te uma mensagem de teste.
4. Se o bot não responder: **reinicia o PC** (para o serviço apanhar as chaves novas). Se mesmo assim não der,
   corre `jarvis doctor`.

**Nota:** a instalação pode pedir as *Visual Studio Build Tools*. É um download grande, mas basta aceitar.

## Como personalizar

Fala com ele. Exemplos:
- "Não me mandes nada ao fim de semana."
- "O meu editor chama-se X; emails dele são sempre prioritários."
- "Esquece o que disse sobre Y."

Ele guarda isto em `USER.md` e `MEMORY.md` (em `%USERPROFILE%\.openjarvis`) e confirma numa linha.

## Custos (estimativa)
- OpenJarvis: grátis (open-source, Apache-2.0).
- API do Claude: paga por uso. Com conversa diária normal, conta com alguns dólares por mês;
  vê o consumo real em console.anthropic.com nos primeiros dias.
- O PC tem de estar ligado para o bot responder.

## Segurança
- Só o teu chat do Telegram pode falar com o bot (`allowed_chat_ids`).
- O servidor só escuta no próprio PC (127.0.0.1).
- As chaves ficam em variáveis de ambiente do Windows e nunca no repositório.
- Ações irreversíveis (enviar, publicar, apagar, pagar) precisam sempre do teu "sim".
