# Progresso do projeto CardioIA - Fase 2

## Estado atual

A Parte 1 foi concluída e seu comportamento foi aprovado pelo responsável pelo projeto nesta sessão. A entrega completa da Fase 2 permanece em andamento.

## Parte 1 concluída

- Dez relatos sintéticos revisados, com sintomas, início e impacto na rotina.
- Mapa CSV com 30 associações e quatro categorias, mantendo as três colunas do enunciado.
- Fontes institucionais e critérios de adaptação documentados em [FONTES_MAPA.md](fase2/parte1/FONTES_MAPA.md).
- Extração por regras com normalização, variantes linguísticas, tratamento limitado de negação e prevenção de contagem duplicada.
- Saída com expressões reconhecidas, conceitos, condições associadas e pontuações.
- Empates explícitos nos relatos 1, 3 e 9, mantidos por decisão aprovada.
- Dez de dez relatos com correspondências; isso não representa 100% de acurácia clínica.
- Treze testes automatizados passaram na validação da implementação.
- Resultados e limitações discutidos e aprovados; encerramento da Parte 1 autorizado pelo usuário.

A contagem é uma heurística didática. O código não interpreta de forma geral duração, relação com esforço ou contexto clínico. Essas limitações foram aceitas para o escopo da atividade e estão registradas no [README da Parte 1](fase2/parte1/README.md).

## Ambiente

A pasta foi renomeada para `carioia-fase2-tarefa1`. Foi identificado que a instalação de Python 3.12 existe, mas seu acesso era restrito nesta sessão. Os scripts do ambiente virtual também continham o caminho antigo. Após o trabalho de correção, o usuário informou que resolveu o ambiente virtual. Não há nova verificação do ambiente nesta etapa de encerramento documental.

## Parte 2 em andamento

Já existem `frases_risco.csv` e `classificador_risco.py`, com TF-IDF e regressão logística. O histórico anterior registra uma execução com acurácia de 0,60; esse valor não constitui uma nova medição nem uma meta exigida.

Pendências:

- Revisar o dataset e seus rótulos junto ao usuário.
- Criar o notebook `.ipynb` exigido pelo enunciado.
- Executar treino e avaliação e registrar os resultados reproduzidos.
- Interpretar erros, diferenças entre classes e limitações da base simulada.
- Documentar a relação com os capítulos 11 e 07 das apostilas.

## Demais entregas

- Atualizar o README principal para a Fase 2 e corrigir o link do repositório.
- Confirmar publicação dos arquivos e acesso público no GitHub.
- Gravar o vídeo de até quatro minutos, publicar como não listado e incluir seu link.
- Implementar os itens Ir Além caso sejam incluídos no escopo da entrega: portal React + Vite e notebook de MLP com Keras para ECG.

Os dados numéricos, textos e imagens da fase anterior permanecem disponíveis como material de apoio. O [mapeamento das apostilas](docs/MAPEAMENTO_APOSTILAS_FASE2.md) orienta as escolhas didáticas.

## Próxima etapa acordada

Iniciar a revisão da Parte 2 em etapas, com acompanhamento e decisões do usuário. Nenhuma alteração na Parte 2 foi realizada durante o encerramento da Parte 1.
