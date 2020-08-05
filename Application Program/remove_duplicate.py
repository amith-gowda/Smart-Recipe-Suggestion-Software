##########remove duplicate entries
def del_dupliacte(in_dict):
    result = dict()
    for key,value in in_dict.items():
        if value not in result.values():
            result[key] = value
    return result.keys() 