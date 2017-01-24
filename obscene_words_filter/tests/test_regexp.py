# coding: utf-8
from __future__ import unicode_literals

import re

import pytest

from .. import regexp as p


def test_variants_of_letter():
    alpha = {
        'ф': 'фF ts',
        'г': 'гg',
    }
    assert p.variants_of_letter(alpha, 'ф') == 'фF|ts'
    assert p.variants_of_letter(alpha, 'г') == 'гg'


def test_build_bad_phrase_from_tuple():
    cases = {
        ('п', 'еи', 'з',
         'д'): r'[а-я]*([п]+(?:[^а-я])*[е|и]+(?:[^а-я])*[з]+(?:[^а-я])*[д]+)[а-я]*',
    }
    for k, v in cases.items():
        assert p.build_bad_phrase(*k) == v


def test_build_bad_phrase_from_string():
    cases = {
        'п еи з д': r'[а-я]*([п]+(?:[^а-я])*[е|и]+(?:[^а-я])*[з]+(?:[^а-я])*[д]+)[а-я]*',
    }
    for k, v in cases.items():
        assert p.build_bad_phrase(k) == v


def test_build_good_phrase_from_tuple():
    cases = {
        ('х', 'л', 'е', 'б', 'а', 'л', 'оа'): '([х][л][е][б][а][л][оа])',
        ('с', 'к', 'и', 'п', 'и', 'д', 'а', 'р'): '([с][к][и][п][и][д][а][р])',
    }
    for k, v in cases.items():
        assert p.build_good_phrase(*k) == v


def test_build_good_phrase_from_string():
    cases = {
        'х л е б а л оа': '([х][л][е][б][а][л][оа])',
        'с к и п и д а р': '([с][к][и][п][и][д][а][р])',
    }
    for k, v in cases.items():
        assert p.build_good_phrase(k) == v
