from dictionary import movies
def sublist():
    array = []
    for x in movies:
        if x["imdb"] > 5.5:
            array.append(x["name"])
    return array
print(sublist())