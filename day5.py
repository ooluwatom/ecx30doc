def fibonacci(n):
  second_last = 0
  last = 1
  for n in range(1,n+1):
    if n == 1:
      print(second_last)
    elif n == 2:
      print(last)
    else:
      new_last = second_last + last
      print(new_last)
      second_last = last
      last = new_last
  print('Term number {} of the Fibonacci = {}'.format(n,new_last))

fibonacci(10)