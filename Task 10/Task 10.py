def parse_subj(text):
    if len(text) > 3:
        for i in range(len(text)-1):
            if (text[i].isalpha() and text[i+1].isdigit() and text[i+2].isdigit()) or (text[i].isalpha() and text[i+1].isdigit()):
                return True
        if text[0].isalpha() and text[1].isdigit() and text[2].isdigit:
            return True
        if text[0].isalpha() and (text[1] == ' ' or text[1] == '-') and text[2].isdigit():
            return True
        return False
    elif len(text) == 2:
        if text[0].isalpha() and text[1].isdigit():
            return True
    else:
        return False

print(parse_subj('и1'))
