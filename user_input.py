#take in user input into a list of ingridients


def take_ingridients():
    user_ingredients=list()
    while(1):
        temp=input('Enter ingridient | enter done to submit list  :  ')
        if temp == 'done':
            break
        else:
            user_ingredients.append(temp.lower())
    return user_ingredients

def choose_ingredients():
    chosen_ingredients=list()
    print('\n Choose from the list of the most commonly used ingredients\n')
    common_ingredients = ['flour','sugar','chocolate','milk','rice','pasta','beans','bread','garlic','onion',
                          'tomato','potato','chicken','turkey','lamb','shrimp','fish','crab','lobster']
    for i in range(1,len(common_ingredients)) :
        print(str(i)+'...'+common_ingredients[i])
    print('Enter your choice | enter 0 to submit list : ')
    while(1):
        take_in = int(input())
        chosen_ingredients.append(common_ingredients[take_in-1])
        if take_in is 0:
            break
    return chosen_ingredients