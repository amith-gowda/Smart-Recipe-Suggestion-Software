import user_input as ui
import algorithm
#######################################################################
#import user_input module and accept inputs
#store user input in take_ing list

print('1...Enter the list of ingredients\n')
print('2...Feeling lazy? Choose from list of ingredients')
choice = int(input())
if choice is 1:
    user_in = ui.take_ingridients()
else:
    user_in = ui.choose_ingredients()

#######################################################################

algorithm.algo(user_in)


    
        
        
        
        
        
        
        
        
        