# Atendimento ao enunciado — Fase 2

Atualização: 22/09/2026. Síntese de acompanhamento baseada no enunciado local da atividade; não substitui o documento original da FIAP.

| Exigência | Evidência atual | Situação |
|---|---|---|
| TXT com dez relatos completos | [Relatos](../parte1/sintomas_pacientes.txt) | Concluído e aprovado |
| CSV de associação entre sintomas e doenças | [Mapa](../parte1/mapa_sintomas_doencas.csv), 30 associações | Concluído e fundamentado |
| Python lendo relatos, extraindo sintomas e sugerindo diagnósticos | [Extrator](../parte1/diagnostico_sintomas.py) e 13 testes | Concluído; empates e limitações documentados |
| CSV de frases rotuladas por risco | [CSV atual](../parte2/frases_risco.csv), 12 frases | Curadoria em andamento; ampliação para 60 aprovada |
| Notebook com TF-IDF, classificação e avaliação | Existe [protótipo em Python](../parte2/classificador_risco.py) | Notebook ainda ausente |
| Avaliação de acurácia, comportamento e distorções | Métricas no protótipo | Análise final pendente após curadoria |
| README completo e repositório público | Estrutura e instruções na raiz | Completar resultados e confirmar publicação/visibilidade |
| Vídeo de até quatro minutos, YouTube não listado, link no README | Ainda ausente | Pendente |

## Próxima etapa acordada

Revisar com o responsável os critérios e as dez propostas de [FONTES_DATASET.md](../parte2/FONTES_DATASET.md). Depois da aprovação, elaborar os demais exemplos por etapas e registrar a origem textual, referências, justificativa do rótulo e família de cenário. Só então atualizar a base e construir o notebook com divisão de treino/teste, TF-IDF ajustado apenas ao treino, classificador e análise de limitações e vieses.

A quantidade de 60 frases e o equilíbrio 30/30 são escolhas do projeto; o enunciado não determina esse tamanho nem uma acurácia mínima. A Parte 1 foi encerrada com os empates aceitos; reorganizar arquivos não altera essa decisão.

## Relação com as apostilas

Os capítulos 02 e 10 fundamentam leitura de arquivos e extração simbólica; o 11 fundamenta TF-IDF e classificação; o 07 orienta a discussão de vieses e limitações. Consulte o [mapeamento didático](MAPEAMENTO_APOSTILAS_FASE2.md), elaborado como auditoria histórica, para os detalhes. As pendências antigas desse mapeamento devem ser lidas à luz do estado atualizado nesta página.

## Itens “Ir Além”

O enunciado também apresenta um portal React + Vite e uma classificação visual de ECG com MLP em Keras. Esses itens não foram implementados nesta etapa. O acervo em `apoio/fase1/` pode apoiar trabalhos posteriores, mas não constitui a implementação dessas extensões. Sua execução deverá ser tratada em etapa própria com o responsável.

Validação da reorganização em 22/09/2026: 13 testes da Parte 1 aprovados, extrator executado nos novos caminhos e integridade dos arquivos movidos conferida por SHA256. A execução do protótipo da Parte 2 parou por ausência de scikit-learn no ambiente virtual (ModuleNotFoundError: sklearn). Antes de executá-lo, instalar as dependências com python -m pip install -r requirements.txt na raiz. Não houve alteração dos algoritmos ou datasets nesta etapa.
