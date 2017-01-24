Python obscene words filter.

---------------

|python| |pypi| |license|

---------------


This is ultra simple words filter, based on regular expressions.
It is built on regular expressions, with Russian language support from the box.

It may work with your language too (if you will write your own regular
expressions).

Before using in production, you should test it, because there are
no swear words filter in the world that does well filtering,
so the quality is not 100%.

But test coverage is :)


Quickstart
----------

Sample code::

    from obscene_word_filter.default import get_default_filter

    f = get_default_filter()

Or::

    from obscene_word_filter import conf
    from obscene_word_filter.words_filter import ObsceneWordsFilter

    f = ObsceneWordsFilter(conf.bad_words_re, conf.good_words_re)

Then you can mask use input::

    f.mask_bad_words("Тут должны быть матерные слова.")
    >>> Тут должны быть ******** *****.


Documentation
-------------
Just read the tests :)


.. |pypi| image:: https://img.shields.io/pypi/v/python-obscene-words-filter.svg?style=flat-square
    :target: https://pypi.python.org/pypi/python-obscene-words-filter
    :alt: pypi

.. |license| image:: https://img.shields.io/github/license/asyncee/python-obscene-words-filter.svg?style=flat-square
    :target: https://github.com/asyncee/python-obscene-words-filter/blob/master/LICENSE.txt
    :alt: MIT License

.. |python| image:: https://img.shields.io/badge/python-2.7-green.svg?style=flat-square
    :target: https://pypi.python.org/pypi/python-obscene-words-filter
    :alt: Python 2.7
