
from os import system, name
from time import sleep
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
Ships={"Carrier":5, "Battleship":4, "Cruiser":3, "Submarine":3, "Destroyer":2}

class Player:
    def __init__(self,number):
        self.playerGrid=Grid()
        self.number=number
class Grid:
    length=11
    def __init__(self):
        self.grid=[["[  ]", "[A]","[B]","[C]","[D]","[E]","[F]","[G]","[H]","[I]","[J]"]]
        for i in range(0,11):
            if i<10:
                row=["["+str(i)+" ]"]
            else:
                row=["["+str(i)+"]"]
            for x in range(0,10):
                row.append( "[o]" )
            self.grid.append(row)
    def printGrid(self):
        for i in self.grid:
            print i
    def addShip(self,spot,direction,ship):      
       #print spot,direction,ship
        #print self.grid[int(spot[1:])+1][self.grid[0].index("["+str(spot[0]).upper()+"]")]
        if (direction.upper()=="R"):
            if (self.grid[0].index("["+str(spot[0]).upper()+"]")+Ships[ship]<10):
                for i in range(0,Ships[ship]):
                    self.grid[int(spot[1:])+1][self.grid[0].index("["+str(spot[0]).upper()+"]")+i]="[+]"
            else:
                for i in range(0,Ships[ship]):
                    self.grid[int(spot[1:])+1][11-Ships[ship]+i]="[+]"
        else:
            if (int(spot[1:])+Ships[ship]<10):
                for i in range(0, Ships[ship]):
                    self.grid[int(spot[1:])+1+i][self.grid[0].index("["+str(spot[0]).upper()+"]")]="[+]"              
            else:
                for i in range(0, Ships[ship]):
                    self.grid[12-Ships[ship]+i][self.grid[0].index("["+str(spot[0]).upper()+"]")]="[+]"
      

    def obfuscate(self):
        obfuscatedGrid=self.grid
        for i in range(len(obfuscatedGrid)):
            for x in range(len(obfuscatedGrid[i])):
                if ((obfuscatedGrid[x][i] == "[o]") or (obfuscatedGrid[x][i] == "[+]")):
                    obfuscatedGrid[x][i] = "[?]"
                
                
                    


def shipSetUp(player):
    for ship in Ships:
        
        print "Ship: ",ship,"\n Length: ", Ships[ship], "\n"
        spot=raw_input("Where would you like to place it?\n(*Example: B5*)\n->")
        direction=raw_input("Would you like it to go right or down(r/d)?\n->")[0]
        player.playerGrid.addShip(spot,direction,ship)
        clear()
        player.playerGrid.printGrid()         
def main():
    player1=Player(1)
    player2=Player(2)
    print "Please set up your battleships"
    player1.playerGrid.printGrid()
    shipSetUp(player1)
    clear()
    print "Please set up your battleships"
    player2.playerGrid.printGrid()
    shipSetUp(player2)
main()
