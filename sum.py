# -*- coding: utf-8 -*-
import argparse
from rules import get_first_sentence
from utils import unescape

parser = argparse.ArgumentParser(
    description='Make a summary from string'
)

parser.add_argument(
    'paper',
    help='a chunk of strings to be summarized'
)

args = parser.parse_args()


def sum(paper):
    paper = unescape(paper)
    paragraphs = paper.splitlines()

    summary = ''
    for paragraph in paragraphs:
        summary += get_first_sentence(paragraph)

    return summary

print(sum(args.paper))
