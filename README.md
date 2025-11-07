#  Projeto de Colaboração com Git & GitHub (Python)

Esta atividade simula um fluxo de trabalho de desenvolvimento de software em equipe, focando na colaboração através do Git, na prática de revisão de código (Code Review) e na responsabilidade compartilhada pela qualidade do código.

##  Linguagem utilizada

* Python 3

##  Equipe

Este projeto é desenvolvido pela seguinte equipe:

* **Mantenedor(a) :** `Naili Marques`
    * *Responsabilidade:* Criar o repositório, proteger a branch `main`, revisar todos os Pull Requests e fazer o "merge" final.
* **Desenvolvedor(a) 1:** `Rachel Franco`
    * *Funcionalidade:* `sao_anagramas()`
* **Desenvolvedor(a) 2:** `Giovanna Hirata`
    * *Funcionalidade:* `cifra_de_cesar()`
* **Desenvolvedor(a) 3:** `Diego Hurtado de Mendoza`
    * *Funcionalidade:* `encontrar_maior_palavra()`

##  Funcionalidades Implementadas

O arquivo `solucoes.py` contém a implementação das seguintes funções lógicas:

1.  **`sao_anagramas(string1, string2)`**
    * Verifica se duas strings são anagramas uma da outra.
    * A verificação ignora espaços e diferenças entre maiúsculas e minúsculas.

2.  **`cifra_de_cesar(texto, deslocamento)`**
    * Aplica a Cifra de César a uma string, deslocando cada letra no alfabeto.
    * Preserva maiúsculas/minúsculas e não altera caracteres não-alfabéticos (números, pontuação, espaços).
    * O alfabeto é tratado de forma circular (ex: `z` + 3 → `c`).

3.  **`encontrar_maior_palavra(frase)`**
    * Encontra e retorna a maior palavra em uma frase.
    * A pontuação anexada às palavras é ignorada na contagem de comprimento.
    * Se houver empate, retorna a primeira maior palavra encontrada.

##  Como Usar

1.  Clone este repositório:
    ```bash
    git clone [git@github.com:nah5f4/Atividade-Pratica-3.git]
    cd Atividade-Pratica-3
    ```

2.  (Opcional, mas recomendado) Crie e ative um ambiente virtual:
    ```bash
    # No Windows
    python -m venv .venv
    .\.venv\Scripts\activate

    # No macOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  Abra um shell Python (digitando `python` ou `python3`) e importe as funções para testar:
    ```python
    from solucoes import sao_anagramas, cifra_de_cesar, encontrar_maior_palavra

    # Exemplo de teste
    print(f"Amor e Roma são anagramas? {sao_anagramas('amor', 'roma')}")
    print(f"Cifra de 'abc' com 2: {cifra_de_cesar('abc', 2)}")
    print(f"Maior palavra em 'O rato roeu a roupa': {encontrar_maior_palavra('O rato roeu a roupa')}")
    ```

##  Fluxo de Trabalho (Git Flow)

Este projeto segue um fluxo para garantir a qualidade do código e praticar a colaboração.

1.  **Branch `main` Protegida:**
    * A branch `main` é protegida.
    * **Ninguém** pode enviar `push` diretamente para ela.
    * Todas as mudanças devem passar por um Pull Request.

2.  **Desenvolvimento em Branches:**
    * Cada desenvolvedor cria uma branch própria a partir da `main` para sua funcionalidade (ex: `feat/funcao-anagrama`).
    * `git checkout -b nome-da-branch`

3.  **Pull Request (PR):**
    * Quando a funcionalidade está pronta, o desenvolvedor envia sua branch para o GitHub (`git push origin nome-da-branch`).
    * Em seguida, abre um Pull Request no GitHub, com o objetivo de mesclar sua branch na `main`.

4.  **Code Review (Revisão de Código):**
    * O Mantenedor (e outros membros da equipe) devem revisar o PR.
    * O feedback é dado através de comentários nas linhas de código.
    * O autor do PR discute e aplica as correções (fazendo novos commits na sua branch, que atualizam o PR automaticamente).

5.  **Merge:**
    * Somente após o PR ser **aprovado** pelo Mantenedor, ele pode clicar em "Merge pull request".
    * Isso integra a nova funcionalidade à branch `main`.

6.  **Sincronização:**
    * Após um merge, todos os membros devem atualizar suas cópias locais da `main`:
    ```bash
    git checkout main
    git pull origin main
    ```
