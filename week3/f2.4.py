from dictionary import movies
def avg_imdb(films):
    cnt = 0
    summ = 0
    for x in movies:
        if x["name"] in films:
            summ += x["imdb"]
            cnt += 1
    return summ/cnt
print(avg_imdb(['What is the name', 'Detective']))