import re


def get_first_sentence(paragraph):
    """
    Return the first sentence of a paragraph written in Japanese.
    If there is a quotation mark at the beginning of the paragraph,
    return the quotation part.
    """
    quotation_mark_re = re.compile(r'^[\"\'「].+?[\"\'」]')
    first_sentence_re = re.compile(r'^.+?。')

    quotation_mark_match = quotation_mark_re.match(paragraph)
    if quotation_mark_match:
        return quotation_mark_match.group()

    first_sentence_match = first_sentence_re.match(paragraph).group()
    if not first_sentence_match:
        return None

    return first_sentence_match.group()
