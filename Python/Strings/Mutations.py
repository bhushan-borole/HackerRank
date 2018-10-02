def mutate_string(string, pos, character):
    l = list(string)
    l[pos] = character
    return ''.join(l)