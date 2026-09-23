# Origem, referências e critérios do dataset de risco

## Status desta etapa

O responsável pelo projeto aprovou a proposta de 60 frases sintéticas, 30 por classe, e solicitou o registro das fontes. Os critérios e o lote piloto abaixo são propostas para revisão conjunta. As 60 frases ainda não foram produzidas nem aprovadas individualmente; o CSV de treinamento mantém os 12 registros anteriores.

## O que significa “fonte” neste dataset

Há três informações diferentes a registrar:

1. **Origem textual:** exemplo do enunciado, adaptação identificada ou elaboração sintética com apoio de IA (assistente Codex).
2. **Referência de saúde:** documento institucional que descreve os sintomas ou o contexto usado na elaboração.
3. **Origem do rótulo:** decisão didática do projeto, justificada por critérios explícitos e sujeita à revisão. Não é um rótulo atribuído pela instituição citada.

Nenhuma frase nova será apresentada como fala de paciente real, prontuário ou transcrição de uma fonte médica. As referências não validam os rótulos nem o modelo. A revisão do responsável pelo projeto não equivale a revisão clínica.

## Proveniência dos 12 registros atuais

- Registro 1, “sinto dor no peito e falta de ar”: reproduz o exemplo de alto risco do [Enunciado.md](../Enunciado.md), Parte 2.
- Registro 2, “tive um leve incômodo nas costas”: reproduz o exemplo de baixo risco do mesmo enunciado.
- Registros 3 a 12: já estavam em `frases_risco.csv` quando começou esta revisão. Não foi identificada fonte externa individual ou autoria original; não serão atribuídos retroativamente às referências consultadas agora.

O fato de uma frase constar no enunciado é sua origem didática, não validação clínica independente.

## Critérios propostos de rotulagem

### Alto risco na simulação

Relatos construídos com sintomas de alerta descritos nas fontes, especialmente desconforto torácico associado a falta de ar, suor frio ou dor no braço; ou percepção de batimentos alterados associada a dificuldade respiratória. A presença ou ausência isolada de uma palavra não define a classe. Referências: R1 e R2.

### Baixo risco na simulação

Cenários fictícios explicitamente descritos como bem-estar atual ou queixas musculoesqueléticas localizadas, pouco intensas e em melhora, sem sinais de alerta relatados. A definição é uma convenção do exercício, não uma classificação de segurança fornecida pelas fontes. R3 e R4 ajudam a contextualizar queixas musculoesqueléticas e seus limites.

Não considerar “leve”, “consigo caminhar”, ausência de dor no peito ou a palavra “não” como garantia de baixo risco. Informação ausente não equivale a sintoma negado.

### Casos insuficientes ou ambíguos

Não forçar um rótulo para frases vagas como “estou passando mal” ou “sinto desconforto depois de caminhar”. Reescrever o cenário fictício com informações suficientes ou retirar o exemplo antes de treinar. O CSV final continuará binário, conforme o enunciado; a ambiguidade será tratada durante a curadoria.

## Primeiro lote para revisão — ainda não incorporado ao CSV

Os identificadores abaixo são de revisão, não números de linha do futuro dataset.

| ID | Frase proposta | Rótulo proposto | Origem textual | Referência e justificativa didática |
|---|---|---|---|---|
| P01 | sinto dor no peito e falta de ar | alto risco | Exemplo literal do enunciado, já presente no CSV | E1; R1 contextualiza a combinação de sintomas. |
| P02 | Desde esta manhã, sinto pressão no tórax acompanhada de suor frio. | alto risco | Nova elaboração sintética com apoio de IA | R1: combinação de desconforto torácico e suor frio. |
| P03 | A dor começou no peito e agora também sinto dor no braço esquerdo. | alto risco | Nova elaboração sintética com apoio de IA | R1: cenário que explicita a extensão da dor para o braço. |
| P04 | Meu coração está disparado e estou com dificuldade para respirar mesmo sentado. | alto risco | Nova elaboração sintética com apoio de IA | R2: percepção de batimentos alterados associada a dificuldade respiratória. |
| P05 | Não sinto dor no braço, mas estou com aperto no peito e falta de ar. | alto risco | Nova elaboração sintética com apoio de IA | R1: negação de um sintoma não anula os outros sintomas afirmados. |
| P06 | Tive um pequeno incômodo na região lombar depois de carregar caixas; hoje está melhor e faço minhas atividades normalmente. | baixo risco | Adaptação sintética do exemplo de incômodo nas costas do enunciado | E1 e R3: foram acrescentados localização, contexto e melhora; rótulo é uma decisão do exercício. |
| P07 | Meu punho ficou dolorido após uma pequena torção, mas a dor está diminuindo e consigo movimentá-lo normalmente. | baixo risco | Nova elaboração sintética com apoio de IA | R4: cenário localizado de lesão e melhora, sem afirmar diagnóstico de entorse. |
| P08 | Sinto um incômodo discreto na musculatura das costas desde que levantei uma caixa, e ele vem diminuindo ao longo do dia. | baixo risco | Nova elaboração sintética com apoio de IA | R3: cenário musculoesquelético em melhora; mesma família de P06 para evitar divisão artificial entre treino e teste. |
| P09 | Hoje me sinto bem, respiro normalmente e realizo minhas atividades habituais. | baixo risco | Nova elaboração sintética com apoio de IA | Critério interno de bem-estar explícito; sem fonte clínica individual atribuída. |
| P10 | Não tenho dor no peito nem falta de ar e estou me sentindo bem hoje. | baixo risco | Nova elaboração sintética com apoio de IA | Critério interno de bem-estar com sintomas negados; não demonstra ausência de doença. |

## Registro previsto para cada uma das 60 frases

O arquivo de treinamento manterá apenas `frase,situacao`. Um arquivo auxiliar de proveniência deverá acompanhar a versão final com os campos:

- `id`: identificador estável.
- `frase`: texto exato, permitindo conferir a correspondência com o CSV.
- `situacao`: rótulo do exercício.
- `origem_textual`: exemplo do enunciado, adaptação ou elaboração sintética.
- `referencias`: identificadores das fontes ou indicação de critério interno.
- `justificativa_rotulo`: explicação específica, sem alegar validação clínica.
- `familia_cenario`: grupo de exemplos semelhantes para orientar a separação treino/teste.
- `status_revisao`: proposto ou aprovado pelo responsável pelo projeto.

Esse arquivo auxiliar é um entregável planejado para acompanhar as 60 frases; ainda não foi criado. Seus campos não devem ser usados como atributos do classificador, pois alguns revelam diretamente o rótulo.

## Cuidados para a ampliação e avaliação

- Balancear as classes é uma escolha didática, não estimativa da frequência real de casos.
- Diversificar redações e cenários; não completar a quantidade com pequenas paráfrases.
- Manter negações nas duas classes e não remover automaticamente “não” e “sem”.
- Evitar que “dor”, “leve”, “não” ou localização do corpo sejam atalhos suficientes para decidir a classe.
- Não usar frases que contenham a resposta, como “sou um paciente de alto risco”.
- Revisar duplicatas e famílias de cenários antes da divisão dos dados, mantendo exemplos muito semelhantes no mesmo conjunto.
- Documentar que rótulos sintéticos e quantidade pequena limitam qualquer interpretação de acurácia.
- Relacionar TF-IDF e classificação ao capítulo 11 e a análise de vieses ao capítulo 07 das apostilas; elas são referências metodológicas, não origem literal dos relatos.

## Referências consultadas

Consulta em 20/09/2026. As sínteses abaixo apenas delimitam o uso de cada referência; as frases e classes do projeto não foram retiradas como pares rotulados desses sites.

- **E1 — FIAP.** [Enunciado da atividade, Parte 2](../Enunciado.md). Solicita uma base simulada binária e fornece dois exemplos de frases com rótulos.
- **R1 — Ministério da Saúde.** [Infarto](https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/i/infarto), seção “Sintomas”. Descreve dor ou desconforto peitoral, possível irradiação para o braço, suor frio e falta de ar.
- **R2 — NHLBI/NIH.** [Arrhythmias — Symptoms](https://www.nhlbi.nih.gov/health/arrhythmias/symptoms). Descreve palpitações e manifestações associadas; aponta dificuldade respiratória e dor torácica como sintomas graves que requerem avaliação emergencial.
- **R3 — NHS.** [Back pain](https://www.nhs.uk/conditions/back-pain/). Apresenta causas possíveis, evolução e sinais de alerta. Serve como contexto para cenários fictícios de dor lombar em melhora, não como prova de baixo risco individual.
- **R4 — NHS.** [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/). Apresenta sintomas de lesões musculares e ligamentares e situações que requerem atendimento. Não fornece rótulos binários para o nosso dataset.

## Decisão pendente

Revisar e aprovar os critérios e as dez propostas acima antes da elaboração dos demais exemplos e da substituição do CSV.
