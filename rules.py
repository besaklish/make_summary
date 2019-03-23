import re


def get_first_sentence(paragraph):
    """
    Return the first sentence of a paragraph written in Japanese.
    If there is a quotation mark at the beginning of the paragraph,
    return the quotation part.
    """
    inline_quotation_mark_re = re.compile(r'^.*?[\"\'「].+?[\"\'」].*?[.。]')
    quotation_mark_re = re.compile(r'^[\"\'「].+?[\"\'」]')
    first_sentence_re = re.compile(r'^.+?[\.。]')

    inline_quotation_mark_match = inline_quotation_mark_re.match(paragraph)
    if inline_quotation_mark_match:
        return inline_quotation_mark_match.group()

    quotation_mark_match = quotation_mark_re.match(paragraph)
    if quotation_mark_match:
        return quotation_mark_match.group()

    first_sentence_match = first_sentence_re.match(paragraph)
    if not first_sentence_match:
        return paragraph

    return first_sentence_match.group()


def get_sentences(paragraph):
    """
    Return a list of sentences from a paragraph
    """
    sentences = []
    while True:
        sentence = get_first_sentence(paragraph)
        if sentence == '':
            break
        else:
            sentences.append(sentence)

        # make paragraph smalller
        paragraph = paragraph.replace(sentence, '', 1)

    return sentences


def reduce_sentences(sentences, reduce_words):
    """
    if a reduce_word is included in a sentence,
    the sentence will be removed from sentences
    """
    reduce_regexes = [re.compile(word) for word in reduce_words]
    for regex in reduce_regexes:
        for sentence in sentences:
            if regex.search(sentence):
                sentences.remove(sentence)
                break

    return sentences


def get_important_sentences(sentences, important_words):
    """
    Return sentences which includes important_word
    """
    important_regexes = [re.compile(word) for word in important_words]
    
    important_sentences = []
    for regex in important_regexes:
        for sentence in sentences:
            if regex.search(sentence):
                important_sentences.append(sentence)
                sentences.remove(sentence)
                break
    
    return important_sentences
