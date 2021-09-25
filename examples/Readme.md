<p align="center">
  <img src="../.github/logo.png" width=300 alt="Curso em Vídeo">
</p>
<h1 align="center">EXEMPLOS</h1>

# 📌 Sobre

Exemplos desenvolvidos nas aulas teóricas do curso.

# 📌 Índice

### ⚙️ Aula 6 – Tipos Primitivos e Saída de Dados
- Funcionamento dos tipos primitivos no Python e as peculiaridades do `int() `, `float()`, `bool()` e `str()` e as primeiras operações com a função `print()` do Python.

### ⚙️ Aula 7 – Operadores Aritméticos
- Funcionamento dos operadores de adição, subtração, multiplicação, divisão, exponenciação e quociente e também sua ordem de precedência dentro de expressões matemáticas. 

- **Operadores**
  - `+` ⇒ adição
  - `-` ⇒ subtração
  - `*` ⇒ multiplicação
  - `/` ⇒ divisão
  - `**` ⇒ potência
  - `//` ⇒ divisão inteira
  - `%` ⇒ resto da divisão (módulo)
  - `==` ⇒ igual

- **Ordem de precedência**
  - `( )`
  - `**`
  - `*` `/` `//` `%`
  - `+` `-`

### ⚙️ Aula 8 – Utilizando Módulos
- Utilização de módulos em Python utilizando os comandos `import` e `from/import` no Python. Carregamento das bibliotecas de funções e utilização de vários recursos adicionais nos seus programas utilizando módulos `built-in` e módulos externos, oferecidos no `Pypi`.

### ⚙️ Aula 9 – Manipulando Texto
- Utilização das operações com String => fatiamento de String, análise com `len()`, `count()`, `find()`, transformações com `replace()`, `upper()`, `lower()`, `capitalize()`, `title()`, `strip()`, junção com `join()`.

### ⚙️ Aula 10 – Condições
- Utilização de estruturas condicionais simples e compostas.

### ⚙️ Aula 11 – Cores no Terminal
- Utilização dos códigos de escape sequence ANSI para configurar cores.

### ⚙️ Aula 12 – Condições Aninhadas
- Criação de estruturas condicionais aninhadas, usando os comandos `if`, `elif` e `else`

### ⚙️ Aula 13 - Estrutura de repetição `for`
- Utilização do `for` => que é uma estrutura versátil e simples.

### ⚙️ Aula 14 - Estrutura de repetição `while`
- Utilização do `while` => outra estrutura de repetição.

### ⚙️ Aula 15 - Interrompendo repetições `while`
- Utilização da a instrução `break` e os loopings infinitos a favor das estratégias de código. É muito importante saber usar o `break` no Python, já que em alguns casos precisamos interromper um laço no meio do caminho.

### ⚙️ Aula 16 - Tuplas
- As tuplas são variáveis compostas e imutáveis que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

### ⚙️ Aula 17 e 18 - Listas
- As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

  **Alguns comandos:**
  - `x.append(y)` ⇒ adiciona o elemento `y` no final da lista `x`
  - `x.insert(a, y)` ⇒ adiciona o elemento `y` na posição `a` da lista `x`
  - `del x[y]` ⇒ elimina o elemento na posição `y` da lista `x`
  - `x.pop(a)` ⇒ elimina o elemento na posição `a` da lista `x`
      - caso não seja informada a posição, será eliminado o último elemento
  - `x.remove(y)` ⇒ elimina o elemento `y` da lista `x`
  - `x.sort()` ⇒ ordena os valores da lista `x`
  - `x.sort(reverse=True)` ⇒ ordena em ordem decrescente os valores da lista `x`
  - `x = list(range(4, 11))` ⇒ lista ordenada de 4 a 10

### ⚙️ Aula 19 - Dicionários 
- Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves literais.

  **Alguns comandos:**
  - `del dados['idade']` => remove o elemento idade
  - `x.values()` => identifica o valor do elemento
  - `x.keys()` => identfica a chave do elemento
  - `x.items()` => identifica o elemento

### ⚙️ Aula 20 e 21 - Funções
- Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python.****************
- vinculadas a palavra rotina ⇒ algo que se faz constantemente
- `def xxx()` ⇒ definição de uma função
- **empacotamento** ⇒ serão passados vários e serão jogados dentro do parâmetro
  `def contador(*num):`
- é possível utilizar as funções com lista também
  `def dobra(lst):`

- **Interactive Help**
    - ajuda interativa às funções do python
    - pode ser utilizada no console ou no pycharm
    - `help(<nome da função>)`
    - `print(<nome da função>.__doc__)`
- **DocStrings**
    - string de documentação
    - a função `help()` demonstra a **docString** das funções do python
    - Criação de uma **docString** para um função criada pelo usuário
        - logo abaixo do comando `def` ⇒ abrir e fechar 3 x aspas duplas (")
        - colocar as instruções da função
       
- **Parâmetros Opcionais**
    - Para utilização de parâmetros opcionais, é só incluir um valor default para os parâmetros da função
   
- **Escopo de variáveis**
    - escopo ⇒ local onde a variável existe
    - escopo global ⇒ variável funciona dentro de fora das funções
    - escopo local ⇒ variável definida dentro de uma função ⇒ só funciona dentro da função
    - Caso a variável global seja declarada dentro da função com a palavra reservada `global` a mesma passa a ter o novo valor, mesmo fora da função

- **Retorno de valores**
    - As funções podem ou não retornar valor
    - `return`
    - Retornando uma função, é possível jogar em uma variável ou diretamente no print

### ⚙️ Aula 22 - Módulos e Pacotes

- Foi criado um projeto em separado para facilitar a demonstração de módulos e pacotes. Para acessar [clique aqui!](../modularizacao)

### ⚙️ Aula 23 - Tratamento de erros e exceções
************


# 👩‍💼 Author
<img src="../.github/picture.png" width="100px;" alt="Picture"/>
<p><b>Nádia Ligia, budding back-end developer.</b></p>
<a href="https://www.linkedin.com/in/nlnadialigia/">
  <img alt="Linkedin" src="https://img.shields.io/badge/-Linkedin -8703A4?style=flat&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/nlnadialigia/" />
</a>&nbsp;
<a href="mailto:nlnadialigia@gmail.com">
  <img alt="Email" src="https://img.shields.io/badge/-Email-8703A4?style=flat&logo=Gmail&logoColor=white&link=mailto:nlnadialigia@gmail.com" />
</a>&nbsp;
<a href="https://www.nlnadialigia.com">
  <img alt="Homepage" src="https://img.shields.io/badge/-Homepage-8703A4" />
</a>