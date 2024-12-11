# Figuras 2D manipuladas com OpenCV

Este projeto tem como objetivo demonstrar a manipulação de figuras geométricas simples (quadrado, triângulo e círculo) sobre um vídeo ao vivo, usando a biblioteca OpenCV. As figuras são movidas pela tela, alteram suas cores entre azul e vermelho, além de alternar entre diferentes formas de maneira dinâmica.

## Funcionalidades

- **Movimento das Figuras**: As figuras geométricas se movem pela tela de maneira automática.
- **Troca de Cores**: A cor da figura alterna entre azul e vermelho, com a tecla `c` do teclado.
- **Troca de Formas**: A figura pode ser alterada entre quadrado, triângulo e círculo, com a tecla `s` do teclado.
- **Interação com o Usuário**: O programa permite a interação com o usuário para modificar a cor e a forma da figura em tempo real.

## Requisitos

- **Python 3.x**
- **OpenCV**: Biblioteca necessária para capturar frames da webcam e desenhar as figuras.

Para instalar as dependências, use o seguinte comando:

```bash
pip install -r requirements.txt
```

## Como Usar

1. Clone ou baixe o repositório.
2. Abra o terminal ou prompt de comando na pasta do projeto.
3. Execute o arquivo Python:

```bash
python will.py
```

4. O programa abrirá a câmera e exibirá a figura (inicialmente um quadrado azul) se movendo na tela.
5. Pressione as teclas abaixo para interagir com o programa:
   - **`c`**: Alterna entre as cores azul e vermelho.
   - **`s`**: Alterna entre as formas quadrado, triângulo e círculo.
   - **`q`**: Encerra o programa.

## Como Funciona

- **Captura de vídeo**: O programa captura frames ao vivo da webcam usando a função `cv2.VideoCapture`.
- **Movimento da Figura**: A figura é movida por um deslocamento (dx, dy).
- **Desenho da Figura**: Dependendo da forma selecionada (quadrado, triângulo ou círculo), a figura é desenhada usando as funções do OpenCV (`cv2.line`, `cv2.circle`).
- **Troca de Cores e Formas**: As teclas `c` e `s` permitem alternar entre cores e formas. As cores são alternadas entre azul e vermelho, enquanto as formas são trocadas entre quadrado, triângulo e círculo.

## Vídeo demonstrativo

- Assista ao [vídeo]('./video_demonstrativo/will.mp4') demonstrativo da aplicação