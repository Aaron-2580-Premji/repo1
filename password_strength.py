
special_chars = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '=', '+', '{', '}', '[', ']', '|', '\\',
    ':', ';', '"', "'", '<', '>', ',', '.', '?', '/',
    '`', '~'
]


def p_strength(password):
    upper=False
    lower=False
    has_digits=False
    spec_char=False
    for i in password:
        if i.isupper():
            upper=True
        elif i.islower():
            lower=True
        elif i.isdigit():
            has_digits=True
        elif i in special_chars:
            spec_char=True
        else:
            return False
    if upper and lower and has_digits and spec_char:
        return True


password = str(input("Enter the input: "))
if p_strength(password):
    print("Passsword is strong")
else:
    print("Password weak")