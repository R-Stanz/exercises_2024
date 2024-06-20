def verifica_senha(string):
    chars_and_digits = [0, 0]
    for c in string:
        if ((ord(c) >= ord('0')) and (ord(c) <= ord('9'))):
            chars_and_digits[1] += 1
        elif ((ord(c) >= ord('a')) and (ord(c) <= ord('z'))):
            pass
        elif ((ord(c) >= ord('A')) and (ord(c) <= ord('Z'))):
            pass
        else:
            chars_and_digits[0] += 1

    return chars_and_digits
