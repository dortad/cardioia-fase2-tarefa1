> **Atualização posterior à curadoria:** o notebook e a avaliação foram concluídos em 22/09/2026. As pendências abaixo registram o momento da curadoria. O script atual já usa a divisão fixa por grupos; veja [protocolo](PROTOCOLO_AVALIACAO.md) e [resultados](RESULTADOS.md).

# Relatório de curadoria — 60 frases

Data: 2026-09-22. Conferência estrutural e revisão didática; não constitui validação clínica nem avaliação de um modelo.

## Conferências realizadas

- 60 IDs únicos, de P01 a P60, com 30 frases por classe.
- 60 pares de texto/rótulo idênticos entre treinamento e proveniência, na mesma ordem.
- P01–P30 preservadas em todos os campos da proveniência.
- Nenhuma duplicata exata após normalizar caixa, acentos, espaços e pontuação.
- Nenhuma frase contém o próprio rótulo alto risco ou baixo risco.
- Origem, referências, justificativa, família e status presentes nos 60 registros.
- P01–P30: aprovação do responsável. P31–P60: revisão pelo assistente sob autorização, sem aprovação individual atribuída ao usuário.
- Base anterior preservada byte a byte em `historico/frases_risco_inicial_12.csv`; SHA256: `e5598343af5bcf8f8482fdf3f40c2827fb1b5421296bbea1b002ca31e97305ce`.

## Semelhança e divisão dos dados

Há 24 famílias iniciais, mas elas não representam 24 grupos necessariamente independentes. A comparação exploratória por Jaccard de conjuntos de palavras normalizadas encontrou 6 pares com similaridade igual ou superior a 0,45. Esse limite serve apenas para inspeção: não detecta todas as paráfrases e não prova independência dos demais pares.

| Par | Jaccard | Mesma família inicial |
|---|---|---|
| P05 / P13 | 0.579 | não |
| P01 / P05 | 0.571 | sim |
| P05 / P23 | 0.550 | sim |
| P04 / P21 | 0.500 | sim |
| P29 / P59 | 0.480 | sim |
| P05 / P10 | 0.450 | não |

Antes do notebook, consolidar famílias semelhantes em grupos de avaliação e congelar a divisão sem escolher sementes pelos resultados. Exemplos musculares após esforço, torções semelhantes em diferentes membros e relatos de bem-estar não são independentes apenas porque mudam a redação ou a região corporal. Os cenários torácicos com sintomas sobrepostos também precisam de revisão conjunta. Registrar os IDs efetivamente usados em treino e teste e garantir presença das duas classes nos dois conjuntos.

O script Python existente ainda usa divisão aleatória estratificada por linha. Ele permanece um protótipo e não implementa o controle de grupos descrito aqui; resultados desse script não devem ser apresentados como avaliação final. Não foi treinado nem ajustado um modelo nesta etapa de curadoria.

## Vieses e limites a discutir no notebook

- Todos os exemplos são didáticos e majoritariamente produzidos com apoio da mesma IA, com padrões de linguagem semelhantes.
- Há concentração de bem-estar e melhora na classe baixa e de combinações de sinais de alerta na alta. Não se pode generalizar para queixas ambíguas ou populações reais.
- Os lotes finais incluem alguns alertas musculoesqueléticos para reduzir a associação entre região corporal e classe; isso não elimina o viés de seleção nem torna a base representativa.
- A classe alta reúne contextos que as fontes descrevem com níveis diferentes de urgência. Essa redução binária é uma convenção do exercício, não uma escala clínica.
- Negação aparece nas duas classes, mas TF-IDF não garante compreensão de escopo, temporalidade ou causalidade.
- A ausência de duplicatas exatas não elimina semelhança semântica. Pequeno número de famílias pode limitar o tamanho e o equilíbrio de uma divisão por grupos.
- Quantidade de 60 e equilíbrio 30/30 foram escolhas do projeto; não refletem prevalência e não são requisitos numéricos do enunciado.

Os capítulos 11 e 07 das apostilas fundamentam, respectivamente, a vetorização/classificação e a análise de vieses. O notebook, as métricas finais e a demonstração em vídeo continuam pendentes.
