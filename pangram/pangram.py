def is_pangram(sentence):
    if sentence == "":
        return False
    else:
        for x in range(97, 123):
            if chr(x) not in sentence.lower():
                return False
        return True
