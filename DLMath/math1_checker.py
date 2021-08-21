

class math1_checker:
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return self.name

  def test_m1(self , f):
    if f(3 , 4 , 1) == self.m1(3 , 4 , 1):
      print('\033[92m Test 1: Passed')
    else:
      print('\033[91m Test 1: Failed')

  def test_dm1_dx(self , f):
    if f(3 , 4 , 1) == self.dm1_dx(3 , 4, 1):
      print('\033[92m Test 1: Passed')
    else:
      print('\033[91m Test 1: Failed')

  def test_m2(self , f):
    if f(3 , 4 , -1 , 100) == self.m2(3 , 4, -1 , 100):
      print('\033[92m Test 1: Passed')
    else:
      print('\033[91m Test 1: Failed')

  def test_dm2_dx(self , f):
    if f(3 , 4 , -1 , 10) == self.dm2_dx(3 , 4, -1 , 10):
      print('\033[92m Test 1: Passed')
    else:
      print('\033[91m Test 1: Failed')

  def test_m3(self , f):
    if f([3 , 4 , -1] , 9) == self.m3([3 , 4, -1] , 9):
      print('\033[92m Test 1: Passed')
    else:
      print('\033[91m Test 1: Failed')

  def test_dm3_dx(self , f):
    if f([1 , 2 , 3] , 9) == self.dm3_dx([1 , 2 , 3] , 9):
      print('\033[92m Test 1: Passed')
    else:
      print('\033[91m Test 1: Failed')

  def test_ex7(self , F):
    if F[0](9) - F[1](-4) == self.dg(9) - self.dg_dd(-4):
      print('\033[92m Test 1: Passed')
    else:
      print('\033[91m Test 1: Failed')

  def test_ex8(self , f1 , f2):
    if f1(9) - f2(-4) == self.obvious(9) - self.dobvious_do(-4):
      print('\033[92m Test 1: Passed')
    else:
      print('\033[91m Test 1: Failed')

  def test_ex9(self , F):
    if F[0](9) - F[1](-4) + 2 * F[2](1) + F[3](0)**2 == self.u_ex_nine(9) - self.du_ex_nine_dx(-4) + 2 * self.v_ex_nine(1) + self.dv_ex_nine_dx(0)**2:
      print('\033[92m Test 1: Passed')
    else:
      print('\033[91m Test 1: Failed')

    if F[4](2.1) - 6*F[5](-4) == self.M1(2.1) - 6*self.dM1_dx(-4):
      print('\033[92m Test 2: Passed')
    else:
      print('\033[91m Test 2: Failed')

  def test_ex10(self , F):
    if F[0](9) - F[1](-4) + 2 * F[2](1) + F[3](0)**2 == self.u_ex_ten(9) - self.du_ex_ten_dx(-4) + 2 * self.M4(1) + self.dM4_dx(0)**2:
      print('\033[92m Test 1: Passed')
    else:
      print('\033[91m Test 1: Failed')

  def m1(self , a , b , x):
    return a * x + b

  def dm1_dx(self , a , b , x):
    return a

  def m2(self , a , b , c , x):
    return a*x**2 + b*x + c

  def dm2_dx(self , a , b , c , x):
    return 2*a*x + b

  def m3(self , W , x):
    l = len(W)
    if l == 0:
      return 0
    sum = 0
    for i in range(l):
      sum = sum + W[i] * x**i
    return sum

  def dm3_dx(self , W , x):
    l = len(W)
    if l == 0:
      return 0
    f = 0
    for i in range(1,l):
      f = f + i*W[i] * x**(i-1)
    return f

  def dg(self , d):
    return d**4 -3

  def dg_dd(self , d):
    return 4 * d**3

  def obvious(self , o):
    return 3*o**-1 + 3*o**1.5 + 3

  def dobvious_do(self , o):
    return -3*o**-2 + 4.5*o**0.5

  def u_ex_nine(self , x):
    return 4*x**5 + 3*x - 7

  def du_ex_nine_dx(self , x):
    return 20*x**4 + 3

  def v_ex_nine(self , x):
    return 3*x**2 + 2*x

  def dv_ex_nine_dx(self , x):
    return 6*x + 2

  def M1(self , x):
    return 5*u_ex_nine(x) + 3*v_ex_nine(x)

  def dM1_dx(self , x):
    return 5*du_ex_nine_dx(x) + 3*dv_ex_nine_dx(x)

  def u_ex_ten(self , x):
    return 3*x + 2

  def du_ex_ten_dx(self , x):
    return 3

  def M4(self , x):
    return 5*u_ex_ten(x)**2 - 6*u_ex_ten(x)

  def dM4_dx(self , x):
    return 10*u_ex_ten(x)*du_ex_ten_dx(x) -6*du_ex_ten_dx(x)

