from dictionary import movies
def rate(movie):
    for x in movies:
        if x["name"] == movie:
            return x["imdb"] > 5.5
    return false
print(rate('Exam'))