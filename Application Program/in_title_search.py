#sort to give priority with dishes thathave the names of ingredients in it

title_match_index = list()
temp_dict = dict()
index_list = list()
def tilte_sort(index,titles,ingredients):
    for i in range(len(index)):
        titles[i] = titles[i].lower()
        temp_dict[index[i]] = titles[i]
    index_list = temp_dict.keys()
    for j in index_list:
        for traverse_ingredients in ingredients:
            if traverse_ingredients not in temp_dict[j]:
                break
            else:
                title_match_index.append(j)     
    return title_match_index