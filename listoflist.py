## Given an array of arrays, flatten into a single array

list_of_lists = [[1,2,3,4], [5,6],[7]]
flattened_list = []

#flatten the list

def mergelistoflist():
    for x in list_of_lists:
        for y in x:
            flattened_list.append(y)
    print(flattened_list)

mergelistoflist()