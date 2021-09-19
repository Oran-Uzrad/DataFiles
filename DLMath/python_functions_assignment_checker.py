class functions_assignment_checker:

  def __init__(self , name):
    self.name = name

  def test_ex1(self , f):
    if f(3) == 9:
      print('\033[92m Test 1: Passed')
    else:
      print('\033[91m Test 1: Failed')
    if f(-4) == 16:
      print('\033[92m Test 2: Passed')
    else:
      print('\033[91m Test 2: Failed')

  def test_ex2(self , f):
    if f(3 , 3 , 3) == 3:
      print('\033[92m Test 1: Passed')
    else:
      print('\033[91m Test 1: Failed')
    if f(-4 , 5 , -9) == 5:
      print('\033[92m Test 2: Passed')
    else:
      print('\033[91m Test 2: Failed')

  def test_ex3(self , f):
    if f(3 , 3):
      print('\033[92m Test 1: Passed')
    else:
      print('\033[91m Test 1: Failed')
    if f(-4 , 5):
      print('\033[92m Test 2: Failed1')
    else:
      print('\033[91m Test 2: Passed1')

  def test_ex4(self , f):
    if f(0 , 0 , 0 , 0 , 0) == 0:
      print('\033[92m Test 1: Passed')
    else:
      print('\033[91m Test 1: Failed')
    if f(-4 , 5 , 2.4 , 10.1 , 12) == (-4+5+2.4+10.1+12)/5:
      print('\033[92m Test 2: Passed')
    else:
      print('\033[91m Test 2: Failed')