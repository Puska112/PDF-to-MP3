import pdfplumber as pd
from gtts import gTTS
from pathlib import Path


def convert(file_path='test.pdf', language='en'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':

        print('Подождите...')

        with pd.open(file_path) as pdf_file:
           page = [page.extract_text() for page in pdf_file.pages]
        text = ''.join(page)
        text = text.replace('\n', '')

        final_file = gTTS(text=text, lang=F'{language}')
        file_name = Path(file_path).stem
        final_file.save(F"{file_name}.mp3")
        return print(F"{file_name}.mp3 успешно сохранен!")
    else:
        return print("Не обработано. Проверьте файл или путь к файлу.")


def main():
    language = input('Выберете язык, например "ru" или "en": ' )
    file_name = input('Введите путь к PDF файлу: ')
    convert(file_path=f'{file_name}', language=f'{language}')

if __name__ == '__main__':
    main()
