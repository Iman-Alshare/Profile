 
import numpy as np    

board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

#p.random.seed(0)

def print_board():
    '''
    This function Print the board of the Tic_Toc_Toe game 
    
    Inputs:
      No Inputs
         
    Otput: Print The board after insert the input
      '''
    print()
    for i in range(len(board)):
        for j in range(len(board[i])-1):
            if(i<2):
             print('\u0332'+board[i][j]+'|', end='')
            else:
             print(board[i][j]+'|', end='')  
        if (i<2):
          print('\u0332'+board[i][2])
        else:
          print(board[i][2])
    print()    

def machine_chocie(machine_char,user_char):
    '''
    This function try to choose the best position to replace the char of the machine to win
    input :
      - machine_char: the machine char 
      - user_char: the user char 
      
      output:
        x: the row on the board
        y: the coloumn on the board
    '''
    ##check if the use try to close a path
    columns = list(zip(*board))
    x = 0 
    y = 0
    if(board[0].count(user_char)==2 and ' ' in board[0]):  ##row
        x = 1 
        y = board[0].index(' ')+1
        
    elif(board[1].count(user_char)==2 and ' ' in board[1]):
        x = 2
        y = board[1].index(' ')+1
        
    elif(board[2].count(user_char)==2 and ' ' in board[2]): 
        x = 3
        y = board[2].index(' ')+1
        
    elif(columns[0].count(user_char)==2 and ' ' in columns[0]):# column
        x = columns[0].index(' ')+1
        y = 1
          
    elif(columns[1].count(user_char)==2 and ' ' in columns[1]):
        x = columns[1].index(' ')+1
        y = 2
        
    elif(columns[2].count(user_char)==2 and ' ' in columns[2]):     
        x = columns[2].index(' ')+1
        y = 3  
        
    elif(board[0][0] == user_char and board[1][1] == user_char and ' '== board[2][2]): #diagonal
        x = 3
        y = 3
        
    elif(board[0][0] == user_char and board[2][2] == user_char and ' '== board[1][1]): #diagonal
        x = 2
        y = 2
    elif(board[1][1] == user_char and board[2][2] == user_char and ' '== board[0][0]): #diagonal
        x = 1
        y = 1
        
    elif(board[0][2] == user_char and board[1][1] == user_char and ' '== board[2][0]): #diagonal
        x = 3
        y = 1
        
    elif(board[0][2] == user_char and board[2][0] == user_char and ' '== board[1][1]): 
        x = 2
        y = 2
    elif(board[1][1] == user_char and board[2][0] == user_char and ' '== board[0][2]): 
        x = 1
        y = 3
    
    ##machine
    elif(board[0].count(machine_char)==2 and ' ' in board[0]):  ##row
        x = 1
        y = board[0].index(' ')+1
        
    elif(board[1].count(machine_char)==2 and ' ' in board[1]):
        x = 2
        y = board[1].index(' ')+1
        
    elif(board[2].count(machine_char)==2 and ' ' in board[2]): 
        x = 3
        y = board[2].index(' ')+1
        
    elif(columns[0].count(machine_char)==2 and ' ' in columns[0]):# column
        x = columns[0].index(' ')+1
        y = 1
          
    elif(columns[1].count(machine_char)==2 and ' ' in columns[1]):
        x = columns[1].index(' ')+1
        y = 2
        
    elif(columns[2].count(machine_char)==2 and ' ' in columns[2]):     
        x = columns[2].index(' ')+1
        y = 3  
        
    elif(board[0][0] == machine_char and board[1][1] == machine_char and ' '== board[2][2]): #diagonal
        x = 3
        y = 3
        
    elif(board[0][0] == machine_char and board[2][2] == machine_char and ' '== board[1][1]): #diagonal
        x = 2
        y = 2
    elif(board[1][1] == machine_char and board[2][2] == machine_char and ' '== board[0][0]): #diagonal
        x = 1
        y = 1
        
    elif(board[0][2] == machine_char and board[1][1] == machine_char and ' '== board[2][0]): #diagonal
        x = 3
        y = 1
        
    elif(board[0][2] == machine_char and board[2][0] == machine_char and ' '== board[1][1]): 
        x = 2
        y = 2
    elif(board[1][1] == machine_char and board[2][0] == machine_char and ' '== board[0][2]): 
        x = 1
        y = 3
    
    else:
    
        x = np.random.randint(1,4)
        y = np.random.randint(1,4)
            
        ###check the boarder
        while(board[x-1][y-1]!=' '):
            x = np.random.randint(1,4)
            y = np.random.randint(1,4)

    return x,y


def Tic_Toc_Toe(inp ,x, y):
    '''
    This function updates the board of the Tic_Toc_Toe with the player input 
    
    Inputs:
      inp: X or O capital 
      
      X: The position of row to put the input at
      
      y: The position of the column to put the input at
      
      output: Print The board after insert the input at (x-1,y-1) coordinates
      '''
    
    board[x-1][y-1]=inp
    print_board()
    
def check_winner(user_char):
    '''
    This function used to peridically chech if the current player wins
    
    Input: The charachter of the current player
    
    Output:
    return boolen flag indicates the current player wins if true otherwise the return false'''
    flag = False 
    
    if(board[0][0] == user_char and board[0][1]== user_char and board[0][2] ==user_char): #horizantal
        flag = True
    elif(board[1][0]==user_char and board[1][1]== user_char and board[1][2] ==user_char):
        flag= True
    elif(board[2][0]==user_char and board[2][1]== user_char and board[2][2] ==user_char):
        flag= True
    elif(board[0][0]==user_char and board[1][0]== user_char and board[2][0] ==user_char):#vertical
        flag= True
    elif(board[0][1]==user_char and board[1][1]== user_char and board[2][1] ==user_char):
        flag= True
    elif(board[0][2]==user_char and board[1][2]== user_char and board[2][2] ==user_char):
        flag= True
    elif(board[0][0]==user_char and board[1][1]== user_char and board[2][2] ==user_char):#diagonal
        flag= True
    elif(board[0][2]==user_char and board[1][1]== user_char and board[2][0] ==user_char):
        flag= True
    
    return flag
    
def enter_input(pos):
    '''
    this function restrict the user input to be only digits and in [1,2,3]'''
    x = 0
    if (pos=='x'):
        st = 'row'
    else:
        st = 'column'
    try:
            x = int(input(f"Enter the {st} to insert the input at (one of these values [1,2,3]): "))
            while(not x in [1,2,3]):
                x = int(input(f"Re-Enter the {st} to insert the input at (one of these values [1,2,3]): "))
    except:
            print('you enter non integer input!')
            enter_input(pos)
    return x     

def main():
    '''
    The main function runs the Tic_Toc_Toe game between the computer and a human user until one of the players wins
      or all board positions are filled.
      
      The charchter of the computer and user are picked randomly and then inform the user of his charchter (X or O).
      The computer choose his position at the board based on the the other player.
    outputs:
    
    if user wins print The User Wins
    
    if computer wins then print The Computer Wins
    
    if no empty position then print No One Wins
    '''
    free_pos = 9
    print('Initial State of the board:')
    print_board()
    
    user_char = 'X'
    flag = True
    if(np.random.randint(2)==1):
       user_char = 'O'
       
    while(free_pos):
        if (user_char=='X'):  
          if(flag) :
           print('User Turn (You are the %s):'%user_char)
           x = enter_input('x')
           y = enter_input('y')
            ## check if the position filled 
           while(board[x-1][y-1]!=' '):
                 print('The position is filled, Please Re-Enter a new postion:')
                 x = enter_input('x')
                 y = enter_input('y')
                    
           Tic_Toc_Toe(user_char ,x, y)
           free_pos-=1
           if(check_winner(user_char)):
                print('The User Wins')
                break
           flag =not flag 
            
          else:
            print('Computer Turn:')
          
            x, y = machine_chocie('O', user_char)
            ###check the boarder
            
            Tic_Toc_Toe('O' ,x, y)
            free_pos-=1
            if(check_winner('O')):
                print('The Computer Wins')
                break
            flag =not flag 
            
        elif (user_char=='O'):  
          if(not flag) :
           print('User Turn (You are the %s):'%user_char) 
           x = enter_input('x')
           y = enter_input('y')
                
            ## check if the position filled 
           while(board[x-1][y-1]!=' '):
                 print('The position is filled, Please Re-Enter a new postion:')
                 x = enter_input('x')
                 y = enter_input('y') 
                
           Tic_Toc_Toe(user_char ,x, y)
           free_pos-=1
           if(check_winner(user_char)):
                print('The User Wins')
                break
                
           flag =not flag 
            
          else:
            print('Computer Turn:')
  
            x, y = machine_chocie('X', user_char)
            ###check the boarder
            
            Tic_Toc_Toe('X' ,x, y)
            free_pos-=1
            if(check_winner('X')): 
                print('The Computer Wins')
                break
            flag =not flag   
          if(free_pos==0):
             print('No One Wins')

main()    