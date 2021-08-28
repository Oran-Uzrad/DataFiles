from datetime import datetime
from pytz import timezone

class python_test_checker:

  def __init__(self , name):
    self.name = name
    self.log = open('/content/gdrive/MyDrive/Colab Notebooks/checkers/python_test_log.txt' , 'a')
    self.log.write('----- New seesion at ' + str(datetime.now(timezone('Europe/Berlin'))) + ' -----\n')

  def personal_details(self):
    self.log.write('Student:\n')
    self.log.write('\tName: ' + input('Name: ') + '\n')
    self.log.write('\tTeacher: ' + input('Teacher: ') + '\n')

  def submit(self):
    self.log.close()

  def q1_check(self):
    try:
      a = int(input("Enter answer number 1,2,3 or 4: "))
    except:
      raise ValueError(f"{a} not a legal answer")
    if a < 1 or a > 4:
      raise ValueError(f"{a} not a legal answer")
    if a == 2:
      self.log.write(f"q1 correct answer: {a}\n")
    else:
      self.log.write(f"q1 wrong answer: {a}\n")

  def q2_check(self , f):
    l = f()
    if l == [30, 33, 39, 42, 45, 51, 54, 57, 63, 66, 69, 75]:
      self.log.write(f"q2 correct answer: {str(l)}\n")
    else:
      self.log.write(f"q2 wrong answer: {str(l)}\n")