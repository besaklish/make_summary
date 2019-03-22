# -*- coding: utf-8 -*-
from .rules import get_first_sentence, reduce_sentences
from html import unescape


def sum(paper):
    paper = unescape(paper)
    paragraphs = [
        paragraph for paragraph in paper.splitlines() if paragraph != ''
    ]

    sentences_summary = []
    # Summarizing
    for paragraph in paragraphs:
        sentence = ''
        sentence += get_first_sentence(paragraph)
        sentences_summary.append(sentence)

    # Remove irrelevant sentences
    sentences_summary = reduce_sentences(
        sentences_summary,
        ['例えば']
        )

    # Concatenating paragraphs
    summary = ''
    for sentence in sentences_summary:
        summary += sentence + '\n'

    return summary
