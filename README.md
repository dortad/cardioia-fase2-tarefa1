# CardioIA — Fase 2: Diagnóstico Automatizado

Entrega do Capítulo 1 — Desafio Integrador: IA entre Robôs, Sinapses e Medicina. Este repositório reúne a extração de sintomas por regras (Parte 1) e a classificação de risco com TF-IDF e aprendizado supervisionado (Parte 2).

**Status: entrega em preparação.** A Parte 1 está concluída e aprovada. A Parte 2 tem base de 60 frases, notebook executado e avaliação por grupos concluída. Faltam o vídeo, seu link e a publicação/verificação da versão final no GitHub.

## Equipe

Grupo AI4Success — turma 2TIAOR.

| Integrante | RM |
|---|---|
| Durval de Oliveira Dorta Junior | 567007 |
| Guilherme da Nobrega Gontijo | 562211 |

## Organização da entrega

| Caminho | Conteúdo |
|---|---|
| [parte1/](parte1/README.md) | Dez relatos sintéticos, mapa de sintomas, extrator Python, fontes e testes |
| [parte2/](parte2/README.md) | CSV com 60 frases, proveniência, notebook executado e avaliação |
| [docs/STATUS_TAREFA.md](docs/STATUS_TAREFA.md) | Atendimento ao enunciado e pendências |
| [docs/MAPEAMENTO_APOSTILAS_FASE2.md](docs/MAPEAMENTO_APOSTILAS_FASE2.md) | Relação entre os conteúdos estudados e as atividades |
| [apoio/fase1/](apoio/fase1/README.md) | Acervo preservado da fase anterior: dados, imagens, textos e documentação |
| [requirements.txt](requirements.txt) | Dependências da implementação atual da tarefa |

O acervo da Fase 1 possui documentação e dependências próprias. A execução das Partes 1 e 2 usa os arquivos presentes nas respectivas pastas, sem depender desse acervo.

## Preparação e execução

Com Python 3.12, execute na raiz do repositório. Se o ambiente virtual já existe e está configurado, basta ativá-lo.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Parte 1 (usa somente a biblioteca padrão):

```powershell
python parte1/diagnostico_sintomas.py
python -B parte1/test_diagnostico_sintomas.py
```

Parte 2 (notebook e execução equivalente pelo terminal):

```powershell
python parte2/executar_notebook.py
python parte2/classificador_risco.py
python -B parte2/test_classificador_risco.py
```

O [notebook executado](parte2/classificador_risco.ipynb) contém TF-IDF, classificação, matriz de confusão, análise de erros e vieses. Na divisão fixa de 41 frases de treino e 19 de teste, o modelo acertou 17 (89,47%), contra 36,84% do baseline. Os dois erros foram altos previstos como baixos. Consulte [resultados e limitações](parte2/RESULTADOS.md). Para abrir interativamente, use `python -m jupyterlab parte2/classificador_risco.ipynb`. As principais versões da execução estão em [requirements-reproducao.txt](requirements-reproducao.txt).

## Dados, fontes e limitações

Os relatos são sintéticos e didáticos. A origem textual e a fundamentação das associações estão separadas em [fontes da Parte 1](parte1/FONTES_MAPA.md) e [fontes e propostas da Parte 2](parte2/FONTES_DATASET.md). A documentação da Parte 1 detalha a origem dos relatos e as limitações das regras, incluindo os empates mantidos por decisão do projeto.

A Parte 2 contém 60 frases, 30 por classe, com [proveniência individual](parte2/proveniencia_frases.csv). P01–P30 foram aprovadas pelo responsável; P31–P60 foram elaboradas e revisadas pelo assistente sob autorização para concluir sem novas aprovações. A base anterior foi arquivada em `parte2/historico/`. O [relatório de curadoria](parte2/RELATORIO_CURADORIA.md) documenta integridade, semelhanças e limitações. Não há validação clínica e a solução não se destina à triagem real.

O enunciado integral e as apostilas são materiais locais de estudo, ignorados pelo Git. Algumas referências internas apontam para esses arquivos e estarão disponíveis apenas na cópia local que os contém. Os requisitos da entrega estão resumidos no documento de status.

## Vídeo e publicação

**Vídeo de demonstração: pendente.** Após concluir a solução, gravar até quatro minutos, publicar no YouTube como não listado e inserir o link nesta seção.

Repositório configurado: [cardioia-fase2-tarefa1](https://github.com/dortad/cardioia-fase2-tarefa1). Antes da entrega, confirmar a visibilidade pública e o envio da versão final. A reorganização local não publica alterações automaticamente.