import sys

class board:
  def __init__(self):
    self.omokBoardSpaces = []
    self.turncount = 0
    self.gameStatus = False


  def createboard(self):
    for y in range(0, 15):
      for x in range(0, 15):
        currentboardnumber = x + y * 15
        self.omokBoardSpaces.append(currentboardnumber)
        if currentboardnumber < 10:
          currentboardnumber =  str(currentboardnumber) + "  "
        elif currentboardnumber < 100:
          currentboardnumber =  str(currentboardnumber) + " "
        else:
          currentboardnumber = str(currentboardnumber)
        sys.stdout.write(str(currentboardnumber) + "|"),
      print ("")

  def placementX(self):
    while(1):
      place = input("Where would you like to place your omok piece Player One?")
      if place.isdigit() == False:
        print("Sorry! That location is unavailable!")
        continue
      val = int(place)
      if val > 224 or val < 0:
        print("Sorry! That location is unavailable!")
        continue
      self.omokBoardSpaces[val] = "X"
      self.turncount = self.turncount + 1
      break

  def placementO(self):
    while(1):
      place = input("Where would you like to place your omok Player Two?")
      if place.isdigit() == False:
        print("Sorry! That location is unavailable!")
        continue
      val = int(place)
      if val > 224 or val < 0:
        print("Sorry! That location is unavailable!")
        continue
      self.omokBoardSpaces[val] = "O"
      self.turncount = self.turncount + 1
      break


  def printBoard(self):
    counter = 0
    for y in range(0, 225):
        if (self.omokBoardSpaces[y] == "X") or (self.omokBoardSpaces[y] == "O") or (int(self.omokBoardSpaces[y]) < 10):
          print(str(self.omokBoardSpaces[y]) + "  "),
          sys.stdout.write("|"),
        elif int(self.omokBoardSpaces[y]) < 100 and int(self.omokBoardSpaces[y]) >= 10:
          print(str(self.omokBoardSpaces[y]) + " "),
          sys.stdout.write("|"),
        elif int(self.omokBoardSpaces[y]) >= 100:
          print(str(self.omokBoardSpaces[y])),
          sys.stdout.write("|"),
        counter += 1
        if counter > 14:
          print("")
          counter = 0

  def checktie(self):
    if self.turncount == 224:
      self.game = True
    else:
      self.game = False

  #Malcolm Win Combo Check SHOUTOUT MALCOLM
  def VerticalWinCheck(self):
    #vertical checks
    for i in range(0, 15):
      if self.omokBoardSpaces[i] == self.omokBoardSpaces[i+15]:
        if self.omokBoardSpaces[i+15] == self.omokBoardSpaces[i+30]:
          if self.omokBoardSpaces[i+30] == self.omokBoardSpaces[i+45]:
            if self.omokBoardSpaces[i+45] == self.omokBoardSpaces[i+60]:
              self.game = True
    for i in range(75, 90):
      if self.omokBoardSpaces[i] == self.omokBoardSpaces[i+15]:
        if self.omokBoardSpaces[i+15] == self.omokBoardSpaces[i+30]:
          if self.omokBoardSpaces[i+30] == self.omokBoardSpaces[i+45]:
            if self.omokBoardSpaces[i+45] == self.omokBoardSpaces[i+60]:
              self.game = True
    for i in range(150, 165):
      if self.omokBoardSpaces[i] == self.omokBoardSpaces[i+15]:
        if self.omokBoardSpaces[i+15] == self.omokBoardSpaces[i+30]:
          if self.omokBoardSpaces[i+30] == self.omokBoardSpaces[i+45]:
            if self.omokBoardSpaces[i+45] == self.omokBoardSpaces[i+60]:
                self.game = True

  def HorizontalWinCheck(self):
    for i in range(0, 211, 15):
      if self.omokBoardSpaces[i] == self.omokBoardSpaces[i+1]:
        if self.omokBoardSpaces[i+1] == self.omokBoardSpaces[i+2]:
          if self.omokBoardSpaces[i+2] == self.omokBoardSpaces[i+3]:
            if self.omokBoardSpaces[i+3] == self.omokBoardSpaces[i+4]:
                self.game = True
    for i in range(5, 216, 15):
      if self.omokBoardSpaces[i] == self.omokBoardSpaces[i+1]:
        if self.omokBoardSpaces[i+1] == self.omokBoardSpaces[i+2]:
          if self.omokBoardSpaces[i+2] == self.omokBoardSpaces[i+3]:
            if self.omokBoardSpaces[i+3] == self.omokBoardSpaces[i+4]:
              self.game = True
    for i in range(10, 221, 15):
      if self.omokBoardSpaces[i] == self.omokBoardSpaces[i+1]:
        if self.omokBoardSpaces[i+1] == self.omokBoardSpaces[i+2]:
          if self.omokBoardSpaces[i+2] == self.omokBoardSpaces[i+3]:
            if self.omokBoardSpaces[i+3] == self.omokBoardSpaces[i+4]:
              self.game = True

  def DiagonalL2R(self):
    for i in range(0, 151, 15):
      if self.omokBoardSpaces[i] == self.omokBoardSpaces[i+16]:
        if self.omokBoardSpaces[i+16] == self.omokBoardSpaces[i+32]:
          if self.omokBoardSpaces[i+32] == self.omokBoardSpaces[i+48]:
            if self.omokBoardSpaces[i+48] == self.omokBoardSpaces[i+64]:
                self.game = True
    for i in range(5, 157, 15):
      if self.omokBoardSpaces[i] == self.omokBoardSpaces[i+16]:
        if self.omokBoardSpaces[i+16] == self.omokBoardSpaces[i+32]:
          if self.omokBoardSpaces[i+32] == self.omokBoardSpaces[i+48]:
            if self.omokBoardSpaces[i+48] == self.omokBoardSpaces[i+64]:
              self.game = True
    for i in range(10, 162, 15):
      if self.omokBoardSpaces[i] == self.omokBoardSpaces[i+16]:
        if self.omokBoardSpaces[i+16] == self.omokBoardSpaces[i+32]:
          if self.omokBoardSpaces[i+32] == self.omokBoardSpaces[i+48]:
            if self.omokBoardSpaces[i+48] == self.omokBoardSpaces[i+64]:
              self.game = True

  def Diagonal2(self):
    for i in range(14, 165, 15):
      if self.omokBoardSpaces[i] == self.omokBoardSpaces[i+14]:
        if self.omokBoardSpaces[i+14] == self.omokBoardSpaces[i+28]:
          if self.omokBoardSpaces[i+28] == self.omokBoardSpaces[i+42]:
            if self.omokBoardSpaces[i+42] == self.omokBoardSpaces[i+56]:
                self.game = True
    for i in range(9, 160, 15):
      if self.omokBoardSpaces[i] == self.omokBoardSpaces[i+14]:
        if self.omokBoardSpaces[i+14] == self.omokBoardSpaces[i+28]:
          if self.omokBoardSpaces[i+28] == self.omokBoardSpaces[i+42]:
            if self.omokBoardSpaces[i+42] == self.omokBoardSpaces[i+56]:
              self.game = True
    for i in range(4, 155, 15):
      if self.omokBoardSpaces[i] == self.omokBoardSpaces[i+14]:
        if self.omokBoardSpaces[i+14] == self.omokBoardSpaces[i+28]:
          if self.omokBoardSpaces[i+28] == self.omokBoardSpaces[i+42]:
            if self.omokBoardSpaces[i+42] == self.omokBoardSpaces[i+56]:
              self.game = True


  def checkwin(self):
    self.VerticalWinCheck()
    if self.gameStatus == True:
      return
    self.HorizontalWinCheck()
    if self.gameStatus == True:
      return
    self.DiagonalL2R()
    if self.gameStatus == True:
      return
    self.Diagonal2()
    if self.gameStatus == True:
      return
    self.checktie()
    if self.gameStatus == True:
      return

board = board()
board.createboard()
gamestat = False
while(True):
  board.placementX()
  board.printBoard()
  board.checkwin()
  if board.gameStatus == True and board.turncount == 224:
    print("Tie!")
    break
  elif board.gameStatus == True:
    print("player one wins!")
    break
  board.placementO()
  board.printBoard()
  board.checkwin()
  if board.gameStatus == True and board.turncount == 224:
    print("Tie!")
    break
  elif board.gameStatus == True:
    print("player two wins!")
    break


