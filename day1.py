print('This program converts a List to a Set by checking if any of the objects provided earlier occured.')
user_input = list(map(str, input("Input the members of the list: ").split()))
new_list = []
for item in user_input:
    if item in new_list:
        continue
    new_list.append(item)
print(new_list)