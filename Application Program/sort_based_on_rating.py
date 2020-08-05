#optimze search results using sorting methods

temp_dict = dict()
temp_list = list()
temp2_dict = dict()
sorted_ratings = dict()
return_list = list()
def rating_sort(list_of_match,rating_val_list):
    temp_dict = dict(zip(list_of_match, rating_val_list))
    for key in temp_dict.keys():
        if temp_dict[key] in range(5):
            temp2_dict [key] = temp_dict[key] 
        else:
            continue
    rdict = dict(map(reversed, temp2_dict.items()))
    for key in sorted(rdict.keys()):
        return_list.append(rdict[key])
    return return_list[::-1]