# coding: utf-8
from __future__ import unicode_literals

import re
from functools import partial


alphabet_ru = {
    'а': 'а',
    'б': 'б6',
    'в': 'в',
    'г': 'г',
    'д': 'д',
    'е': 'е',
    'ё': 'ё',
    'ж': 'ж',
    'з': 'з',
    'и': 'и',
    'й': 'й',
    'к': 'к',
    'л': 'л',
    'м': 'м',
    'н': 'н',
    'о': 'о',
    'п': 'п',
    'р': 'р',
    'с': 'с',
    'т': 'т',
    'у': 'у',
    'ф': 'ф',
    'х': 'х',
    'ц': 'ц',
    'ч': 'ч',
    'ъ': 'ъ',
    'ы': 'ы',
    'ь': 'ь',
    'э': 'э',
    'ю': 'ю',
    'я': 'я',
}


def variants_of_letter(alphabet, letter):
    letters = alphabet.get(letter, letter)
    return '|'.join(letters.split())


ru_variants_of_letter = partial(variants_of_letter, alphabet_ru)


def build_bad_phrase(*symbols, **kwargs):
    """
    Построить регулярную фразу из символов.

    Между символами могут располагаться пробелы или любые не−кириллические символы.
    Фраза возвращается в виде группы.
    """
    variants_func = kwargs.get('variants_func', ru_variants_of_letter)
    separator = '(?:[^а-я])*'  # non-capturing group

    if len(symbols) == 1:
        symbols = symbols[0].split()

    symbol_regexp = []
    for symbol in symbols:
        if len(symbol) == 1:
            symbol = [symbol]

        parts = [variants_func(i) for i in symbol]
        symbol_regexp.append('[{}]+'.format('|'.join(parts)))

    return r'[а-я]*({})[а-я]*'.format(separator.join(symbol_regexp))


def build_good_phrase(*symbols):
    if len(symbols) == 1:
        symbols = symbols[0].split()

    out = []
    for symbol in symbols:
        out.append('[{}]'.format(symbol))
    return r'({})'.format(''.join(out))
