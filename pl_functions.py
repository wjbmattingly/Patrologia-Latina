import re
from string import digits

#Feed a string of an entire PL text and this function will output a tuple of a cleaned text (no punctuation) and a lowercased (everything lowercased). The result is data cleaned and prepped for machine learning.
def clean_pl_ml(text):
    cleaned = re.sub(r"[\(\[].*?[\)\]]", "", text).replace(" ,", ",").replace(" .", ".").replace(" .", ".").replace("\n\n", "\n").replace("\n\n", "\n").replace("\n\n", "\n").replace("  ", " ").replace("  ", " ").replace("\n ", "\n").replace(" ;", ";").replace(" :", ":").replace(" ?", "?").replace("?  ", "? ").replace(" ,", ",").replace("J", "I").replace("j", "i")
    remove_digits = str.maketrans('', '', digits)
    cleaned = cleaned.translate(remove_digits)
    l_data = cleaned.lower()
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    lp_data = ""
    for char in l_data:
        if char not in punctuations:
            lp_data = lp_data+char
    lowercase_data = lp_data.replace("\n", " ")
    new_f.write(lowercase_data)
    return (cleaned, lowercase_data)
