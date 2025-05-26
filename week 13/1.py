def check_all_students_passed(scores_input: str,names_input: str )-> str:
    scores = scores_input.split(',')
    names = names_input.split(',')

    a = False
    temp = []
    i = 0
    while i < len(scores):
        n = int(scores[i])
        if (n) < 35:
            temp += names[i]
            a = True
        i += 1
    if a:
        print('Есть не сдавшие')
        for x in temp:
            print(x)
    else:
        print('Все сдали')
            

scores_input = input()
names_input = input()
check_all_students_passed(scores_input, names_input)
