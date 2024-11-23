from string import ascii_letters, digits
from random import choices, shuffle



punc = r"!#$&()*+,.-/:;<=>?@[]^_{|}~"
printable = ascii_letters + digits + punc

def password_generator(length=8, number_allow=True, punctuation=True):
    global printable, punc

    if length < 8:
        return f"WARNING(Out Of Range): The Password Must Contain At Least 8 Characters!"
    else:
        if not number_allow and punctuation:
            printable = ascii_letters + punc
            password = choices(printable, k=length)

        elif number_allow and not punctuation:
            printable = ascii_letters + digits
            password = choices(printable, k=length)

        elif not number_allow and not punctuation:
            password = choices(ascii_letters, k=length)
        
        else:
            password = choices(printable, k=length)
        
        shuffle(password)
        return "".join(password)
