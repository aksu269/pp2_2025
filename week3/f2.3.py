from dictionary import movies
def category(category_name):
    array = []
    for x in movies:
        if x["category"] == category_name:
            array.append(x["name"])
    return array
print(category("Suspense"))