<h1 align="center"> Calculadora de notas (Colegio Anchieta)</h1>

<p align="center">
<img src="https://img.shields.io/badge/STATUS-FINALIZADO-brightgreen"/>
</p>

# 🐱‍🚀 Descrição do projeto

Projeto simples, requisitado pela necessidade de os alunos de terem um meio de saberem rapidamente quantos pontos faltam para passarem de ano (a escola é dividida em três trimestres).
O programa usando a biblioteca sqlite3 pega as notas dos dois primeiros trimestres e calcula quantos pontos faltam para passar de ano em conjunto as médias durante ano letivo, armazenando na base de dados e permitindo a visualização dessa informação posteriormente.

# 📁 Acesso ao projeto

**https://github.com/pexonaut/final-grade**

# 🛠️ Abrir e rodar o projeto

**Fazer dowload do projeto e abrir em um compilador que suporte a linguagem Python (Visual Studio, Pycharm, Jupyter, etc...)**

# 🤖 Variaveis

* conexao/cursor = conexão com a biblioteca sqlite3
* inserir_menu = resposta utilizada na funcionalidade do primeiro menu
* materia_escolhida = determina a materia visualizada ou calculada
* repe = utilizado na reinicialização do programa
* g1/g2/g3/p1/p2 = variaveis que são atribuidas as notas do 1° trimestre
* globo1/globo2/globo3/px1/px2 = variaveis que são atribuidas as notas do 2° trimestre
* lista1/lista2 = Variaveis que compilam as notas do 1° e 2° trimestre em uma lista
* pe/pxe = a soma de p1 + p2 ou px1 + px2
* nt1 e nt2/nota1 e nota2 = as duas maiores notas selecionadas por max() e a biblioteca heapq
* mdp e media = as médias do 1° e 2° trimestre
* ptf = quantidades de pontos que faltam para a conclusão do ano
* rapariga = representação str da variavel ptf
* materia_(abreviação da matéria) = A variavel que representa as matérias escolhidas nos menus e na parte de visualização (vão de 1 a 7)


# 📚 Autor

| [<img src="https://avatars.githubusercontent.com/u/114774026?v=4" width=115><br><sub>Enzo Bueno de Almeida</sub>](https://github.com/pexonaut) |
| :---: |
