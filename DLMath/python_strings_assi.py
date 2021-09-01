
class functions_assignment_checker:

  def __init__(self , name):
    self.name = name

  def test_ex1(self , f):
    if f("abra", "cadabra") == "abracadabra":
      print('\033[92m Test 1: Passed')
    else:
      print('\033[91m Test 1: Failed')

  def test_ex2(self , f):
    if f("abra", "cadabra") == False:
      print('\033[92m Test 1: Passed')
    else:
      print('\033[91m Test 1: Failed')
    if f("abra", "cada") == True:
      print('\033[92m Test 2: Passed')
    else:
      print('\033[91m Test 2: Failed')

  def test_ex3(self , f):
    if f("abra", "cadabra") == False:
      print('\033[92m Test 1: Passed')
    else:
      print('\033[91m Test 1: Failed')
    if f("abra", "abcde") == True:
      print('\033[92m Test 2: Passed')
    else:
      print('\033[91m Test 2: Failed')

  def test_ex4(self , f):
    if f("the good things in life are glee") == False:
      print('\033[92m Test 1: Passed')
    else:
      print('\033[91m Test 1: Failed')
    if f("the good things in life are free") == True:
      print('\033[92m Test 2: Passed')
    else:
      print('\033[91m Test 2: Failed')

  def test_ex5(self , f):
    if f("banana","a") == 3:
      print('\033[92m Test 1: Passed')
    else:
      print('\033[91m Test 1: Failed')
    if f("banana","d") == 0:
      print('\033[92m Test 2: Passed')
    else:
      print('\033[91m Test 2: Failed')   