#take in user input into a list of ingridients

def take_ingridients():
    user_ingridients=list()
    while(1):
        temp=input('Enter ingridient | enter done to submit list  :  ')
        if temp == 'done':
            break
        else:
            user_ingridients.append(temp)
    return user_ingridients