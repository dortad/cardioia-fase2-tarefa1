# Progresso do projeto CardioIA - Fase 2

## Resumo executivo

Este documento reúne tudo o que foi analisado, planejado, criado e validado até o momento para dar continuidade ao desenvolvimento da Fase 2 do projeto CardioIA conforme o enunciado em `Enunciado.md`.

O repositório atual está majoritariamente alinhado com a Fase 1 do projeto, e não com a Fase 2. A análise mostrou que o que existe hoje é uma base de dados, documentação e materiais de aquisição de dados, mas ainda faltam os entregáveis exigidos pela Fase 2, especialmente:

- Parte 1: frases de sintomas + mapa de conhecimento + código de extração
- Parte 2: dataset classificado + TF-IDF + classificador treinado
- Repositório público e README final
- Vídeo no YouTube
- Itens “Ir Além” (portal React e classificador visual com MLP)

Mesmo assim, parte da base para a Fase 2 foi iniciada e validada com scripts executáveis.

---

## 1) Contexto e objetivo

O enunciado descreve a fase 2 como o módulo de diagnóstico automatizado por IA para o CardioIA. A ideia principal é simular automatização de diagnóstico a partir de:

- relatos textuais de sintomas
- análise de risco por classificação de texto
- mapa de conhecimento entre sintomas e doenças
- triagem clínica baseada em NLP
- portal front-end de suporte visual (Ir Além 1)
- diagnóstico visual em ECG por rede neural (Ir Além 2)

A atividade exige múltiplos entregáveis acadêmicos e práticos, incluindo arquivos `.txt`, `.csv`, notebooks ou scripts em Python, README completo, GitHub e link de vídeo demonstrativo.

---

## 2) Verificação do estado atual do repositório

### O que já existe na pasta principal

O projeto atual contém os seguintes itens relevantes:

- [README.md](README.md) — documentação da Fase 1
- [Enunciado.md](Enunciado.md) — descrição da atividade da Fase 2
- [data/cardioia_dataset.csv](data/cardioia_dataset.csv) — base numérica
- [data/heart_kaggle.csv](data/heart_kaggle.csv) — base clínica de origem
- [docs/texto1-tecnico.txt](docs/texto1-tecnico.txt)
- [docs/texto2-leigo.txt](docs/texto2-leigo.txt)
- [docs/texto3-opas-doencas-cardiovasculares.txt](docs/texto3-opas-doencas-cardiovasculares.txt)
- [docs/texto4-ms-hipertensao.txt](docs/texto4-ms-hipertensao.txt)
- [assets/ecg](assets/ecg) — imagens de ECG
- [data/gerar_dataset.py](data/gerar_dataset.py)
- [data/baixar_imagens.py](data/baixar_imagens.py)
- [data/gerar_tiras_sinais.py](data/gerar_tiras_sinais.py)

### Conclusão da análise

O projeto está avançado em dados e documentação, mas ainda não está em conformidade com a Fase 2 do enunciado. A estrutura de `README.md` e da documentação geral falam de uma fase anterior, não da fase atual da atividade.

---

## 3) Checklist de implementação da Fase 2

Foi criado o arquivo [FASE2_CHECKLIST.md](FASE2_CHECKLIST.md), contendo a checklist geral.

### Parte 1 — Frases de sintomas + extração de informações

- [x] Visão geral da necessidade definida
- [x] Mapa de sintomas e doenças identificado
- [x] Estrutura de arquivos iniciada em `fase2/parte1/`
- [x] Arquivo TXT com 10 frases criadas
- [x] CSV de mapeamento de sintomas criado
- [x] Script de diagnóstico inicial criado
- [ ] Aprimorar a lógica para cobrir mais variações de linguagem
- [ ] Validar melhor precisão nas sugestões de diagnóstico

### Parte 2 — Classificador básico de texto

- [x] Visão geral da necessidade definida
- [x] Dataset inicial de frases com rótulos criado
- [x] Script de classificação com TF-IDF criado
- [x] Modelo treinado e executado
- [x] Métricas produzidas
- [ ] Melhorar a qualidade e a quantidade dos dados
- [ ] Aumentar a acurácia e robustez do modelo
- [ ] Gerar relatório final mais completo

### Ir Além 1 — Portal React + Vite

- [ ] Criar app React/Vite
- [ ] Estruturar pastas `contexts`, `components`, `services`, `pages`
- [ ] Implementar autenticação simulada com `Context API`
- [ ] Gerenciar clientes/pacientes com dados simulados
- [ ] Formulário de agendamento com `useState` e `useReducer`
- [ ] Dashboard com métricas
- [ ] Rotas protegidas
- [ ] Estilização responsiva
- [ ] README com instruções de execução

### Ir Além 2 — Diagnóstico visual em cardiologia

- [ ] Criar notebook Python com procedimento completo
- [ ] Pré-processar imagens de ECG
- [ ] Implementar MLP com Keras
- [ ] Treinar, testar e avaliar modelo
- [ ] Registrar resultados e acurácia
- [ ] Documentar no README

### Documentação final e entrega

- [ ] Atualizar README principal para a Fase 2
- [ ] Incluir integrantes, objetivos e links
- [ ] Incluir link do vídeo YouTube
- [ ] Publicar repositório no GitHub
- [ ] Preparar apresentação final

---

## 4) Artefatos criados até agora

### Diretório principal de Fase 2

Foi criado o diretório `fase2/` com esta estrutura:

```
fase2/
├── README.md
├── requirements.txt
├── parte1/
│   ├── README.md
│   ├── sintomas_pacientes.txt
│   ├── mapa_sintomas_doencas.csv
│   └── diagnostico_sintomas.py
└── parte2/
    ├── README.md
    ├── frases_risco.csv
    └── classificador_risco.py
```

### Arquivo TXT de frases

Arquivo: [fase2/parte1/sintomas_pacientes.txt](fase2/parte1/sintomas_pacientes.txt)

Conteúdo: 10 frases simulando relatos de sintomas do paciente e suas condições.

### CSV de mapa de conhecimento

Arquivo: [fase2/parte1/mapa_sintomas_doencas.csv](fase2/parte1/mapa_sintomas_doencas.csv)

Esse arquivo associa palavras-chave a doenças, como:

- dor no peito + aperto no tórax → Infarto
- cansaço constante + fadiga → Insuficiência Cardíaca
- falta de ar + dificuldade para respirar → Angina

### Script de extração de sintomas

Arquivo: [fase2/parte1/diagnostico_sintomas.py](fase2/parte1/diagnostico_sintomas.py)

Função:

- lê frases do TXT
- normaliza o texto
- compara palavras-chave com o mapa de sintomas
- sugere diagnóstico

### Dataset de risco

Arquivo: [fase2/parte2/frases_risco.csv](fase2/parte2/frases_risco.csv)

Estrutura:

- coluna `frase`
- coluna `situacao`
- rótulos: `alto risco` e `baixo risco`

### Classificador de risco

Arquivo: [fase2/parte2/classificador_risco.py](fase2/parte2/classificador_risco.py)

Tecnologia utilizada:

- `TfidfVectorizer`
- `LogisticRegression`
- `train_test_split`
- `accuracy_score`
- `classification_report`

---

## 5) Validações executadas

### Script de Parte 1

Comando executado:

```bash
py -3 "c:\Users\dorta\Dropbox\00 FIAP\Ano 02_Fase_02\Ano 02 Fase 02 Tarefa Cap 1\cardioia-fase1-main\fase2\parte1\diagnostico_sintomas.py"
```

Resultado verificado:

- O script executou com sucesso
- Produziu diagnósticos para as 10 frases de exemplo
- Diagnósticos foram sugeridos com base no mapa de conhecimento

### Script de Parte 2

Comando executado:

```bash
py -3 "c:\Users\dorta\Dropbox\00 FIAP\Ano 02_Fase_02\Ano 02 Fase 02 Tarefa Cap 1\cardioia-fase1-main\fase2\parte2\classificador_risco.py"
```

Resultado verificado:

- O script executou com sucesso
- Acurácia obtida: 0.60
- Modelo demonstrou funcionalidade inicial, mas ainda precisa de mais dados para robustez

Observação importante:

- O classificador é funcional como prova de conceito
- Ele ainda não atende ao nível de qualidade esperado para uma entrega definitiva de atividade acadêmica

---

## 6) Observações técnicas importantes

### 1. O ambiente Python funciona

Foi confirmado que a máquina possui Python 3.12 e as bibliotecas necessárias para este estágio:

- pandas
- sklearn

### 2. O projeto ainda está em fase de construção

As implementações criadas até agora são um ponto de partida e servem como base para continuar em outra sessão.

### 3. Há um claro desvio entre a fase atual e a documentação do projeto

A pasta raiz ainda está centrada em Fase 1 e precisa ser reorganizada para refletir a Fase 2 antes da entrega final.

---

## 7) O que foi aprendido até agora

- A estrutura da Fase 2 pode ser organizada em módulos separados
- A lógica de detecção por regras é simples e funcional para uma prova de conceito
- O classificador com TF-IDF funciona e é adequado ao objetivo da atividade
- O repositório precisa ser atualizado para refletir a nova etapa do projeto
- O restante da entrega exige trabalho em front-end e visão computacional

---

## 8) Próximo passo recomendado para continuar em outro momento

A sequência mais lógica para continuidade é:

1. Melhorar a Parte 1 com mais termos e regras de extração
2. Expandir o dataset da Parte 2 com frases mais diversas
3. Melhorar a acurácia do classificador e documentar a análise
4. Atualizar o README principal para a Fase 2
5. Implementar o portal React + Vite
6. Criar o notebook de MLP para ECG
7. Preparar vídeo e finalização do GitHub

---

## 9) Arquivos importantes para continuar

- [Enunciado.md](Enunciado.md)
- [README.md](README.md)
- [FASE2_CHECKLIST.md](FASE2_CHECKLIST.md)
- [fase2/README.md](fase2/README.md)
- [fase2/parte1/diagnostico_sintomas.py](fase2/parte1/diagnostico_sintomas.py)
- [fase2/parte2/classificador_risco.py](fase2/parte2/classificador_risco.py)

---

## 10) Status final

Status atual do projeto:

- Base teórica e analítica concluída
- Estrutura inicial da Fase 2 implementada
- Parte 1 funcional
- Parte 2 funcional em prova de conceito
- Entrega final incompleta

Em outras palavras, o projeto já foi movimentado para o caminho correto, mas ainda não está pronto para a entrega final da atividade.
