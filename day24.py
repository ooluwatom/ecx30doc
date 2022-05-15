def ascending(list):
    i = 0
    j = 1
    while j < len(list):
        if list[i] > list[j]:
            list.insert(j + 1, list [i])
            list.pop(i)
        i += 1
        j += 1
        
    flag = False
    i = 1
    while i < len(list):
        if(list[i] < list[i - 1]):
            flag = True
        i += 1
        if not flag:
            return list
        ascending(list)
    print (f'The new sorted list is: {list}')

def descending(list):
    i = 0
    j = 1
    while j < len(list):
        if list[i] < list[j]:
            list.insert(j + 1, list [i])
            list.pop(i)
        i += 1
        j += 1

    flag = False
    i = 1
    while (i + 1) < len(list):
        if(list[i + 1] > list[i]):
            flag = True
        i += 1
        if not flag:
            return list
        descending(list)
    print (f'The new sorted list is: {list}')

def sort_function(input, order):
    if order == 'ascending':
        ascending(input)
    elif order == 'descending':
        descending(input)

sort_function(['x','c','b','v','z','a'], 'ascending')