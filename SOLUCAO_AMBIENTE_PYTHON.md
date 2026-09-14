# Solução do problema com o ambiente Python e pip

## Problema identificado

O comando abaixo parecia "não funcionar" ou não estava sendo aplicado no ambiente correto:

```powershell
python -m pip install --upgrade pip
```

A causa raiz foi que o terminal estava usando o Python do Windows Store (`python.exe` do sistema), e não o ambiente virtual do projeto. Além disso, o ambiente virtual `.venv` tinha o `pip` corrompido.

## Diagnóstico

### 1) Verificar qual Python está sendo usado

```powershell
where python
python --version
python -m pip --version
```

No caso do problema, o resultado foi:

```powershell
C:\Users\dorta\AppData\Local\Microsoft\WindowsApps\python.exe
```

Isso mostra que o `python` em uso não era o do ambiente do projeto.

### 2) Verificar o ambiente virtual do projeto

```powershell
.\.venv\Scripts\Activate.ps1
python --version
python -m pip --version
```

No ambiente quebrado, apareceu o erro:

```powershell
ModuleNotFoundError: No module named 'pip._internal.cli.main'
```

Isso indica que a instalação do `pip` dentro da venv estava corrompida.

---

## Solução aplicada

### Passo 1: Ativar a venv do projeto

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

### Passo 2: Reparar o pip quebrado

```powershell
python -m ensurepip --upgrade
```

### Passo 3: Reinstalar o pip, setuptools e wheel

```powershell
python -m pip install --upgrade --force-reinstall pip setuptools wheel
```

### Passo 4: Verificar se o pip foi corrigido

```powershell
python -m pip --version
```

Resultado esperado:

```powershell
pip 26.2.1 from C:\...\.venv\Lib\site-packages\pip (python 3.12)
```

### Passo 5: Atualizar o pip final

```powershell
python -m pip install --upgrade pip
```

---

## Comandos úteis para evitar o problema

### Usar o Python correto no Windows

Se o comando `python` estiver apontando para o Windows Store, prefira:

```powershell
py -3 -m pip --version
py -3 -m pip install --upgrade pip
```

### Ativar a venv antes de instalar pacotes

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install <pacote>
```

### Verificar se a venv está ativa

```powershell
python -c "import sys; print(sys.executable)"
```

Se estiver funcionando corretamente, o caminho deve apontar para a pasta `.venv` do projeto.

---

## Recomendação final

Sempre que for trabalhar no projeto:

1. abrir o terminal;
2. ativar a venv;
3. verificar `python -m pip --version`;
4. instalar ou atualizar dependências com `python -m pip ...`.

Evite usar `python` puro sem confirmar qual ambiente está sendo utilizado.

---

## Resumo

O erro não era do comando em si, mas do ambiente de execução.

- `python` global do Windows → ambiente errado
- `.venv` com `pip` corrompido → erro real
- solução → ativar a venv, corrigir `pip` e reinstalar o pacote do ambiente correto

Com isso, o problema foi resolvido e o pip passou a funcionar corretamente no projeto.
