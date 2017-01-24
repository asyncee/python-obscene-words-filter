# coding: utf-8

from __future__ import unicode_literals

import re
from functools import partial


class ObsceneWordsFilter(object):
    def __init__(self, bad_regexp, good_regexp):
        self.bad_regexp = bad_regexp
        self.good_regexp = good_regexp

    def find_bad_word_matches(self, text):
        return self.bad_regexp.finditer(text)

    def find_bad_word_matches_without_good_words(self, text):
        for match in self.find_bad_word_matches(text):
            if not self.is_word_good(match.group()):
                yield match

    def is_word_good(self, word):
        return bool(self.good_regexp.match(word))

    def is_word_bad(self, word):
        if self.is_word_good(word):
            return False

        return bool(self.bad_regexp.match(word))

    def mask_bad_words(self, text):
        for match in self.find_bad_word_matches_without_good_words(text):
            start, end = match.span()
            text = self.mask_text_range(text, start, end)
        return text

    @staticmethod
    def mask_text_range(text, start, stop, symbol='*'):
        return text[:start] + (symbol * (stop - start)) + text[stop:]
