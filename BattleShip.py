from os import system, name
from copy import deepcopy
Ships={"Carrier":5, "Battleship":4, "Cruiser":3, "Submarine":3, "Destroyer":2}
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
class Player:
    def __init__(self,number,name):
        self.playerGrid=Grid()
        self.number=number
        self.name=name
        self.winner=False
class Grid:    
    def __init__(self):
        self.grid=[["[  ]", "[A]","[B]","[C]","[D]","[E]","[F]","[G]","[H]","[I]","[J]"]]
        for i in range(1,11):
            if i<10:
                row=["["+str(i)+" ]"]
            else:
                row=["["+str(i)+"]"]
            for x in range(0,10):
                row.append( "[o]" )
            self.grid.append(row)
        self.timesHit=0
        self.shipsCovering=0
        self.shipsCovering=17
    def printGrid(self):
        for i in self.grid:
            print " ".join(i)
    def addShip(self,spot,direction,ship):      
        if (direction.upper()=="R"):
            if (self.grid[0].index("["+str(spot[0]).upper()+"]")+Ships[ship]<10):
                for i in range(0,Ships[ship]):
                    self.grid[int(spot[1:])][self.grid[0].index("["+str(spot[0]).upper()+"]")+i]="[+]"
            else:
                for i in range(0,Ships[ship]):
                    self.grid[int(spot[1:])][11-Ships[ship]+i]="[+]"
        else:
            if ((int(spot[1:])+Ships[ship])<10):
                for i in range(0, Ships[ship]):
                    self.grid[int(spot[1:])+i][self.grid[0].index("["+str(spot[0]).upper()+"]")]="[+]"              
            else:
                for i in range(0, Ships[ship]):
                    self.grid[12-Ships[ship]+i][self.grid[0].index("["+str(spot[0]).upper()+"]")]="[+]"
    def printObfuscatedGrid(self):
        obfuscatedGrid=deepcopy(self.grid)
        for i in range(len(obfuscatedGrid)):
            for x in range(len(obfuscatedGrid[i])):
                if ((obfuscatedGrid[x][i] == "[o]") or (obfuscatedGrid[x][i] == "[+]")):
                    obfuscatedGrid[x][i] = "[?]"
            #print " ".join(obfuscatedGrid[i])
        for i in obfuscatedGrid:
            print " ".join(i)                  
    def hit(self, spot):
        coordinates=self.grid[int(spot[1:])+1][self.grid[0].index("["+str(spot[0]).upper()+"]")]
        print coordinates
        if (coordinates=="[o]"):
            self.grid[int(spot[1:])][self.grid[0].index("["+str(spot[0]).upper()+"]")]="[0]"
            print "Miss!"
        if(coordinates=="[+]"):
            self.grid[int(spot[1:])][self.grid[0].index("["+str(spot[0]).upper()+"]")]="[x]"
            print "Hit!"
            self.timesHit+=1
def shipSetUp(player):
    for ship in Ships:
        print "Ship: ",ship,"\n Length: ", Ships[ship], "\n"
        spot=raw_input("Where would you like to place it?\n(*Example: B5*)\n->")
        direction=raw_input("Would you like it to go right or down(r/d)?\n->")[0]
        player.playerGrid.addShip(spot,direction,ship)
        clear()
        player.playerGrid.printGrid()         
def takeTurn(playerA,playerB):
    clear()
    print "--------- Tracking Grid ----------"
    playerB.playerGrid.printObfuscatedGrid()
    print "--------- Your Grid ----------"
    playerA.playerGrid.printGrid()
    print " Your turn ",playerA.name, " !"
    point = raw_input("Please input coordinates to target!\n(*Example: B5*)\n->")
    playerB.playerGrid.hit(point)
    clear()
    print "--------- Tracking Grid ----------"
    playerB.playerGrid.printObfuscatedGrid()    
    holder=raw_input("Press any key to continue!\n->")
    if (playerB.playerGrid.shipsCovering==playerB.playerGrid.timesHit):
        playerA.winner=True
    clear()
def prettyPrintGrid(grid):
    for i in grid:
        print " ".join(i)
def main():
    player1=Player(1,raw_input("Please enter your name Player 1\n->"))
    print "Please set up your battleships"
    player1.playerGrid.printGrid()
    shipSetUp(player1)
    clear()
    player2=Player(2,raw_input("Please enter your name Player 2\n->"))
    print "Please set up your battleships"
    player2.playerGrid.printGrid()
    shipSetUp(player2)
    while ((player1.winner==False)and(player2.winner==False)):
        takeTurn(player1,player2)
        if (player1.winner ==False):
            takeTurn(player2,player1)
    if (player1.winner==True):
        print "Congratulations ",player1.name,"! You win!"
    else:
        print "Congratulations ",player2.name,"! You win!"
    endGame=raw_input("Please press any key to end game!\n->")
    clear()
main()
