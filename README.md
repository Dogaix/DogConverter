## DogConverter
  DogConverter é um conversor básico de áudio criado em Python. Permite converter e alterar o formato original do áudio usando somente a biblioteca Pydub.

## Requisitos
  Para usar o DogConverter, certifique-se de ter os seguintes requisitos instalados:
  - Python 3.6 ou superior
  - Biblioteca `Pydub` (instalável via pip)
  - `ffmpeg` (uma ferramenta externa para manipulação de áudio e vídeo) encontrada [aqui](https://ffmpeg.org/)

## Descrição
  O DogConverter utiliza a biblioteca `Pydub` para manipular arquivos de áudio e requer a presença do `ffmpeg` para funcionar corretamente. Ele pode ser utilizado para converter arquivos de áudio de um formato para outro de forma simples e eficaz.

## Instalação dos Requisitos
  1. **Python**: Verifique se você possui o Python instalado executando o comando `python --version` no seu terminal.
  2. **Instalação da biblioteca `Pydub`**: Utilize o `pip` para instalar a biblioteca `Pydub`:

  ```bash
  pip install pydub
  ```
     
## Instalação do ffmpeg:
  - Windows: Baixe o executável do ffmpeg aqui e adicione-o ao seu PATH.
  - Linux: Instale o ffmpeg usando o gerenciador de pacotes da sua distribuição. Por exemplo, no Ubuntu:

  ```bash
  sudo apt update
  sudo apt install ffmpeg
  ```

## Uso
Para utilizar o DogConverter, execute o script conforme descrito no arquivo `README.md`. O programa solicitará o formato para o qual deseja converter os arquivos de áudio localizados na pasta de entrada.

> Feito com ❤️ por Dogaix
