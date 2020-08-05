# list 1 folowed by all elements in list 2 except the ones repeated in list 1

return_list = list()
temp_dict = list()
def rearrange(list_1,list_2):
    return_list.extend(list_2)
    temp_dict = [x for x in list_1 if x not in list_2]
    return_list.extend(temp_dict)          
    return return_list


             