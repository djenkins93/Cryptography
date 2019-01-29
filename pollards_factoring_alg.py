#The following is a computational rendering of Pollard Factoring method which techinally could be applied in trying to break
#ceratin cryptography methods such as RSA.
#Objective: The purpose of this code is to break some "large" composite number created by multplying to large primes together
#upon finding a factor we can then use this factor to break the "key"

print ("***Generating Primality Test Values for Pollard's (p-1) algoritm ***")
def compositeGen(): #initialize random prime num. generation
        global p,q,n
        p = random_prime(1000) #generate random prime1
        q = random_prime(1000) #generate random prime2
        n = (p*q) #multiply the two primes together

        print p,'>> p :1st prime'
        print q,'>> q :2nd prime'
        print n,'>> n :p * q'

compositeGen()

#print ('***Generating test value for factor***')
def valueGen():
    print ''
    print ('***Generating test value for factor***')
    #Check to make sure that 'a' is corpime to 'n'
    global a
    a = randint(2,n)
    while gcd(a,n) != 1:
         a = randint(2,n)
    print a, '>> a :for a mod n'

valueGen()

def factorSearch():
    print ''
    print ('***Searching for suitable factor***')
    print ''
    print ("Please select an iteration limit for factor search")
    print ("1. Default limit (1-10)")
    print ("2. Custom limit (1-?)")
    global B
    #checker = False
    while True :
            select = int(raw_input("Enter a Selection: "))

            if select == 1:
                print ("You selected, 1.Default Limit")
                B = 10
                
                break

            elif select == 2:
                print("You selected, 2.Custom Limit")
                B = int(raw_input("Enter Custom Limit"))
                break
            
            elif select == '' :
                print ("No selecltion was made.")
                
                break

               
    
    for i in range(0,B):
        g = gcd((a**i)-1,n)
        if g > 1 and g < n:
            print 'Found factor "g",' , g
            break
        
    if g == 1 or g == n:
         print 'Factor cannot be found. Set new limit and try again?'
    
        

factorSearch()