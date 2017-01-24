# coding: utf-8
from __future__ import unicode_literals

import re

from .regexp import build_good_phrase, build_bad_phrase


bad_words = [
    build_bad_phrase('п еи з д'),
    build_bad_phrase('х у йёуяию'),
    build_bad_phrase('о х у е втл'),
    build_bad_phrase('п и д оеа р'),
    build_bad_phrase('п и д р'),
    build_bad_phrase('её б а нклт'),
    build_bad_phrase('у её б оа нтк'),
    build_bad_phrase('её б л аои'),
    build_bad_phrase('в ы её б'),
    build_bad_phrase('е б ё т'),
    build_bad_phrase('св ъь еёи б'),
    build_bad_phrase('б л я'),
    build_bad_phrase('г оа в н'),
    build_bad_phrase('м у д а кч'),
    build_bad_phrase('г ао н д о н'),
    build_bad_phrase('ч м оы'),
    build_bad_phrase('д е р ь м'),
    build_bad_phrase('ш л ю х'),
    build_bad_phrase('з ао л у п'),
    build_bad_phrase('м ао н д'),
    build_bad_phrase('с у ч а р'),
    build_bad_phrase('д ао л б ао её б'),
]
bad_words_re = re.compile('|'.join(bad_words), re.IGNORECASE | re.UNICODE)

good_words = [
    build_good_phrase('х л е б а л оа'),
    build_good_phrase('с к и п и д а р'),
    build_good_phrase('к о л е б а н и яей'),
    build_good_phrase('з ао к оа л е б а лт'),
    build_good_phrase('р у б л я'),
    build_good_phrase('с т е б е л ь'),
    build_good_phrase('с т р а х о в к ауи'),
    r'([о][с][к][о][Р][б][л][я]([т][ь])*([л])*([е][ш][ь])*)',
    r'([в][л][ю][б][л][я](([т][ь])([с][я])*)*(([е][ш][ь])([с][я])*)*)',
    r'((([п][о][д])*([з][а])*([п][е][р][е])*)*[с][т][р][а][х][у]([й])*([с][я])*([е][ш][ь])*([е][т])*)',
    r'([м][е][б][е][л][ь]([н][ы][й])*)',
    r'([Уу][Пп][Оо][Тт][Рр][Ее][Бб][Лл][Яя]([Тт][Ьь])*([Ее][Шш][Ьь])*([Яя])*([Лл])*)',
    r'([Ии][Сс][Тт][Рр][Ее][Бб][Лл][Яя]([Тт][Ьь])*([Ее][Шш][Ьь])*([Яя])*([Лл])*)',
    r'([Сс][Тт][Рр][Аа][Хх]([Аа])*)',
]
good_words_re = re.compile('|'.join(good_words), re.IGNORECASE | re.UNICODE)
