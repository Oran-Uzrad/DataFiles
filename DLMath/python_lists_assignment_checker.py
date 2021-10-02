import random
class lists_assignment_checker:

  def __init__(self , name):
    self.name = name

  def test_ex1(self , f):
    if f([3.4 , -8 , 0 , -1.3]) == 3.4:
      print('\033[92m Test 1: Passed')
    else:
      print('\033[91m Test 1: Failed')
    if f([]) == 0:
      print('\033[92m Test 2: Passed')
    else:
      print('\033[91m Test 2: Failed')

  def test_ex2(self , f):
    if f([3.4 , -8 , 0 , -1.3 , 2]) == [3.4 , 0 , 2]:
      print('\033[92m Test 1: Passed')
    else:
      print('\033[91m Test 1: Failed')
    if f([]) == []:
      print('\033[92m Test 2: Passed')
    else:
      print('\033[91m Test 2: Failed')

  def test_ex3(self , f):
    if f(['AAA' , 'CCB' , 'BBC' , 'BAA'] , ['CCC' , 'BBB']) == ['CCC', 'CCB', 'BBC', 'BBB', 'BAA', 'AAA']:
      print('\033[92m Test 1: Passed')
    else:
      print('\033[91m Test 1: Failed')

  def test_ex4(self , f):
    random.seed(3)
    x = f(100 , 100)
    y = self.average_of_random_numbers(100 , 100)
    if x == y:
      print('\033[92m Test 1: Passed')
    else:
      print('\033[91m Test 1: Failed')

  def average_of_random_numbers(self , n , m):
    random.seed(3)
    l = [] 
    for i in range(n):
      l.append(random.randint(0 , m))
    return sum(l) / len(l)
    