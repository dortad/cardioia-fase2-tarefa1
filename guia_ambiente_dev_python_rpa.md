# Guia prático: ambiente de desenvolvimento local para RPA com Python

**Base:** apostila *RPA: Bots que Libertam Humanos*, especialmente as seções **2 Ambiente de Desenvolvimento** e **3 Ambientes Virtuais Python**.  
**Objetivo:** configurar um ambiente local simples, organizado e reproduzível para desenvolver automações/RPA em Python usando uma IDE, em **Windows** e **Linux**.

---

## 1. Ideia central do ambiente

Para projetos de RPA, o ambiente local deve ter quatro peças principais:

1. **Python instalado corretamente** no sistema operacional.
2. **IDE/editor** para escrever e organizar o código.
3. **Ambiente virtual Python (`venv`)** para isolar bibliotecas de cada projeto.
4. **Gerenciamento de pacotes com `pip` e `requirements.txt`** para instalar e reproduzir dependências.

A apostila destaca que a instalação correta do interpretador Python é uma etapa fundamental para desenvolver soluções confiáveis e reproduzir experimentos computacionais. Ela também enfatiza o uso de ambientes virtuais com `venv` para manter dependências consistentes entre projetos diferentes.

---

## 2. Estrutura recomendada de pastas

Crie uma pasta principal para seus projetos de automação. Exemplo:

### Windows

```text
C:\Projetos\rpa-python\
```

### Linux

```text
~/Projetos/rpa-python/
```

Dentro dela, cada robô ou automação deve ficar em sua própria pasta:

```text
rpa-python/
├── robo-extracao-planilha/
│   ├── .venv/
│   ├── src/
│   ├── data/
│   ├── logs/
│   ├── requirements.txt
│   └── README.md
└── robo-baixa-relatorios/
    ├── .venv/
    ├── src/
    ├── data/
    ├── logs/
    ├── requirements.txt
    └── README.md
```

Sugestão prática:

- `src/`: código Python do robô.
- `data/`: arquivos de entrada, planilhas, CSVs e exemplos.
- `logs/`: registros de execução.
- `.venv/`: ambiente virtual do projeto.
- `requirements.txt`: lista das bibliotecas usadas.
- `README.md`: instruções rápidas do projeto.

---

## 3. Configuração no Windows

### 3.1 Instalar Python

1. Acesse o site oficial do Python.
2. Baixe a versão Python 3.x para Windows.
3. Execute o instalador `.exe`.
4. Marque a opção:

```text
Add Python to PATH
```

5. Clique em **Install Now**.
6. Ao final, feche o instalador.

A apostila chama atenção especificamente para marcar **Add Python to PATH**, porque isso permite executar Python e pip diretamente pelo terminal.

### 3.2 Verificar instalação

Abra o **Prompt de Comando** ou o terminal da IDE e execute:

```bat
python --version
pip --version
```

Resultado esperado:

```text
Python 3.x.x
pip x.x.x
```

Caso o comando `python` não funcione, tente:

```bat
py --version
py -m pip --version
```

### 3.3 Criar pasta do projeto

```bat
mkdir C:\Projetos\rpa-python\robo-exemplo
cd C:\Projetos\rpa-python\robo-exemplo
mkdir src data logs
```

### 3.4 Criar ambiente virtual

```bat
python -m venv .venv
```

Alternativa, se seu Windows usa o launcher `py`:

```bat
py -m venv .venv
```

### 3.5 Ativar ambiente virtual no Windows

No Prompt de Comando:

```bat
.venv\Scripts\activate
```

No PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Quando estiver ativo, o terminal normalmente mostra algo parecido com:

```text
(.venv) C:\Projetos\rpa-python\robo-exemplo>
```

Esse prefixo é o “crachá” do ambiente ativo. Sem ele, você pode estar instalando pacote no lugar errado — o clássico “funciona na minha máquina”, primo distante do duende da TI.

### 3.6 Atualizar pip

```bat
python -m pip install --upgrade pip
```

### 3.7 Instalar pacotes básicos para RPA

Exemplo inicial:

```bat
pip install pandas openpyxl requests python-dotenv
```

Para automações com navegador, você pode adicionar depois:

```bat
pip install selenium playwright
```

E, se usar Playwright:

```bat
playwright install
```

### 3.8 Gerar requirements.txt

```bat
pip freeze > requirements.txt
```

### 3.9 Desativar ambiente

```bat
deactivate
```

---

## 4. Configuração no Linux

A apostila separa a instalação por famílias de distribuição: Debian/Ubuntu, Fedora/RHEL/CentOS e Arch Linux.

### 4.1 Ubuntu, Debian e derivados

Atualize os pacotes:

```bash
sudo apt update && sudo apt upgrade -y
```

Instale Python, pip e venv:

```bash
sudo apt install python3 python3-pip python3-venv -y
```

Verifique:

```bash
python3 --version
pip3 --version
```

### 4.2 Fedora, RHEL e CentOS

Atualize os pacotes:

```bash
sudo dnf update -y
```

Instale Python e pip:

```bash
sudo dnf install python3 python3-pip -y
```

Verifique:

```bash
python3 --version
pip3 --version
```

Observação: na apostila aparece `dnv` em um comando, mas o gerenciador correto nas distribuições Fedora/RHEL modernas é `dnf`.

### 4.3 Arch Linux e derivados

Atualize a base de pacotes:

```bash
sudo pacman -Sy
```

Instale Python e pip:

```bash
sudo pacman -S python python-pip
```

Verifique:

```bash
python --version
pip --version
```

### 4.4 Criar pasta do projeto no Linux

```bash
mkdir -p ~/Projetos/rpa-python/robo-exemplo/{src,data,logs}
cd ~/Projetos/rpa-python/robo-exemplo
```

### 4.5 Criar ambiente virtual

Em Ubuntu/Debian/Fedora:

```bash
python3 -m venv .venv
```

Em Arch, normalmente:

```bash
python -m venv .venv
```

### 4.6 Ativar ambiente virtual no Linux

```bash
source .venv/bin/activate
```

Resultado esperado:

```text
(.venv) usuario@maquina:~/Projetos/rpa-python/robo-exemplo$
```

### 4.7 Atualizar pip

```bash
python -m pip install --upgrade pip
```

### 4.8 Instalar pacotes básicos para RPA

```bash
pip install pandas openpyxl requests python-dotenv
```

Para automações com navegador:

```bash
pip install selenium playwright
playwright install
```

### 4.9 Gerar requirements.txt

```bash
pip freeze > requirements.txt
```

### 4.10 Desativar ambiente

```bash
deactivate
```

---

## 5. Configuração da IDE

A apostila não entra em detalhes de uma IDE específica, mas o fluxo abaixo é o mais prático para trabalhar localmente com Python.

### 5.1 Abrir o projeto na IDE

Abra a pasta do projeto, não apenas um arquivo isolado.

Exemplo de pasta correta:

```text
robo-exemplo/
├── .venv/
├── src/
├── data/
├── logs/
└── requirements.txt
```

### 5.2 Selecionar o interpretador Python do ambiente virtual

Na IDE, selecione o Python localizado dentro da pasta `.venv`.

#### Windows

```text
.venv\Scripts\python.exe
```

#### Linux

```text
.venv/bin/python
```

Essa etapa é essencial: a IDE precisa usar o mesmo Python do terminal. Caso contrário, o pacote instala em um lugar e o código roda em outro — a receita oficial para perder uma tarde inteira.

### 5.3 Usar o terminal integrado da IDE

No terminal integrado, confirme se o ambiente está ativo:

```bash
python --version
pip list
```

Se o terminal não mostrar `(.venv)`, ative manualmente:

#### Windows

```bat
.venv\Scripts\activate
```

#### Linux

```bash
source .venv/bin/activate
```

### 5.4 Criar um primeiro arquivo de teste

Crie o arquivo:

```text
src/main.py
```

Conteúdo:

```python
import sys

print("Ambiente Python configurado com sucesso!")
print("Executável Python:", sys.executable)
```

Execute:

```bash
python src/main.py
```

O caminho mostrado em `sys.executable` deve apontar para `.venv`.

---

## 6. Entendendo o ambiente virtual

O `venv` cria uma estrutura isolada para o projeto. Segundo a apostila, esse mecanismo altera principalmente:

- o caminho de instalação dos pacotes;
- a variável `PATH` do sistema;
- o comportamento do interpretador Python;
- a variável `sys.prefix`.

Quando o ambiente está ativo, o Python procura primeiro os executáveis e pacotes dentro do próprio ambiente virtual. Isso evita conflito entre projetos diferentes.

Exemplo prático:

- Projeto A usa `pandas==2.1.0`.
- Projeto B usa `pandas==2.2.0`.
- Cada projeto tem seu próprio `.venv`.
- Um projeto não bagunça o outro.

---

## 7. Instalação e controle de pacotes

### 7.1 Instalar pacote mais recente

```bash
pip install nome-do-pacote
```

Exemplo:

```bash
pip install pandas
```

### 7.2 Instalar versão específica

```bash
pip install pacote==1.2.3
```

Exemplo:

```bash
pip install pandas==2.2.2
```

A apostila destaca que instalar uma versão específica ajuda a manter compatibilidade e evitar atualizações que quebrem o código.

### 7.3 Ver pacotes instalados

```bash
pip list
```

### 7.4 Congelar dependências

```bash
pip freeze > requirements.txt
```

Esse comando registra as versões instaladas, permitindo reconstruir o ambiente depois.

### 7.5 Recriar ambiente a partir de requirements.txt

Depois de criar e ativar um novo `.venv`, execute:

```bash
pip install -r requirements.txt
```

---

## 8. Checklist rápido

Use este checklist sempre que começar um novo projeto RPA em Python.

```text
[ ] Instalei Python 3.x
[ ] Verifiquei python --version ou python3 --version
[ ] Verifiquei pip --version ou pip3 --version
[ ] Criei a pasta do projeto
[ ] Abri a pasta do projeto na IDE
[ ] Criei o ambiente virtual .venv
[ ] Ativei o ambiente virtual
[ ] Configurei a IDE para usar o Python da .venv
[ ] Atualizei o pip
[ ] Instalei os pacotes necessários
[ ] Testei com src/main.py
[ ] Gereei requirements.txt
[ ] Anotei no README.md como executar o robô
```

---

## 9. Comandos resumidos

### Windows

```bat
mkdir C:\Projetos\rpa-python\robo-exemplo
cd C:\Projetos\rpa-python\robo-exemplo
mkdir src data logs
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install pandas openpyxl requests python-dotenv
python -c "import sys; print(sys.executable)"
pip freeze > requirements.txt
deactivate
```

### Linux Ubuntu/Debian

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip python3-venv -y
mkdir -p ~/Projetos/rpa-python/robo-exemplo/{src,data,logs}
cd ~/Projetos/rpa-python/robo-exemplo
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install pandas openpyxl requests python-dotenv
python -c "import sys; print(sys.executable)"
pip freeze > requirements.txt
deactivate
```

### Linux Fedora/RHEL/CentOS

```bash
sudo dnf update -y
sudo dnf install python3 python3-pip -y
mkdir -p ~/Projetos/rpa-python/robo-exemplo/{src,data,logs}
cd ~/Projetos/rpa-python/robo-exemplo
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install pandas openpyxl requests python-dotenv
python -c "import sys; print(sys.executable)"
pip freeze > requirements.txt
deactivate
```

### Linux Arch

```bash
sudo pacman -Sy
sudo pacman -S python python-pip
mkdir -p ~/Projetos/rpa-python/robo-exemplo/{src,data,logs}
cd ~/Projetos/rpa-python/robo-exemplo
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install pandas openpyxl requests python-dotenv
python -c "import sys; print(sys.executable)"
pip freeze > requirements.txt
deactivate
```

---

## 10. Problemas comuns

### Problema 1: `python` não é reconhecido no Windows

Possíveis causas:

- Python não foi adicionado ao PATH.
- A opção **Add Python to PATH** não foi marcada na instalação.

Teste:

```bat
py --version
```

Se funcionar, use:

```bat
py -m venv .venv
py -m pip install --upgrade pip
```

### Problema 2: pacote instalado, mas a IDE não encontra

Causa provável: a IDE está usando outro interpretador Python.

Verifique dentro da IDE:

```python
import sys
print(sys.executable)
```

O resultado deve apontar para `.venv`.

### Problema 3: ambiente virtual não ativa no PowerShell

Ative pelo Prompt de Comando:

```bat
.venv\Scripts\activate
```

Ou ajuste a política de execução do PowerShell conforme a política da sua máquina/empresa.

### Problema 4: instalei pacotes fora do ambiente virtual

Ative o ambiente e reinstale:

```bash
source .venv/bin/activate      # Linux
.venv\Scripts\activate         # Windows CMD
pip install -r requirements.txt
```

---

## 11. Modelo de README.md para cada robô

```markdown
# Nome do robô

## Objetivo
Descrever o processo automatizado.

## Pré-requisitos
- Python 3.x
- Ambiente virtual .venv
- Arquivo requirements.txt instalado

## Como preparar o ambiente

### Windows
```bat
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Como executar
```bash
python src/main.py
```

## Observações
Registrar acessos, arquivos de entrada, logs e exceções conhecidas.
```

---

## 12. Conclusão

Um bom ambiente local evita confusão, reduz erro de instalação e facilita a reprodução do projeto em outra máquina. Para RPA, isso é ainda mais importante porque o robô costuma depender de bibliotecas, arquivos, caminhos, navegadores, planilhas e sistemas externos.

A regra de ouro é simples:

```text
Um projeto = uma pasta = um ambiente virtual = um requirements.txt
```

Seguindo esse padrão, o desenvolvimento fica mais limpo, mais rastreável e muito menos sujeito ao famoso “mas ontem estava funcionando”.
