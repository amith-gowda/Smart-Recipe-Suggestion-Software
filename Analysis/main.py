import json


ingredient_list = list()
count = 0

#user input here


#opening json file
with open('data/rec.json') as json_file:  
    dataset = json.load(json_file)
    for i in dataset:
        try:
            ingredient_list.append(i['ingredients'])
            count += 1
        except KeyError:
            ingredient_list.append(['!!!!!dat_corrupt!!!!!'])
            count += 1
            continue
    
    print(dataset[0])