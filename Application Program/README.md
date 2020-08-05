COCINERO beta

Description...
A smart recipe suggestion application that takes in a list of ingredients from the user and 
returns a list of food dishes that can be prepared using these ingredients.

Instructions...
1.   Launch Cociner beta application.
2.   Choose to enter list of ingredients or select from a list of commonly used ingredients.
3.   Enter your input.
4.   Select one dish from a list of suggestions.
5.   Wait for the recipe ingredients and directions to prepare the dish.

Module Description...
1.   cocinero_beta - Takes input and calls algorithm module.
2.   user_input - Choose between entering ingredients or selecting them. Returns list of ingredients.
3.   algorithm - Performs ui tasks.Imports JSON dataset. Imports various modules listed below.
4.   run_search_1 - compares ingredients for each dish in dataset with user input. Returns list of indexes of matched dishes.
5.   remove_duplicate - Returns list of indexes of matched dishes, after deleting repeated entries.
6.   sort_based_on_rating - Returns list of indexes, after sorting matched dishes based on rating.
7.   in_title_search - Returns list of indexes of matched dishes, with higher priority given to dishes with ingredient name in their title.
8.   mod_list - contains functions to perform all the list manipulaions involved.


