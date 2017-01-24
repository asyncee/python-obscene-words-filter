from . import conf
from .words_filter import ObsceneWordsFilter


def get_default_filter():
    return ObsceneWordsFilter(conf.bad_words_re, conf.good_words_re)
