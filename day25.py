def index(list,item):
    l = 0
    r = len(list) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if list[mid] == item:
            print(f'The index of {item} in the list is: {mid}')
            quit()
        elif list[mid] < item:
            l = mid + 1
        else:
            r = mid - 1
    print(f'{item} is not in the list')

def sort(list,item):
    flag = False
    i = 1
    while i < len(list):
        if(list[i] < list[i - 1]):
            flag = True
        i += 1
    if flag:
        print ('The list entered is not sorted')
    else:
        index(list,item)

sort(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'], 'x')