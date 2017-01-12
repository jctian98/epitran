# -*- coding: utf-8 -*-

def ligaturize(text):
    """Convert text to employ non-standard ligatures."""
    mapping = [(u't͡s', u'ʦ'),
               (u't͡ʃ', u'ʧ'),
               (u't͡ɕ', u'ʨ'),
               (u'd͡z', u'ʣ'),
               (u'd͡ʒ', u'ʤ'),
               (u'd͡ʑ', u'ʥ'),]
    for from_, to_ in mapping:
        text = text.replace(from_, to_)
    return text
