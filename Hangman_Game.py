
#Build a prgram that simulaates hangman game, you can find the game discription [Here](https://en.wikipedia.org/wiki/Hangman_(game)).

print('''Remark: If the enter charchters of the second player contains alphabet and a non-alphabet characters,
      then we remove the non-alphabet and treat the input as a sentence\n''')

print('Values of the Game Level input:\nEasy=> 1\nMedium=> 2\nHard=> 3\n')
level = int(input('Enter the game level: '))

text =''
### delete any non-alphabets characters and spaces in player_1 sentnces
small_lett_text_list=[]
while (small_lett_text_list==[]):
 text = input('Enter the text (Alphabetic Sentence Only): ')
 text = text.strip() 
 new_text =''
 for i in range(len(text)):
   if(text[i].isalpha() or( text[i]==' ' and text[i-1]!=' ')): 
     new_text += text[i]   
 small_lett_text = new_text.lower() 
 small_lett_text = small_lett_text.strip()
 text_char =  list(small_lett_text)   #with spaces list
 # without spaces list
 small_lett_text_list=[]
 for i in text_char:
    if(i !=' ' and not i in small_lett_text_list):
       small_lett_text_list.append(i)
## check 

### define number of trails
trail = 0
if(level==1):
    trail = 10 + len(small_lett_text)
elif(level==2):
    trail = 7 + len(small_lett_text)
elif(level==3):
     trail = 5 + len(small_lett_text)
    
### define the program
x=1
char_list = [] #track the correct choosing letters
chooesed = [] # track all choosing letters
wrong = []
while(x<=trail):
    
    if(len(char_list)==len(small_lett_text_list)):  ##if guess the sentence
        print('\nWOW you are brave, you got it right from the %d trial'%x)
        break
        
    char = input('Enter Alphabetic Character: ')
    print()   
    char = char.strip() 
    
    new_char_pl_2 = ''
    if (len(char)>1):  #remove strips non alpha
      for i in range(len(char)):
        if(char[i].isalpha() or(char[i]==' ' and char[i-1]!=' ')): 
           new_char_pl_2 += char[i]   
      new_char_pl_2 = new_char_pl_2.strip()
      new_char_pl_2 = new_char_pl_2.lower()
    else:
      new_char_pl_2 = char.lower()
    
    ## if it only digits and spaces    
    if(len(new_char_pl_2)==0):
        new_char_pl_2 = ' '
    
    if(len(new_char_pl_2) >1):
        if(small_lett_text.find(new_char_pl_2)!=-1):
            for i in new_char_pl_2:
                if(i.isalpha() and not i in char_list):
                  char_list.append(i)
                  chooesed.append(i)
            print('Greate Guess: %s' %new_char_pl_2) 
            
            for i in range(len(text_char)):
              if( text_char[i] in char_list or text_char[i]==' '):
                print(new_text[i],end='')
              else: 
                print('-',end='')
            print('\n')  
            
    elif(not new_char_pl_2.isalpha()):
        print('You entered a non-alphabet character')
        x-=1
    elif(new_char_pl_2 in chooesed):
        x-=1  
        print('You already entered this character and it was %s' %('RIGHT' if new_char_pl_2 in char_list else 'WRONG'))
        
    elif (new_char_pl_2 in text_char):
        char_list.append(new_char_pl_2)
        chooesed.append(new_char_pl_2)
        print('Greate Guess: %s' %new_char_pl_2)
        
        for i in range(len(text_char)):
           if( text_char[i] in char_list or text_char[i]==' '):
             print(new_text[i],end='')
           else: 
             print('-',end='')
        print(end ='\n')             
    else :
        chooesed.append(new_char_pl_2)
        wrong.append(new_char_pl_2)
        if(x==trail):
           print('You ran out of trials and Catched ',end='')
           for i in range(len(text_char)):
             if( text_char[i] in char_list or text_char[i]==' '):
                print(new_text[i],end='')
           print(end ='\n')    
           print('The right sentence is %s'%new_text)
           
        else:
          
         for i in range(len(text_char)):
            if( text_char[i] in char_list or text_char[i]==' '):
                print(new_text[i],end='')
            else:
                print('-',end='')
         print(end ='\n')           
         print('Wrong Chars:',end='')
         for i in range(len(wrong)-1):
           print(wrong[i],end='-')
         print(wrong[len(wrong)-1],end ='\n')
    print()      
    x+=1
print('\n')
if(len(char_list)==0):  ##wrong
    print('\nWOW you are brave, but it was a wrong answer The right one is %s'% new_text)