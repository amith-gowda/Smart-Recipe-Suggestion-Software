#take list of ingridients required for one dish and run search 
#return true if there is a match, false otherwise
#recognize dish by index

dish_index = 0
matched_dish_index = list()
dish_ingredients = list()

def search_ingredient(ingredients_for_all_dishes,search_list):
    for traverse_ifad in ingredients_for_all_dishes:
        dish_ingredients.append(traverse_ifad)
    for i in range(len(dish_ingredients)):
        for traverse_di in dish_ingredients[i]:
            for j in range(len(search_list)):
                if search_list[j] not in traverse_di:
                    break
                else:
                    matched_dish_index.append(i)
    return matched_dish_index
        