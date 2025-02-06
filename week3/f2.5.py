from dictionary import movies
def avg_imdb(category):
    cnt = 0
    summ = 0
    for x in movies:
        if x["category"] == category:
            summ += x["imdb"]
            cnt += 1
    return summ/cnt
print(avg_imdb("Suspense"))