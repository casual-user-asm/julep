from translate import Translator


def translate_file(file, code_lang):
    translator = Translator(to_lang=code_lang)
    with open(file, "r", encoding="utf-8") as f:
        text = f.read()
    translated_text = translator.translate(text)

    if code_lang == "zh":
        code_lang = "cn"
    elif code_lang == "ja":
        code_lang = "jp"

    with open(f"README-{code_lang.upper()}.md", "w", encoding="utf-8") as f:
        f.write(translated_text)


if __name__ == "__main__":
    file = "README.md"
    languages = ["zh", "fr", "ja"]
    for lang in languages:
        translate_file(file, lang)
