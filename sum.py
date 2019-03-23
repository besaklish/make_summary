# -*- coding: utf-8 -*-
from html import unescape
import json
import os

from .rules import get_first_sentence, reduce_sentences
from .utils import make_paragraphs


def sum(paper):
    paper = unescape(paper)
    paragraphs = make_paragraphs(paper)

    print(__file__)
    word_dict = {}
    with open(os.path.join(os.path.dirname(__file__), 'words.json')) as f:
        word_dict = json.load(f)

    sentences_summary = []
    # Summarizing
    for paragraph in paragraphs:
        sentence = ''
        sentence += get_first_sentence(paragraph)
        sentences_summary.append(sentence)

    # Remove irrelevant sentences
    sentences_summary = reduce_sentences(
        sentences_summary,
        word_dict['reduce_words']
        )

    # Concatenating paragraphs
    summary = ''
    for sentence in sentences_summary:
        summary += sentence + '\n\n'

    return summary
