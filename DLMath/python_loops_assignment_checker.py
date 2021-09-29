import random
class functions_loops_checker:

  def __init__(self , name):
    self.name = name

  def test_ex2(self , f):
    if f(8) == 3:
      print('\033[92m Test 1: Passed')
    else:
      print('\033[91m Test 1: Failed')
    if f(9) == -1:
      print('\033[92m Test 2: Passed')
    else:
      print('\033[91m Test 2: Failed')

  def test_ex3(self , f):
    if f(8 , 3) == 8 - 3:
      print('\033[92m Test 1: Passed')
    else:
      print('\033[91m Test 1: Failed')
    if f(3 , 8) == 3 - 8:
      print('\033[92m Test 2: Passed')
    else:
      print('\033[91m Test 2: Failed')

  def test_ex4(self , f):
    if f(8) == 1:
      print('\033[92m Test 1: Passed')
    else:
      print('\033[91m Test 1: Failed')
    if f(888) == 3:
      print('\033[92m Test 2: Passed')
    else:
      print('\033[91m Test 2: Failed')
    if f(888999) == 6:
      print('\033[92m Test 3: Passed')
    else:
      print('\033[91m Test 3: Failed')

  def test_ex6(self , f):
    if f(8) == 40320:
      print('\033[92m Test 1: Passed')
    else:
      print('\033[91m Test 1: Failed')

  def test_ex7(self , f):
    random.seed(25)
    a = self.largest_of_hundred()
    random.seed(25)
    b = f()
    if a == b:
      print('\033[92m Test 1: Passed')
    else:
      print('\033[91m Test 1: Failed')

  def test_ex8(self , f):
    random.seed(25)
    a = self.index_of_largest_of_hundred()
    random.seed(25)
    b = f()
    if a == b:
      print('\033[92m Test 1: Passed')
    else:
      print('\033[91m Test 1: Failed')


  def largest_of_hundred(self):
    max = -1
    for i in range(100):
      n = random.randint(0,101)
      if n > max:
        max = n
    return max

  def index_of_largest_of_hundred(self):
    max = -1
    indx = -1
    for i in range(100):
      n = random.randint(0,101)
      if n > max:
        max = n
        indx = i
    return indx

  