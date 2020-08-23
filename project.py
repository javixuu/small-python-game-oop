from gametasks import printInstructions, getUserScore, updateUserScore
from gameclass import Game, MathGame, BinaryGame

try:
  mathInstructions = '''\nIn this game, you will be given a simple arithmetic question.
  Each correct answer gives you one mark.
  No mark is deducted for wrong answer\n'''

  binaryInstructions = '''\nIn this game, you will be given a number in base 10.
  Your task is to convert this number to base 2.
  Each correct answer gives you one mark.
  No mark is deducted for wrong answers\n'''

  #Setting game and user
  bg = BinaryGame(4)
  mg = MathGame(4)

  userName = input('Please enter your name: ')
  curScore = getUserScore(userName)
  newUser = False if curScore != -1 else True

  if newUser == True:
    updateUserScore(newUser, userName)
    curScore = 0

  print('\nWelcome %s, your current score is %d' %(userName, curScore))

  #Main game while loop
  userChoice = 0
  while userChoice != '-1':

    #Select game
    game = input('\nMath Game (1) or Binary Game (2): ')
    while game != '1' and game != '2':
      game = input('\nEnter 1 or 2 please. Math Game (1) or Binary Game (2): ')

    while True:
      try:
        numPrompt = input ('\nHow many questions do you want per game (1 to 10): ')
        numPrompt = int(numPrompt)
        break
      except:
        numPrompt = input ('\nTry again, bad format. How many questions do you want per game (1 to 10): ')

    #Set the game choosen
    if game == '1':
      mg.noOfQuestions = numPrompt
      printInstructions(mathInstructions)
      curScore += mg.generateQuestions()

    elif game == '2':
      bg.noOfQuestions = numPrompt
      printInstructions(binaryInstructions)
      curScore += bg.generateQuestions()

    userChoice = input('\Enter any key to continue or -1 to exit: ')

  #Game finished
  updateUserScore(False, userName, curScore)

  print('Your total score playing is %d' %(getUserScore(userName)))

except:
  print('\nUnexpected error ocurred, restart the game please\n')
  print(error)
  exit()

    
    


