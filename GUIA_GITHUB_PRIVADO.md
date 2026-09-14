# Como criar um repositório privado e enviar a solução do VS Code

Este guia usa o site do GitHub e o terminal PowerShell integrado ao VS Code para publicar a versão salva deste projeto, incluindo a pasta `fase2`.

Na verificação realizada para preparar este documento, a pasta `cardioia-fase1-main` ainda não era um repositório Git. Os comandos abaixo devem ser executados por você, na ordem indicada. Criar este guia não cria o repositório nem envia arquivos.

## 1. Salvar a versão atual e abrir o terminal

1. No VS Code, use **Arquivo > Salvar Tudo** para salvar todos os arquivos abertos. O Git envia o conteúdo salvo em disco.
2. Abra **Terminal > Novo Terminal** e selecione **PowerShell**.
3. Entre na raiz da solução:

```powershell
Set-Location -LiteralPath 'C:\Users\dorta\Dropbox\00 FIAP\Ano 02_Fase_02\Ano 02 Fase 02 Tarefa Cap 1\cardioia-fase1-main'
```

4. Confira a pasta e a instalação do Git:

```powershell
Get-Location
git --version
```

O caminho deve terminar em `cardioia-fase1-main`, e o segundo comando deve exibir a versão do Git. Se o Git não estiver instalado, instale o [Git para Windows](https://git-scm.com/download/win), reabra o VS Code e repita a verificação.

## 2. Criar um repositório privado no GitHub

1. Entre na sua conta do [GitHub](https://github.com).
2. Abra a página [New repository](https://github.com/new).
3. Em **Owner**, escolha sua conta ou a organização desejada.
4. Em **Repository name**, informe um nome, por exemplo: `cardioia-fase2`.
5. Em **Description**, opcionalmente informe: `Projeto CardioIA — solução desenvolvida para a FIAP`.
6. Em visibilidade, selecione **Private**.
7. Deixe a criação do README desativada e selecione **None** para `.gitignore` e licença. O projeto local já possui arquivos; o repositório remoto deve começar vazio.
8. Clique em **Create repository**.
9. Na página seguinte, selecione **HTTPS** e copie a URL do repositório. Ela terá este formato:

```text
https://github.com/SEU_USUARIO/cardioia-fase2.git
```

Substitua `SEU_USUARIO` pelo proprietário escolhido. Se usou outro nome de repositório, substitua também `cardioia-fase2` nos comandos deste guia.

## 3. Inicializar o Git e configurar a autoria

No terminal do VS Code, execute:

```powershell
git init -b main
```

Configure seu nome e e-mail para os commits deste projeto, substituindo os exemplos:

```powershell
git config user.name "Seu Nome"
git config user.email "seu-email@example.com"
```

Use um e-mail associado à sua conta do GitHub ou o endereço `noreply` disponível nas configurações de e-mail da conta. Essas configurações identificam a autoria; elas não fazem login.

## 4. Conferir o que será enviado

O `.gitignore` existente exclui, entre outros: `CLAUDE.md`, `HISTORICO.md`, `_interno/`, `.claude/`, caches Python, arquivos `.zip` e `.jpeg`. Esses itens não entram no envio normal.

Se alguma imagem `.jpeg` fizer parte da entrega, revise essa regra antes de continuar. Para entender por que um arquivo foi ignorado, use `git check-ignore -v caminho/do/arquivo`.

Caso existam arquivos locais de credenciais ou ambientes virtuais, acrescente ao `.gitignore`, conforme necessário:

```gitignore
# Credenciais e ambientes locais
.env
.env.*
!.env.example
.venv/
venv/
```

O arquivo `.env.example`, caso exista, deve conter apenas exemplos sem credenciais reais.

Confira os arquivos candidatos ao envio:

```powershell
git status --short
git add --dry-run .
```

Revise a lista para confirmar que inclui a solução desejada e não contém senhas, tokens ou arquivos locais indevidos. Mesmo em um repositório privado, mantenha credenciais fora do versionamento.

## 5. Registrar a versão atual em um commit

Adicione todos os arquivos não ignorados da pasta atual e de suas subpastas:

```powershell
git add .
git diff --cached --stat
git status
```

Confira o resumo. Para retirar um arquivo da seleção inicial sem apagá-lo do computador, execute `git rm --cached -- "caminho/do/arquivo"` e adicione a regra correspondente ao `.gitignore`. Se modificar o `.gitignore`, execute `git add .gitignore` novamente.

Quando a seleção estiver correta, crie o commit:

```powershell
git commit -m "Adiciona versao atual da solucao CardioIA"
```

O commit registra a versão localmente. O envio ao GitHub acontece no próximo passo.

## 6. Conectar ao repositório e enviar

Substitua a URL pela URL HTTPS copiada no passo 2:

```powershell
git remote add origin https://github.com/SEU_USUARIO/cardioia-fase2.git
git remote -v
git push -u origin main
```

Na primeira publicação, o Git pode solicitar autenticação. Se abrir uma janela ou o navegador, entre na conta que tem acesso ao repositório e conclua a autorização. Se houver solicitação de senha no terminal, a senha comum do GitHub não funciona para operações Git por HTTPS; use a autenticação pelo gerenciador de credenciais ou um token de acesso pessoal com permissão para esse repositório. Não coloque o token na URL nem em arquivos do projeto.

Espere o comando terminar sem erros. A opção `-u` associa a branch local `main` à branch remota para facilitar os próximos envios.

## 7. Verificar a publicação

1. Atualize a página do repositório no GitHub.
2. Confirme o indicador **Private** ao lado do nome.
3. Confirme que a branch selecionada é `main`.
4. Confira o último commit e a presença das pastas esperadas, como `assets`, `data`, `docs` e `fase2`, além do `README.md`.
5. No terminal, execute:

```powershell
git status
git log -1 --oneline
```

O status deve indicar que a branch está atualizada com `origin/main` e que não existem alterações pendentes, desde que você não tenha modificado arquivos após o commit.

O `README.md` atual contém um link para o repositório original `Guibeast/cardioia-fase1`. Se desejar que a documentação aponte para sua nova cópia, atualize esse link e publique a alteração usando o passo seguinte.

## 8. Enviar futuras alterações

Depois de editar os arquivos, use **Salvar Tudo** e execute, na raiz do projeto:

```powershell
git status
git add .
git diff --cached --stat
git commit -m "Descreve as alteracoes realizadas"
git push
```

Revise a seleção antes do commit e troque a mensagem por uma descrição do que mudou. Não é necessário repetir `git init` ou `git remote add`.

## Problemas comuns

| Mensagem ou situação | Como resolver |
|---|---|
| `git` não é reconhecido | Instale o Git para Windows e reabra o VS Code. |
| `Author identity unknown` | Execute os dois comandos de configuração de nome e e-mail do passo 3. |
| `remote origin already exists` | Confira `git remote -v`. Se a URL estiver errada, use `git remote set-url origin URL_CORRETA`. |
| `Repository not found` | Confira o proprietário, o nome da URL e se a conta autenticada tem acesso ao repositório privado. |
| `src refspec main does not match any` | Confira se o primeiro commit foi criado e execute `git branch --show-current`. Se a branch tiver outro nome e você quiser usar `main`, renomeie com `git branch -m main`. |
| Push rejeitado com `non-fast-forward` ou `fetch first` | O remoto já possui commits. Execute `git fetch origin` e `git log --oneline --graph --all` para conferir os históricos antes de integrá-los. Não use `--force` para contornar o problema. |
| `nothing to commit, working tree clean` | Não há novas alterações salvas para registrar. Se já houver um commit ainda não enviado, execute `git push`. |

## Referências oficiais

- [Criar um repositório no GitHub](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository).
- [Enviar código local ao GitHub](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github).
- [Autenticação por HTTPS e armazenamento de credenciais](https://docs.github.com/en/get-started/git-basics/caching-your-github-credentials-in-git).
