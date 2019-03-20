# -*- coding: utf-8 -*-
from .rules import get_first_sentence
from .utils import unescape


def sum(paper):
    paper = unescape(paper)
    paragraphs = paper.splitlines()

    summary = ''
    for paragraph in paragraphs:
        summary += get_first_sentence(paragraph)

    return summary
