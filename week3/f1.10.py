def unique(a):
    new_a = []
    for x in a:
        if x not in new_a:
            new_a.append(x)
    return new_a