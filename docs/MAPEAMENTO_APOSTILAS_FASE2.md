# CardioIA Fase 2: relação entre enunciado, apostilas e implementação

Análise em 20/09/2026. Este documento complementa a auditoria da pasta após a inclusão das 12 apostilas.

## Como interpretar os requisitos

O usuário esclareceu que as atividades devem ser interpretadas à luz dos conhecimentos ensinados nas apostilas. Assim, as soluções devem aplicar e explicar os conceitos pertinentes à fase.

O `Enunciado.md` define os entregáveis e as tecnologias obrigatórias. As apostilas explicam os fundamentos e oferecem exemplos de implementação. Uma técnica apresentada em aula não se torna automaticamente obrigatória em todas as atividades.

Foram examinados os sumários dos 12 capítulos e as seções diretamente relacionadas à atividade. Esta é uma leitura dirigida ao projeto, não uma revisão integral de todas as páginas ou uma validação de todas as afirmações das apostilas.

## Mapeamento dos 12 capítulos

| Capítulo | Relação com a atividade |
|---|---|
| 01 - Robôs, Neurônios e Saúde | Contextualiza a integração das disciplinas; não acrescenta por si só novos entregáveis ao enunciado. |
| 02 - RPA na Veia | Apoia a leitura de TXT/CSV, uso de UTF-8, módulo `csv`, Pandas e tratamento de arquivos nas Partes 1 e 2. |
| 03 - Cérebros de Silício | Contexto de neuromorfismo e neurônios; não há exigência explícita de memristores ou circuitos nesta atividade. |
| 04 - Além do Bit | Fundamentação em vetores e matrizes; não há exigência explícita de Qiskit ou computação quântica. |
| 05 - Interfaces Inteligentes | Referência direta do Ir Além 1: Hooks, Context API, consumo de dados, autenticação simulada e proteção de acesso. |
| 06 - IA Criativa | Referência direta da MLP do Ir Além 2: camadas, ativações, treinamento e implementação com Keras. |
| 07 - IA Responsável | Fundamenta a discussão de qualidade dos dados, vieses, interpretação de resultados e limitações. |
| 08 - Memória da Máquina | Contexto de armazenamento IoT; bancos em nuvem, ESP32 e persistência embarcada não são exigências desta entrega. |
| 09 - Veja para Crer | Apoio conceitual à organização de dashboards. O portal pedido continua sendo React + Vite; Node-RED e Grafana não são exigidos. |
| 10 - IA que Entende | Referência principal da Parte 1: abordagem simbólica, normalização, extração por regras e ontologias. |
| 11 - NLP no Estilo Clássico | Referência principal da Parte 2: vetorização, TF-IDF, classificação supervisionada, divisão treino/teste e métricas. |
| 12 - Máquinas que Enxergam | Apoia a preparação e análise das imagens no Ir Além 2. Filtros específicos são possibilidades a justificar, não entregáveis obrigatórios. |

## Parte 1: demonstrar extração e representação do conhecimento

**Base didática:** capítulo 10, seção 1.1 (p. 7), seção 2.2 (pp. 13-18), seção 4.2 (pp. 38-43) e seções 5.1-5.3 (pp. 48-58). Capítulo 02, seção 1.6.1 (pp. 12-14), para leitura de CSV.

O fluxo esperado é relato textual → normalização → identificação de sintomas → consulta ao mapa → sugestão de diagnóstico. O código atual já segue parte desse fluxo, mas só apresenta o resultado final.

Para evidenciar o aprendizado, recomenda-se apresentar os sintomas encontrados e a associação que motivou a sugestão, explicar como variantes são normalizadas e declarar como ambiguidades são tratadas. Isso é uma recomendação pedagógica; o enunciado não exige um formato específico de explicação.

As falhas já identificadas permanecem: “palpitações” não corresponde a “palpitação”; “pressao” não corresponde a “pressão”; associações duplicadas alteram a contagem; empates dependem da ordem do mapa. A normalização ensinada no capítulo 10 é diretamente pertinente a esses problemas.

O CSV solicitado representa um mapa simplificado de conhecimento. A apostila apresenta ontologias formais em RDF/OWL, mas o enunciado admite expressamente CSV ou planilha. Portanto, `rdflib`, OWL, spaCy e NLTK não são obrigatórios. Podem ser usados quando contribuírem para a solução, com justificativa.

## Parte 2: demonstrar vetorização, aprendizagem e avaliação

**Base didática:** capítulo 11, seção 3.3 (pp. 35-37) e seção 4.2 (pp. 45-48).

O código atual usa `TfidfVectorizer`, separação estratificada, ajuste do vocabulário somente no treino, regressão logística e relatório de classificação. Essas escolhas estão alinhadas aos conceitos estudados.

O notebook exigido deve explicar e executar a sequência: carregar e verificar os rótulos → dividir treino/teste → vetorizar → treinar → prever → avaliar → discutir erros. Mostrar uma pequena matriz TF-IDF e seu vocabulário ajuda a demonstrar o conceito, como no código-fonte 13 da apostila, mas não é uma exigência adicional do enunciado.

O exemplo de classificação da apostila usa BoW e Naive Bayes. O enunciado exige TF-IDF e permite outros classificadores simples; não há motivo para substituir a regressão logística apenas para copiar o exemplo.

O capítulo 11 interpreta diferenças de precisão entre classes, em vez de apenas imprimir uma acurácia. Assim, a entrega ganha alinhamento pedagógico ao explicar quais frases foram confundidas e possíveis causas. Não há meta mínima de acurácia no enunciado; os 97% do exemplo de spam pertencem a outro problema e não são meta para CardioIA.

## Governança: relacionar a reflexão ao modelo realmente entregue

**Base didática:** capítulo 07, seção 2 (pp. 12-16) e seções 8.3-8.4 (pp. 46-48).

A discussão deve considerar a base simulada de frases: distribuição de classes, diversidade de vocabulário, critérios de rotulagem, erros e possíveis associações superficiais aprendidas. Casos com negação ou diferentes maneiras de expressar um mesmo sintoma são exemplos de avaliação a considerar, não resultados já obtidos.

O CSV atual não possui atributos demográficos. Não é possível afirmar que foi medida justiça por sexo, raça ou idade nesse classificador. A análise da base numérica da fase anterior serve como contexto, mas não comprova fairness do modelo textual.

## Ir Além 1: aplicar o capítulo 05

**Base didática:** capítulo 05, seções 2 e 3 (pp. 8-29) e seção 5 (pp. 50-58). A figura 44 (p. 51) mostra autenticação simulada com Context API, token no localStorage e funções de login/logout.

A implementação deve evidenciar `useState`, `useEffect`, `useContext` e `useReducer`, além de Context API, dados simulados, proteção de rotas e os demais requisitos explícitos. O agendamento é uma aplicação natural das transições de estado ensinadas com reducer. O enunciado dispensa integração real com back-end.

## Ir Além 2: combinar capítulos 06 e 12

**Base didática:** capítulo 06, seção 4 (p. 30) e seção 6.2 (pp. 42-44); capítulo 12, seções de filtros e seus usos, especialmente 3.4 (pp. 22-23).

O capítulo 06 apresenta MLP e um exemplo com `Sequential`, `Dense`, compilação e treinamento. Para a atividade, é necessário adaptar a entrada às imagens, preparar os valores dos pixels, treinar e avaliar em dados separados, explicando as escolhas.

O README existente prevê CNN para imagens, mas o enunciado desta extensão pede **MLP com Keras**. Uma CNN isolada não substitui esse requisito. Filtros do capítulo 12 podem ser explorados e comparados quando fizerem sentido; não é necessário aplicar todos nem assumir que melhoram a classificação.

## Consequência para a auditoria anterior

As pendências de arquivos, notebook, documentação, vídeo e confirmação do GitHub público continuam. A complementação é pedagógica: além de entregar um programa que roda, demonstrar e explicar os conceitos pertinentes das apostilas.

A prioridade continua sendo corrigir e validar a Parte 1, concluir o notebook da Parte 2 com análise dos resultados e finalizar a documentação e o vídeo. Os materiais das demais disciplinas não ampliam automaticamente o escopo exigido pelo enunciado.

## Fontes locais

As páginas indicadas correspondem à ordem das páginas dos PDFs.

- [Enunciado da atividade](../Enunciado.md).
- [Capítulo 02 - RPA na Veia](<../Apostilas/2TIAOA - Fase 2 - Cap02 - RPA na Veia Automatizando Arquivos, Redes e Sistemas com Python_RevFinal.pdf>).
- [Capítulo 05 - Interfaces Inteligentes](<../Apostilas/2TIAOA - Fase 2 - Cap05 - Interfaces Inteligentes Conectando IA ao Usuário com React e JWT_RevFinal.pdf>).
- [Capítulo 06 - IA Criativa](<../Apostilas/2TIAOA - Fase 2 - Cap06 - IA Criativa Desvendando o Cérebro das Máquinas que Criam_RevFinal.pdf>).
- [Capítulo 07 - IA Responsável](<../Apostilas/2TIAOA - Fase 2 - Cap07 - IA Responsável Ética, Sustentabilidade e Regulação na Era dos Dados_RevFinal.pdf>).
- [Capítulo 10 - IA que Entende](<../Apostilas/2TIAOA - Fase 2 - Cap10 - IA que Entende Processamento de Linguagem Natural Baseado em Regras_RevFinal.pdf>).
- [Capítulo 11 - NLP no Estilo Clássico](<../Apostilas/2TIAOA - Fase 2 - Cap11 - NLP no Estilo Clássico Estatística, Vetores e Emoções em Texto_RevFinal.pdf>).
- [Capítulo 12 - Máquinas que Enxergam](<../Apostilas/2TIAOA - Fase 2 - Cap12 - Máquinas que Enxergam Filtragem Inteligente de Imagens com IA_RevFinal.pdf>).
