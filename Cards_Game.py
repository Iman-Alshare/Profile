import numpy as np

def create_deck(): #48 cards
    '''
    This function fill the deck every time the luckiest_game function is called 
    '''
    deck = []
    for i in range(2,11):
        deck+=[str(i)]*4
    deck+=['k']*4
    deck+=['g']*4
    deck+=['j']*4
    return deck

def pick_cards(deck):
  '''
    This function returns a list of random 4 cards are picked from the deck and remove them from the deck list
  '''

  cards = []
  if(len(deck)>=4):
   for i in range(4):
        
    card = np.random.randint(len(deck))
    cards.append(deck[card])
    deck.remove(deck[card])
  
  return cards, deck
        
def generate_cards():
  '''
   this will randomly generate list of 4 cards and returns without any cheng on the number of cards in deck
  '''

  cards = []
  for i in range(4):
    card = np.random.randint(4)
    if(card==0):
        cards.append('k')
    elif (card==1):
        cards.append('g')
    elif (card==2):
        cards.append('j')
    elif (card==3):
        cards.append('n') # number #str(np.random.randint(1,11)))
 
  return cards

def counting_machine_game():
    '''
    This function will mange the counting_machine_game between the machine and human user.
    The rules of the game are:
      1- The machine play first and it can pass or swap based randomly and the machine swap 
          done based on of the elment with maximum occuarnce :
          
            - if the element with maximum occuarnce in the ground cards then swap with the first different element 
                not equal to that element in the machine cards
    
            - if the element is not in the ground cards then randomly swap cards
            
      2- The user choose to pass or swap and define the swaped vaules
      3- check if one of the player collect 4 cards of the same type
      4- iterate until one of the player wins
      5- at the end of every round the ground_cards are changed
      
      -As a remark we assume any integer a number type and encode in the game as n letter
      -Also we assume the deck always full of cards
      - The system check if the input of the user in his cards or the ground cards then play otherwise he ignore
         user turn and pass to the next round
    '''
    

    print('The counting machine\n')
    human_cards = generate_cards()
    machine_cards = generate_cards()
    ground_cards = generate_cards()
    
    while(True):
        print('---------------------------------------------------------------') 
        print('                          Machine Turn') 
        print('---------------------------------------------------------------') 
        computer_swape = np.random.randint(2)
        if(computer_swape==1): #swap or pass pass =0 swap =1

            num_occurence_elemnts = list((machine_cards.count(elm)  for elm in machine_cards))
            ind = num_occurence_elemnts.index(max(num_occurence_elemnts))
            
            if(machine_cards[ind] in ground_cards): # if the element with max occure in ground then swap with
              ground_swape = ground_cards.index(machine_cards[ind])  # index of the card in the ground_cards
              computer_swaped = 0 #ind # index of the card in the machine_cards
              for i in range(len(machine_cards)):# find index to swap with in machine
                 if(machine_cards[i]!= machine_cards[ind]):
                    computer_swaped= i
                    break
            else: #random swap
              ground_swape = np.random.randint(4) # index of the card in the ground_cards
              computer_swaped = np.random.randint(4) # index of the card in the machine_cards
            tem = machine_cards[computer_swaped]
            machine_cards[computer_swaped] = ground_cards[ground_swape]
            ground_cards[ground_swape] = tem
            print('The card machine swaped is %s and swaped with is %s' %(ground_cards[ground_swape],machine_cards[computer_swaped]))
            print('The current ground cards is %s\n'%str(ground_cards))
            print('The Machine cards are %s\n'%str(machine_cards))
            
            num_occurence_elemnts = list((human_cards.count(elm)  for elm in human_cards))
            if(max(num_occurence_elemnts)==4): 
                print('\nThe machine Wins!!')
                break
        ###user turn
        print('---------------------------------------------------------------') 
        print('                          User Turn') 
        print('---------------------------------------------------------------') 
        num_occurence_elemnts = list((human_cards.count(elm)  for elm in human_cards))
        ind = num_occurence_elemnts.index(max(num_occurence_elemnts))
          
        print('\nYour cards are %s'%str(human_cards))
        print('The ground cards are %s'%str(ground_cards))
        swap = input('Enter Which card you want to swap (in your hand) or if you want pass: ')
        swap = swap.strip()
        swap_with=''
        if(swap in human_cards):
            swap_with = input('Enter Which card you want to swap (in ground): ')
            swap_with = swap_with.strip()
            if(swap_with in ground_cards):
                tem  = swap
                human_cards[human_cards.index(swap)] = swap_with
                ground_cards [ground_cards.index(swap_with)]  =  swap         
                print('The ground cards are %s\n'%str(ground_cards)) 
                
        num_occurence_elemnts = list((human_cards.count(elm)  for elm in human_cards))        
        if(max(num_occurence_elemnts)==4): 
            print('\nYou Wins!!')
            break     
        ground_cards = generate_cards()                        
 


def luckiest_game(deck):
     '''
     This function find the palyer who collect more score during picks a cards of the deck,
     untill the deck is empty.
     
     This function stop when the deck is empty
     
     The rules:
       - The player and machine win based on the total cards they collect from all the round
       - The user input if is found in the hand and in the ground then collect all the cards with same char entered by the use 
       - If the user input the character a and j card in the hand he will collect all cards on the ground
       - If the user enter p the he will pass his turn
       - In every round the machine and user collect cards based on the 4 picked cards at that round
       - The collected cards at all round will be saved in total card list to track who's the winner 
       - We assume the deck only 48 [2-10] and king, jack and girl
     '''
    
     print('The luckiest game\n')
     human_cards, deck = pick_cards(deck)
     machine_cards, deck = pick_cards(deck)
     ground_cards, deck = pick_cards(deck)
     total_human_cards = []
     total_machine_cards = []   
     while(True):
    
            
        print('---------------------------------------------------------------') 
        print('                          Machine Turn') 
        print('---------------------------------------------------------------')    
        print('The machine cards before collect are %s\n'%machine_cards)        
        print('The ground cards before collect are %s\n'%ground_cards)
        if ('j' in machine_cards):
            machine_cards += ground_cards
            ground_cards = []
        else:
          for c in machine_cards:  # optimal collect if there is j in machine hand
            if (c in ground_cards):
                machine_cards += [c]*ground_cards.count(c)
                ground_cards = list(filter(lambda a: a != c, ground_cards))
        print('---------------------------------------------------------------')    
        print('The machine cards after collect are %s\n'%machine_cards)        
        print('The ground cards after collect are %s\n'%ground_cards)
        
        print('---------------------------------------------------------------') 
        print('                          User Turn') 
        print('---------------------------------------------------------------')
        
        print('''You can enter the name of the card you want to collect based on follwing rules:
        1- If there is j card in your cards then you can enter %s to collect all cards on the ground
        2- If there is similar card in hand and on the ground you can collect them
        3- If you want to end your turn enter p\n''' %('\u0332' +'a' ))
        print('---------------------------------------------------------------')
        print('The human cards before collect are %s\n'%human_cards)   
        print('The ground cards before collect are %s\n'%ground_cards)
        inp = input('Enter the card you want to collect: ')
        inp = inp.strip()
        while(inp !='p'):
            if (inp =='a' and 'j' in human_cards): ## enter a to collect all if j in hand
                human_cards += ground_cards
                ground_cards = []
            elif(inp in ground_cards and inp in human_cards):
                human_cards += [inp]*ground_cards.count(inp)
                ground_cards = list(filter(lambda a: a != inp, ground_cards))
            else:
                print('The enter card is not valid or it is not in your hand or on the ground.')
            inp = input('Enter the card you want to collect: ')
            inp = inp.strip()
       
        print('---------------------------------------------------------------')     
        print('The human cards after collect are %s\n'%human_cards)   
        print('The ground cards after collect are %s\n'%ground_cards)
     
    
        total_human_cards += human_cards
        total_machine_cards += machine_cards
        
        if(len(deck)==0):
            if(len(total_machine_cards)> len(total_human_cards)):
                print('The machine collected large score and beat the you\n')
            elif(len(total_machine_cards)< len(total_human_cards)):
                print('The human user collected large score and beat the machine\n')
            else:
                print('Balance!! both collect the same score.\n')
            break
            
        ground_cards,deck = pick_cards(deck)    
        machine_cards, deck = pick_cards(deck)
        human_cards,deck = pick_cards(deck)
        
        if(len(ground_cards)==0 or len(human_cards)==0 or len(machine_cards)==0):
            if(len(total_machine_cards)> len(total_human_cards)):
                print('The machine collected large score and beat the you\n')
            elif(len(total_machine_cards)< len(total_human_cards)):
                print('The human user collected large score and beat the machine\n')
            else:
                print('Balance!! both collect the same score.\n')
            break
            
        
def main():
    '''
    In the main function you can run two games or exit from the program. 
    If the user input 1 then the main will run the counting_machine_game.
    If the user input 2 then the main will run the luckiest_game.
    If the user input 3 then the main will exit.
    '''
    while (True):
      print('Game can be played:\nThe counting machine game: enter 1\nThe luckiest game: enter 2\nTo exit from the program: enter 3\n')
      inp = 0
      try:
        inp = int((input('\nEnter which game you want to play: ')))  
      except:
        print('Enter only 1,2 or 3')
      if(inp == 1):
         counting_machine_game()
         print('---------------------------------------------------------------')   
      elif(inp==2):
         deck = create_deck()
         luckiest_game(deck)  
         print('---------------------------------------------------------------') 
      elif(inp==3):
         print('\nYou exit')
         break 
        
main()    