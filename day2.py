def list_to_set(items):
  newset = set(items)
  mode = max(set(items), key = items.count)
  return('The set is: {} and the mode of the set is: {}'.format(newset,mode))
  
print(list_to_set(['a','b','a','a',3,3,2,'hello','b']))