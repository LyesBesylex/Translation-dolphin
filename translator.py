import deepl



class translation:
    def translate(text, target):
        auth_key = "fda59a42-7456-da4c-771c-36b1bab7595c:fx"
        translator = deepl.Translator(auth_key)
        result = translator.translate_text(text, target)
        return result.text