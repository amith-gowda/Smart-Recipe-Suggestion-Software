ddict = {1: 4.2,3: 1.5,2: 3.5}
return_list = list()
rdict = dict(map(reversed, ddict.items()))
for key in sorted(rdict.keys()):
    return_list.append(rdict[key])
print(return_list[::-1])

#optimze search results using sorting methods

temp_dict = dict()
temp_list = list()
sorted_ratings = dict()
return_list = list()
def rating_sort(list_of_match,rating_val_list):
    temp_dict = dict(zip(list_of_match, rating_val_list))
    rdict = dict(map(reversed, temp_dict.items()))
    for key in rdict.keys():
        if key in range(5):
            temp_list.append(rdict[key])
        else:
            continue
    for i in sorted(temp_list):
            return_list.append(rdict[key])
    return return_list[::-1]