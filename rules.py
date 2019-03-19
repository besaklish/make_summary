import re

"""
「このなかで。区切られてしまう。」
こういうエスケープはしたくない。
"""
def get_first_sentence(string):
    first_sentence_re = re.compile(r'^.+?。')
    if not first_sentence_re.match(string):
        return None
    
    return first_sentence_re.match(string).group()
