import run_search_1 as rs
import sort_based_on_rating as sort_r
import in_title_search as its
import mod_list as ml
import remove_duplicate as rd
import json

def algo(take_ing):
    list_of_all_ingredients = list()
    list_of_all_titles = list()
    list_of_all_directions = list()
    list_of_all_ratings = list()
    list_of_all_categories = list()
    with open("recipes.json", "r") as dataset:
        data = json.load(dataset)
        for field_ingredient in data:
            try:
                list_of_all_ingredients.append((field_ingredient['ingredients']))
            except:
                pass
        for field_title in data:
            try:
                list_of_all_titles.append((field_title['title']))
            except:
                pass
        for field_direction in data:
            try:
                list_of_all_directions.append((field_title['directions']))
            except:
                pass
        for field_rating in data:
            try:
                list_of_all_ratings.append((field_rating['rating']))
            except:
                pass
        for field_category in data:
            try:
                list_of_all_categories.append((field_category['rating']))
            except:
                pass
            
    #######################################################################
    #import run_seacrh module and pass data to the search function 
    #get a list of all matched dishes's index values in match_dish_list
    
    match_dish_list = list()
    match_ratings = list()
    match_titles = list()
    refined_match_index = list()
    match_dish_list = rs.search_ingredient(list_of_all_ingredients,take_ing)
    if len(match_dish_list) == 0:
        print('No results found')
        exit
    else:
        print('\nMatched results : \n')
        for i in match_dish_list:
            match_ratings.append(list_of_all_ratings[i])
        refined_match_index = sort_r.rating_sort(match_dish_list,match_ratings)
        for traverse_rmi in refined_match_index:
            match_titles.append(list_of_all_titles[traverse_rmi])
            
    #######################################################################
    #import in_title_search module and pass refined search index with titles
    #and user input return list of index 
        
        match_title_index = list()
        match_title_index = its.tilte_sort(refined_match_index,match_titles,take_ing)  
        
    #######################################################################
    #import mod_list and get a refined_2 index list 
        
        refined_match_index_2 = list()
        titles = list()
        refined_match_index_2 = ml.rearrange(match_dish_list,match_title_index)
        for j in refined_match_index_2:
            titles.append(list_of_all_titles[j])
        
    ########################################################################
    #get rid of duplicates entries
        pass_dict = dict(zip(refined_match_index_2, titles))
        refined_match_index_3 = list()
        refined_match_index_3 = rd.del_dupliacte(pass_dict)      
     
    ########################################################################
    #display and choice
    
        print('\nChoose one of the dishes : \n')
        count = 0
        for j in refined_match_index_3:
            count+=1        
            print(str(count)+'...'+list_of_all_titles[j]+'\n')
        choice = int(input('Enter your choice : '))
        print('\nTo cook ' + list_of_all_titles[refined_match_index_2[(choice-1)]])
        print('\nYou will need\n')
        print(list_of_all_ingredients[refined_match_index_2[(choice-1)]])
        print('\nDirections\n')
        print(list_of_all_directions[refined_match_index_2[(choice-1)]])
        end_in = input()