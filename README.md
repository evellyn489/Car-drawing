# Desenho de carros utilizando OpenGL
OpenGL (Open Graphics Library) é uma biblioteca de computação gráfica amplamente utilizada para renderização de gráficos 2D e 3D. Ela fornece uma API (Interface de Programação de Aplicações) que permite aos desenvolvedores criar e manipular gráficos de alta performance, aproveitando o hardware da GPU (Unidade de Processamento Gráfico) para realizar operações complexas, como renderizar imagens, desenhar objetos, aplicar texturas e executar transformações geométricas.


Este projeto é uma demonstração do uso da biblioteca OpenGL para a criação de um desenho 3D de **três carros vermelhos**. O código foi feito utilizando a linguagem de programação Python.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação usada para desenvolver a aplicação.
- **OpenGL**: Biblioteca principal para renderização gráfica.
- **GLU**: Para facilitar a criação e manipulação de objetos 3D.
- **GLUT**: Utilizada para facilitar o gerenciamento de janelas e interações com o usuário.

## Como Rodar o Projeto

1. **Pré-requisitos**:
   - Instalar o Python
   - Instalar OpenGL, GLU e GLUT.
2. Executar o arquivo `cars_3d`

### Como usar

O projeto permite interações via teclado e mouse para manipular a visualização dos carros 3D.

  **Teclado:**
  - `Seta Esquerda`: Move a câmera ou o objeto para a esquerda.
  - `Seta Direita`: Move a câmera ou o objeto para a direita.
  - `Seta Cima`: Move a câmera ou o objeto para cima (aumenta o valor de `cimabaixo`).
  - `Seta Baixo`: Move a câmera ou o objeto para baixo (diminui o valor de `cimabaixo`).

  **Mouse:**
  - **Botão Esquerdo**: Aproxima a visualização (zoom-in), diminuindo a distância dos carros, enquanto a distância for maior ou igual a 10 unidades.
  - **Botão Direito**: Afasta a visualização (zoom-out), aumentando a distância dos carros, enquanto a distância for menor ou igual a 130 unidades.

## Sobre o Projeto
Este projeto foi desenvolvido como parte de um trabalho da disciplina de Computação Gráfica na Universidade Federal de Alagoas (UFAL). Ele demonstra o uso das bibliotecas OpenGL e GLU para renderização de objetos 3D, focando na criação de objetos tridimensionais.

