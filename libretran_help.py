from libretranslatepy import LibreTranslateAPI
from operator import itemgetter

LT_API = LibreTranslateAPI("https://translate.argosopentech.com/")


def _detect_lang(text: str) -> str:
    global LT_API
    langs = sorted(LT_API.detect(text),
                   key=itemgetter('language'),
                   reverse=True)
    return langs[0].get("language")


def lt_translate(text: str, lang_to: str = 'ru', lang_from: str = 'auto') -> str:
    global LT_API
    if lang_from == 'auto' or not lang_from:
        lang_from = _detect_lang(text)
    return LT_API.translate(text, lang_from, lang_to)
