matrix = [ [ 2, 7, 6 ],
        [ 9, 5, 1 ],
        [ 4, 3, 8 ] ]
def isMagicSquare(matrix) :
  n = len(matrix)
  sumdiagonal1 = 0
  sumdiagonal2 = 0
  for i in range(n):
    sumdiagonal1 += matrix[i][i]  
    sumdiagonal2 += matrix[i][n-i-1]
  if (sumdiagonal1 != sumdiagonal2):
    return False
  for i in range(n):
    sumrow = 0
    sumcolumn = 0
    for j in range(n):
      sumrow += matrix[i][j]
      sumcolumn += matrix[j][i]
    if sumrow != sumcolumn != sumdiagonal1:
      return False
  return True

if isMagicSquare(matrix):
    print('It is a Magic Square')
else:
    print('Not a Magic Square')