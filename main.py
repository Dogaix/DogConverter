from pydub import AudioSegment
import os

def detect_format(file_path):
    """Função para detectar o formato do arquivo."""
    return file_path.split('.')[-1]

def convert_audio(input_folder, output_folder, target_format):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file in os.listdir(input_folder):
        input_path = os.path.join(input_folder, file)
        if os.path.isfile(input_path):
            input_format = detect_format(file)
            output_path  = os.path.join(output_folder, file.replace(f".{input_format}", f".{target_format}"))
            sound        = AudioSegment.from_file(input_path, format=input_format)
            sound.export(output_path, format=target_format)
            print(f"Convertido: {input_path} -> {output_path}")
            os.remove(input_path)
            print(f"Removido: {input_path}")

def main():
    print("""\033[1;34m
.------------------------.
|                        |
|      DogConverter      |
|           by           |
|         Dogaix         |
|                        |
'------------------------'
\033[0m""")
    formato2 = input("Formato que quer converter: ").strip()
    convert_audio("convert", "convert", formato2)
    print("""
=============================================

         Conversão completa!
  Seus arquivos foram convertidos com sucesso.

=============================================
""")

if __name__ == "__main__":
    main()