#!/usr/bin/python3
"""prints a text with 2 new lines after
    each of these characters: ., ? and :"""


def text_indentation(text):
    """
    prints a text with 2 new lines after
    each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    my_text = []
    line = text.split('\n')
    for i in line:
        text_line = []
        for char in i:
            text_line.append(char)
            if char in ('.', '?', ':'):
                text_line.append("\n\n")
        my_text.append("".join(text_line))

    f_text = "".join(my_text)
    print(f_text, end="")
