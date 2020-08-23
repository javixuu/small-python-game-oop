class Game:
  def __init__(self, noOfQuestions = 0):
    self._noOfQuestions = noOfQuestions

  @property
  def noOfQuestions(self):
    return self._noOfQuestions
  
  @noOfQuestions.setter
  def noOfQuestions(self, value):
    if(value < 1):
      self._noOfQuestions = 1
      print("\nMinimum Number of Questions = 1")
    elif value > 10:
      self._noOfQuestions = 10
      print("\nMaximum Number of Questions = 10")
    else:
      self._noOfQuestions = value
      print("\nNumber of Questions = %d" %value)

class BinaryGame(Game):
  def generateQuestions(self):
    from random import randint
    score = 0
    for i in range(self.noOfQuestions):
      base10 = randint(1,100)
      print('\n->Question %d of %d. Binary of %d' %(i, self.noOfQuestions, base10))
      userResult = input('\tAnswer: ')
      while True:
        try:
          userResult = int(userResult, 2)
          if base10 == userResult:
            score +=10
            print('\nCorrect answer!')
          else:
            print("\nWrong answer. The correct answer is {:b}.".format(base10))
          break
        except:
          print('\nAn error ocurred, please type again your answer\n')
          userResult = input('\tAnswer: ')

    print('\nYour final score is %d' %score)
    return score

  
class MathGame(Game):
  def generateQuestions(self):
    from random import randint
    score = 0
    numberList = [0, 0, 0, 0, 0]
    symbolList = ['', '', '', '']
    operatorDict = {1: '+', 2: '-', 3: '*', 4: '**'}
    
    for i in range (self.noOfQuestions):
      print('\n-> Question %d / %d \n' %(i, self.noOfQuestions))
      for j in range (5):
        numberList[j] = randint(1, 9)

      for j in range(4):
        randOper = randint(1,4)
        if j>0:
          if symbolList[j-1] == '**' and randOper ==  4:
            randOper = randint (1,3)
        symbolList[j] = operatorDict[randOper]
    
      questionString = '('
      for j in range (5):
        questionString += str(numberList[j]) 
        if(j != 4):
          questionString += symbolList[j]

      questionString += ')'
      result = eval(questionString)
      questionString = questionString.replace("**", "^")
      print('\nResult for %s' %questionString)
      userResult = input('\n\tAnswer: ')
      
      while True:
        try:
          userResult = int(userResult)
          if (result == userResult):
            score += 10
            print('\nGood answer\n')
          else:
            print('\nWrong answer, the good anwer is %d \n' %result)
          break
        except:
          userResult = input('\nBad format, enter again your answer: ')
    
    print('\nYour final score for this game is %d' %score)
    return score

      

        

    