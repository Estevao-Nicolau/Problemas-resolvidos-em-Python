c = 1
letra =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] 
n = int(input())
while 1>n or n > 26:
    n = int(input())
for i in range(n):
    while c<=n:
        print(letra[c-1]*c)
        c += 1
            
        
    















'''
#n = int(input())
#alfabeto = ['','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
'''
'''
import string
 
n = int(input())
letters = list(string.ascii_lowercase[:n])
print(letters)
'''
'''
n = int(input())
def triângulo(n):
  
  s = ''
  i = n (1 <= n <= 26)
  c = 1
  while i>=1:
    s = s + str('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    print(s)
    i = i-1
triângulo2(n)
'''
'''
import string

n = int(input())
#alfabeto = ['','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letters = list(string.ascii_lowercase[:n])
print(letters)
'''
