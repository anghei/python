from google_trans_new import google_translator
import requests

translator = google_translator()

with open('task-4.txt', encoding='utf-8') as en:
    with open('task-4-ru.txt', 'w', encoding='utf-8') as ru:
        for line in en:
            translate_text = translator.translate(line, lang_tgt='ru')
            print(translate_text, file=ru)

# print(translate_text)