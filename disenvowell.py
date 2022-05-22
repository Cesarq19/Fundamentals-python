def disemvowel(string_):
    result = ""
    for caracter in string_:
        if not caracter.lower() in "aeiou":
            result += caracter
    return result