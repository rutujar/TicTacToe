b = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']    
player = 1    
   
 
Win = 1    
Draw = -1    
Running = 0    
Stop = 1    
  
Game = Running    
Mark = 'X'    
   
  
def Board():    
    print(" %c | %c | %c " % (b[1],b[2],b[3]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (b[4],b[5],b[6]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (b[7],b[8],b[9]))    
    print("   |   |   ")    
   
   
def Pos(x):    
    if(b[x] == ' '):    
        return True    
    else:    
        return False    
   
  
def CheckWin():    
    global Game    
      
    if(b[1] == b[2] and b[2] == b[3] and b[1] != ' '):    
        Game = Win    
    elif(b[4] == b[5] and b[5] == b[6] and b[4] != ' '):    
        Game = Win    
    elif(b[7] == b[8] and b[8] == b[9] and b[7] != ' '):    
        Game = Win    
       
    elif(b[1] == b[4] and b[4] == b[7] and b[1] != ' '):    
        Game = Win    
    elif(b[2] == b[5] and b[5] == b[8] and b[2] != ' '):    
        Game = Win    
    elif(b[3] == b[6] and b[6] == b[9] and b[3] != ' '):    
        Game=Win    
      
    elif(b[1] == b[5] and b[5] == b[9] and b[5] != ' '):    
        Game = Win    
    elif(b[3] == b[5] and b[5] == b[7] and b[5] != ' '):    
        Game=Win    
 
    elif(b[1]!=' ' and b[2]!=' ' and b[3]!=' ' and b[4]!=' ' and b[5]!=' ' and b[6]!=' ' and b[7]!=' ' and b[8]!=' ' and b[9]!=' '):    
        Game=Draw    
    else:            
        Game=Running    
    
  
print("Player 1 [X] --- Player 2 [O]\n")    

  
while(Game == Running):    
       
    Board()    
    if(player % 2 != 0):    
        print("Player 1's chance")    
        Mark = 'X'    
    else:    
        print("Player 2's chance")    
        Mark = 'O'    
    ch = int(input("Enter 1-9 to mark : "))    
    if(Pos(ch)):    
        b[ch] = Mark    
        player=player+1    
        CheckWin()    
    
   
Board()    
if(Game==Draw):    
    print("Game Draw")    
elif(Game==Win):    
    player=player-1    
    if(player%2!=0):    
        print("Player 1 Won")    
    else:    
        print("Player 2 Won") 
