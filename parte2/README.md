# Parte 2 - Classificador básico de texto

## Objetivo

Treinar um classificador de risco clínico com base em frases curtas, usando TF-IDF e Logistic Regression.

## Arquivos

- `frases_risco.csv` — base atual com 12 frases e rótulos
- `FONTES_DATASET.md` — origem dos dados, fontes consultadas, critérios propostos e lote piloto para revisão
- `classificador_risco.py` — treino e avaliação do modelo

## Execução

```bash
python parte2/classificador_risco.py
```

## Observação

Foi aprovada a proposta de ampliar a base para 60 frases sintéticas, 30 por classe. A quantidade é uma escolha do projeto, não uma exigência do enunciado. Os critérios e as primeiras dez propostas estão em [FONTES_DATASET.md](FONTES_DATASET.md), ainda sujeitos à revisão conjunta. O CSV mantém os 12 registros anteriores nesta etapa.

As referências de saúde fundamentam a construção dos cenários; não são fontes literais das frases novas nem autoras dos rótulos. Frases e rótulos sintéticos serão identificados como elaboração didática com apoio de IA e revisão do responsável pelo projeto, sem alegar validação clínica.
