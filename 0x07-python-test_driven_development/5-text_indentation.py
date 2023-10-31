#!/usr/bin/python3
def text_indentation(text):
    """Prints text wiith indentation"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    copy = text[:]

    for delim in ".:?":
        copy_list = copy.split(delim)

        copy = ""
        for item in copy_list:
            item = item.strip(" ")
            copy = item + delim if copy is "" else copy + "\n\n" + item + delim
    print(copy[:-3], end="")

text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
        Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
        Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
        Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
        Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
        rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
        stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
        cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
        beatiorem! Iam ruinas videres""")
