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

As famílias foram consolidadas em seis grupos antes do treinamento, e a divisão foi congelada sem escolher sementes pelos resultados. Exemplos semelhantes permanecem no mesmo conjunto. Os IDs de treino e teste estão registrados em `divisao_avaliacao.csv` e ambos os conjuntos contêm as duas classes.

O script e o notebook atuais usam a mesma divisão fixa por grupos e o mesmo `Pipeline`. A avaliação final está documentada em [RESULTADOS.md](RESULTADOS.md); qualquer ajuste futuro orientado pelos erros exigirá um novo conjunto independente de teste.

## Vieses e limites discutidos no notebook

- Todos os exemplos são didáticos e majoritariamente produzidos com apoio da mesma IA, com padrões de linguagem semelhantes.
- Há concentração de bem-estar e melhora na classe baixa e de combinações de sinais de alerta na alta. Não se pode generalizar para queixas ambíguas ou populações reais.
- Os lotes finais incluem alguns alertas musculoesqueléticos para reduzir a associação entre região corporal e classe; isso não elimina o viés de seleção nem torna a base representativa.
- A classe alta reúne contextos que as fontes descrevem com níveis diferentes de urgência. Essa redução binária é uma convenção do exercício, não uma escala clínica.
- Negação aparece nas duas classes, mas TF-IDF não garante compreensão de escopo, temporalidade ou causalidade.
- A ausência de duplicatas exatas não elimina semelhança semântica. Pequeno número de famílias pode limitar o tamanho e o equilíbrio de uma divisão por grupos.
- Quantidade de 60 e equilíbrio 30/30 foram escolhas do projeto; não refletem prevalência e não são requisitos numéricos do enunciado.

Os capítulos 11 e 07 das apostilas fundamentam, respectivamente, a vetorização/classificação e a análise de vieses. O notebook e as métricas finais foram concluídos; a demonstração em vídeo permanece pendente.
