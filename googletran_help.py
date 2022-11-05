from translatepy.translators.google import GoogleTranslate

gtranslate = GoogleTranslate()


def gt_translate(text: str, lang_from: str = 'auto', lang_to: str = 'English') -> str:
    return gtranslate.translate(text, source_language=lang_from, destination_language=lang_to)
