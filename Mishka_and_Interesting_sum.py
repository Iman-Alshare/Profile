### XOR Operation can be done by ^ operator ex: 2^3 ###
import numpy as np

### Write Your Code Here ###
def check_input(n,l, k=-1,b=-1):
    try:
        
        n = n.strip()
        if(l==1 and k==-1):
            n = int(n)
            if(n<1 or n>1e6):
                print('Enter n in the rand 1<=n<=1e6.')
                return ' '
                
        elif(l==2 and k!=-1):
            n = [int(x) for x in n.split(' ')]
           
            if(len(n)!=k):
                print(f"Enter {k} elements.")
                return ' '
            elif(list(filter(lambda x:x>1e9 or x<1, n))!=[]):
                print(f"Enter values in range 1<=a<=1e9.")
                return ' '
                
        elif(l==3 and k==-1):
            n = int(n)
            if(n<1 or n>1e6):
                print('Enter m in the rand 1<=m<=1e6.')
                return ' '
              
        elif(l==4 and k==2):
            n = [int(x) for x in n.split(' ')]
            if(len(n)!=k):
                print(f"Enter 2 elements:")
                return ' '
            elif(n[0]>n[1] or n[1]>b or n[0]<1):
                print(f"Enter values in range 1<=l<=r<={b}.")
                return ' '
              
    except:
        print('Enter only integers.')
        return ' '
    return n

def find_interesting_sum (lis,l,r):
   '''
   This function find the intersted sum after finding the element the in range [l,r]
   then we count the ocuuence of unique values and the insert the unique elements in
   the range [l,r] with even ocuuarnce.
   
   Input: 
      lis: List 
      l: Left index
      r: Right index
   
   Output return the intersted_sum 
   '''
   inter_sum = 0 
   values, counts = np.unique(lis[l-1:r], return_counts=True)
 
   tem =[]
   for i in range(len(values)):
         if(counts[i]%2==0):
            tem.append(values[i])
   if(len(tem)==0):
      return 0
   elif(len(tem)==1):
      return tem[0]
   else:
      inter_sum = tem[0]^tem[1]
      for i in range(2,len(tem)):
          inter_sum ^= tem[i]
      
   return inter_sum
    
def main():
  
  n = input('Enter number of elements: ')
  n = check_input(n,1)
  while(n == ' '):
        n = input('Enter number of elements: ')
        n = check_input(n,1)
     
  a = input(f"Enter {n} elements: ") 
  a = check_input(a,2,n)
  while( a ==' '):
        a = input(f"Enter {n} elements: ")
        a = check_input(a,2,n)
      
  m = input(f"Enter number of queries : ")   
  m = check_input(m,3)
  while( m == ' '):
        m = input('Enter number of queries: ')
        m = check_input(m,3)
  
  for i in range(m):
        q = input('Enter your query: ')
        q = check_input(q,4,2,n)
        while( q ==' '):
            q = input('Enter your of query: ')
            q = check_input(q,4,2,n)
        inter_sum = find_interesting_sum(a,q[0],q[1])
        print('-------------------------------------')
        print('Interesting sum = %d'%inter_sum)
        print('-------------------------------------')
main()