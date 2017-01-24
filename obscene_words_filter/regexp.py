# coding: utf-8
from __future__ import unicode_literals

import re
from functools import partial


alphabet_ru = {
    'а': 'а4a',
    'б': 'б6b',
    'в': 'вvw',
    'г': 'гgr',
    'д': 'дgd',
    'е': 'е3e',
    'ё': 'ё3e',
    'ж': 'жjgzh zh ghz',
    'з': 'з3z ts',
    'и': 'иiy',
    'й': 'йiy',
    'к': 'кk',
    'л': 'лl',
    'м': 'мm',
    'н': 'нh',
    'о': 'оo',
    'п': 'пnp',
    'р': 'рpr',
    'с': 'сsc z',
    'т': 'тtm',
    'у': 'уyu yu',
    'ф': 'фf',
    'х': 'хxh kh',
    'ц': 'цc ts z',
    'ч': 'чch ch tsch',
    'ъ': 'ъ\'\"',
    'ы': 'ыyu',
    'ь': 'ь\'\"b',
    'э': 'эe3',
    'ю': 'юyu yu',
    'я': 'яya ya',
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
