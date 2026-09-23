# Atendimento ao enunciado — Fase 2

Atualização: 22/09/2026. Síntese de acompanhamento baseada no enunciado local da atividade; não substitui o documento original da FIAP.

| Exigência | Evidência atual | Situação |
|---|---|---|
| TXT com dez relatos completos | [Relatos](../parte1/sintomas_pacientes.txt) | Concluído e aprovado |
| CSV de associação entre sintomas e doenças | [Mapa](../parte1/mapa_sintomas_doencas.csv), 30 associações | Concluído e fundamentado |
| Python lendo relatos, extraindo sintomas e sugerindo diagnósticos | [Extrator](../parte1/diagnostico_sintomas.py) e 13 testes | Concluído; empates e limitações documentados |
| CSV de frases rotuladas por risco | [CSV consolidado](../parte2/frases_risco.csv), 60 frases e proveniência | Curadoria concluída; 30 por classe |
| Notebook com TF-IDF, classificação e avaliação | [Notebook executado](../parte2/classificador_risco.ipynb) | Implementado e executado sem erros |
| Avaliação de acurácia, comportamento e distorções | [Resultados](../parte2/RESULTADOS.md): 17/19 acertos, dois falsos negativos | Avaliação por grupos e limitações documentadas |
| README completo e repositório público | Estrutura e instruções na raiz | Resultados documentados; confirmar publicação/visibilidade e incluir vídeo |
| Vídeo de até quatro minutos, YouTube não listado, link no README | Ainda ausente | Pendente |

## Próxima etapa acordada

Os seis lotes estão concluídos: 60 frases com proveniência. P01–P30 têm aprovação individual do responsável; P31–P60 foram concluídas pelo assistente sob autorização para prosseguir sem novas aprovações. A base inicial foi preservada em `parte2/historico/`. Conferências e limitações constam em [RELATORIO_CURADORIA.md](../parte2/RELATORIO_CURADORIA.md).

Notebook e avaliação concluídos. Próxima etapa: preparar a demonstração de até quatro minutos, publicar o vídeo como não listado, incluir o link no README e confirmar a versão final pública no GitHub. Não houve publicação nesta etapa.

A quantidade de 60 frases e o equilíbrio 30/30 são escolhas do projeto; o enunciado não determina esse tamanho nem uma acurácia mínima. A Parte 1 foi encerrada com os empates aceitos; reorganizar arquivos não altera essa decisão.

## Relação com as apostilas

Os capítulos 02 e 10 fundamentam leitura de arquivos e extração simbólica; o 11 fundamenta TF-IDF e classificação; o 07 orienta a discussão de vieses e limitações. Consulte o [mapeamento didático](MAPEAMENTO_APOSTILAS_FASE2.md), elaborado como auditoria histórica, para os detalhes. As pendências antigas desse mapeamento devem ser lidas à luz do estado atualizado nesta página.

## Itens “Ir Além”

O enunciado também apresenta um portal React + Vite e uma classificação visual de ECG com MLP em Keras. Esses itens não foram implementados nesta etapa. O acervo em `apoio/fase1/` pode apoiar trabalhos posteriores, mas não constitui a implementação dessas extensões. Sua execução deverá ser tratada em etapa própria com o responsável.

Validação da reorganização em 22/09/2026: 13 testes da Parte 1 aprovados, extrator executado nos novos caminhos e integridade dos arquivos movidos conferida por SHA256. A execução do protótipo da Parte 2 parou por ausência de scikit-learn no ambiente virtual (ModuleNotFoundError: sklearn). Antes de executá-lo, instalar as dependências com python -m pip install -r requirements.txt na raiz. Não houve alteração dos algoritmos ou datasets nesta etapa.


Atualização da implementação em 22/09/2026: dependências instaladas na .venv; o impedimento de scikit-learn relatado na reorganização foi resolvido. Notebook executado do início ao fim em kernel novo e cinco testes de integridade/isolamento aprovados. Divisão congelada antes do ajuste; parâmetros mantidos após observar os erros. Parte 1 preservada.
