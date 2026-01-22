import json
import os

BASE_DIR = os.path.dirname(__file__)

SUPPORTED_LANGS = ["en", "ru", "fi"]
DEFAULT_LANG = "en"

_texts_cache = {}


def load_language(lang: str):
    if lang not in SUPPORTED_LANGS:
        lang = DEFAULT_LANG

    if lang not in _texts_cache:
        path = os.path.join(BASE_DIR, f"{lang}.json")
        with open(path, "r", encoding="utf-8") as f:
            _texts_cache[lang] = json.load(f)

    return _texts_cache[lang]


def get_text(key: str, lang: str = DEFAULT_LANG, **kwargs) -> str:
    texts = load_language(lang)
    text = texts.get(key, f"❓ Missing text: {key}")

    if kwargs:
        try:
            text = text.format(**kwargs)
        except KeyError:
            pass

    return text
