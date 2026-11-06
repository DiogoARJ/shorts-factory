---
name: agencia-financas
description: "Usar quando o Diogo pede trabalho de finanças da agência ou de um cliente: fecho do mês, lançamentos, reconciliações bancárias, demonstrações financeiras, análise de desvios (orçamento vs real), apoio a auditoria. Guias do plugin Finance oficial da Anthropic."
---

# Finanças da agência

Responder em pt-PT, direto e curto. Abrir só o guia da tarefa em curso: `guias/<nome>/GUIA.md` (e as `references/` que ele indicar). `guias/CONNECTORS.md` lista as ferramentas que os guias esperam (ERP, folha de cálculo, banco); se não houver conector, trabalhar com ficheiros que o Diogo dá (extratos, CSV, Excel).

| Tarefa | Guia |
|---|---|
| Lançamentos contabilísticos (acréscimos, diferimentos, amortizações) | `journal-entry`, `journal-entry-prep` |
| Reconciliação banco / razão / subcontas | `reconciliation` |
| Demonstração de resultados, balanço, fluxos de caixa | `financial-statements` |
| Orçamento vs real, desvios por cliente ou serviço | `variance-analysis` |
| Calendário e checklist do fecho do mês | `close-management` |
| Apoio a auditoria, testes de controlo | `audit-support`, `sox-testing` |

## Regras
- Os guias seguem prática dos EUA (US GAAP, SOX). Em Portugal aplica-se o SNC e as regras da AT: adaptar a terminologia e dizer quando algo não se aplica (SOX não se aplica a uma agência portuguesa).
- Não inventar valores. Cada número sai de um documento do Diogo ou é marcado como estimativa.
- Isto prepara o trabalho, não substitui o contabilista certificado: decisões fiscais e entregas à AT ficam com ele.
- Contas de clientes nunca se misturam com as da agência.

Licença: Apache 2.0 (anthropics/knowledge-work-plugins @ab4cb1c), ver `LICENSE-Apache-2.0.txt`.
