from translatepy.translators.google import GoogleTranslate

gtranslate = GoogleTranslate()


def translate(text: str, lang_from: str = 'auto', lang_to: str = 'Russian') -> str:
    if not lang_from:
        lang_from = 'auto'
    return f"{gtranslate.translate(text, source_language=lang_from, destination_language=lang_to)}"
