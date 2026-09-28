# Atendimento ao enunciado — Fase 2

Atualização: 27/09/2026. Síntese da atividade principal; os itens “Ir Além” estão fora do escopo definido pelo responsável.

| Exigência | Evidência atual | Situação |
|---|---|---|
| TXT com dez relatos completos | [Relatos](../src/parte1/sintomas_pacientes.txt) | Concluído e aprovado |
| CSV de associação entre sintomas e doenças | [Mapa](../src/parte1/mapa_sintomas_doencas.csv), 30 associações | Concluído e fundamentado |
| Python lendo relatos, extraindo sintomas e sugerindo diagnósticos | [Extrator](../src/parte1/diagnostico_sintomas.py) e 13 testes | Concluído; empates e limitações documentados |
| CSV de frases rotuladas por risco | [CSV consolidado](../src/parte2/frases_risco.csv), 60 frases e proveniência | Concluído; 30 exemplos por classe |
| Notebook com TF-IDF, classificação e avaliação | [Notebook executado](../src/parte2/classificador_risco.ipynb) | Implementado e executado sem erros |
| Avaliação de acurácia, comportamento e distorções | [Resultados](../src/parte2/RESULTADOS.md): 17/19 acertos e dois falsos negativos | Concluída com divisão por grupos e limitações |
| README no formato do template FIAP | [README principal](../README.md) | Concluído |
| Repositório público no GitHub | Remoto configurado e sincronizado | Pendente: a visibilidade consultada em 27/09/2026 é privada |
| Vídeo de até quatro minutos, YouTube não listado, link no README | Ainda ausente | Pendente |

## Validações realizadas

- Parte 1: 13 testes aprovados.
- Parte 2: cinco testes de integridade e isolamento aprovados.
- Dataset e proveniência: 60 registros correspondentes, 30 por classe.
- Notebook: 11 células de código executadas, nenhuma célula pendente e nenhuma saída de erro.
- Classificador: 89,47% de acurácia no teste retido; baseline de 36,84%.
- Dependências: `pip check` sem inconsistências.
- Git: antes da adequação à template, o commit local estava sincronizado com `origin/main`; a reorganização documental atual permanece local e ainda precisa ser commitada e publicada.

## Próxima etapa

Preparar e gravar a demonstração de até quatro minutos, publicá-la como não listada, inserir o link real no README e alterar a visibilidade do repositório para pública antes da entrega na plataforma FIAP.

Não ajustar dados, divisão ou modelo apenas para elevar a acurácia já observada. Se os erros atuais orientarem mudanças futuras, será necessário reservar outro conjunto independente de teste.

## Relação com as apostilas

Os capítulos 02 e 10 fundamentam leitura de arquivos e extração simbólica; o capítulo 11 fundamenta TF-IDF e classificação; o capítulo 07 orienta a discussão de vieses e limitações. Consulte o [mapeamento didático](MAPEAMENTO_APOSTILAS_FASE2.md). Os PDFs das apostilas são materiais locais de estudo e não estão publicados no repositório.

## Itens “Ir Além”

O portal React + Vite e a classificação visual de ECG com MLP em Keras não foram implementados, conforme a decisão atual de manter esta entrega restrita à atividade principal.
