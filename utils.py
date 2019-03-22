import re


# To be used
def average_newlines_between_paragraphs(paper):
    raw_paragraphs = paper.splitlines()
    num_of_newlines = len(raw_paragraphs)
    num_of_paragraphs = len([
        paragraph for paragraph in raw_paragraphs if paragraph != ''
    ])
    print(num_of_newlines)
    print(num_of_paragraphs)

    return num_of_newlines / num_of_paragraphs


def make_paragraphs(paper):
    raw_paragraphs = paper.splitlines()
    paragraphs = [
        paragraph for paragraph in raw_paragraphs if paragraph != ''
    ]

    return paragraphs
