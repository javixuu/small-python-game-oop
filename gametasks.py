from os import remove, rename
import os

def printInstructions(instruction):
  print(instruction)

def getUserScore(userName):
  auxPath = os.path.abspath(os.getcwd())
  auxPath = auxPath + '\\userScores.txt'
  try:
    f = open(auxPath, 'r')
    for line in f:
      line = line.rstrip()
      auxList = line.split(',')
      if(auxList[0]==userName):
        f.close()
        return int(auxList[1])
    f.close()
    print('User not found')
    return -1
  except:
    print('file not found')
    exit()

def updateUserScore(newUser, userName, score=0):
  auxPath = os.path.abspath(os.getcwd())
  auxPath = auxPath + '\\userScores.txt'
  #user does not exist, create new entry
  if newUser:
    #check if user already exists
    if(getUserScore(userName) != -1):
      print('user already exists')
      return
    f = open(auxPath, 'a')
    newLine = '\n%s, %d' %(userName, score)
    f.write(newLine)
    f.close()
    print('New user added to database')
  #user exists, replace score
  else:
    if getUserScore(userName) == -1: 
      print('User does not exist' )
      return
    else:
      f = open(auxPath, 'r')
      auxList=[]
      for line in f:
        line = line.split(',')
        auxList.append(line)
      f.close()
      f = open(auxPath, 'w')

      #fase reescribir score
      auxListWrite = []

      for line in auxList:
          if line[0] == userName:
            line = [userName, ' %d\n' %score]
          auxListWrite.append(line)
          # print(auxListWrite)
      [f.write( '%s,%s' %(elem[0], elem[1])) for elem in auxListWrite] #python list comprehension
      f.close()
      # f.write(str(auxList))
      # for itema, itemb in zip(lista,listb)
      # func(nombre,edad,nacimiento)
      # dictentradas=
      # func(*dictentradas)
    
