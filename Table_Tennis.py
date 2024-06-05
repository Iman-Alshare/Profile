### Write Your Code Here ###

def check_input(inpt, n=-1):
    '''
    this function take care of the input format, the range values and the number of entered values
    '''

    try:
        inp = [int(x) for x in inpt]
        if(n==-1 and len(inp)==2):
            if(inp[0]< 2 or inp[0]>500):
                print('\nPlease enter 2<=n<-500')
                return []  
                
            if(inp[1]< 2 or inp[1]>1e12):
                print('\nPlease enter 2<=k<-1e12')
                return [] 
            return inp
        elif(n==-1):
            print('\nPlease enter only 2 numbers.')
            return []  
        
        elif(len(inp)==n and n!=-1):
            lis = list(filter(lambda x: x<1 or x>500, inp))
            if(len(lis)==0): ##no out of range
                return inp
            else:
                print(f"\nEnter {n} sequence of numbers seperated by space: ")
                return []
    except:
        print('\nYou enter non integer values, Please, Enter only numbers: ')  
        return []
    
    return inp   


def find_winner(lis,k):
    '''
    find the winner who win k times
    if the k > len(list ) then print max value in the list will win otherwise based on on sequence 
       of play we find the
    
    Input: 
           - the list 
           - limit of win to determine the winner
    
    Output: print the max power of the winner
    
    '''
    wins_count = [0]*len(lis) ## define
    while(True):
        if (k in wins_count):
            print(f"The winner power is {wins_count.index(k)+1}")
            return
        elif( k>= len(lis) ):
            print(f"The winner power is {max(lis)}")
            return
        elif(lis[0]> lis[1]):
            wins_count[lis[0]-1]+=1
            lis = [lis[0]]+lis[2:]+[lis[1]]
        else:
            wins_count[lis[1]-1]+=1
            lis = [lis[1]]+lis[2:]+[lis[0]]
    
def main():
    '''
    In this main function the user enter
    - number of element n
    - number of winings k
    - called the find_winner function to determine the winner based on k
    
    limitation its doesn't handle multipspace between the input numbers 
    ''' 
    inp = input('Enter 2 numbers sperated by space: ')
    inp = inp.strip()
    inp = check_input(inp.split(' '))
    while(inp==[]):
        inp = input('Enter 2 numbers sperated by space: ')
        inp = inp.strip()
        inp = check_input(inp.split(' '))

    
    array = input(f"Enter {inp[0]} sequence of numbers seperated by space: ")
    array = array.strip()
    array = check_input(array.split(' '), inp[0])
    while(array==[]):
        array = input(f"Re-Enter {inp[0]} sequence of numbers seperated by space: ")
        array = array.strip()
        array = check_input(array.split(' '),inp[0])
        
    find_winner(array, inp[1])
    
main()
