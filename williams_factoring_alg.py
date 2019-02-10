print "*** Beginning William's Factoring Algorithm ***"

def iteration_value():
    global B
    global cycle
    
    print "Please begin by selecting a value for the iteration process, (the default value provided is 10)."
    while True :
            print "1. To Continue, or press 2.Create a custom limit"
            select = int(raw_input("Enter a Selection: "))

            if select == 1:
                print ("You selected, 1.Default Limit")
                cycle = 5
                B = factorial(cycle)
                
                break

            elif select == 2:
                print("You selected, 2.Custom Limit")
                cycle = int(raw_input("Enter Custom Limit"))
                B = factorial(cycle)
                break
            
            elif select == '' :
                print ("No selecltion was made.")
                
                break
                
iteration_value()

print ('*** Generating Composite Value ***')
def compositeGen(): #initialize random prime num. ge neration
        global p,q,n
        p = random_prime(50) #generate random prime1
        q = random_prime(50) #generate random prime2
        n = (p*q) #multiply the two primes together

        print p,'>> p :1st prime'
        print q,'>> q :2nd prime'
        print n,'>> n :p * q'

compositeGen()

def z_valueGen():
    print ''
    print '*** Generating components of "z" ***'
    
    #various "z" values
    global z
    global z_comp
    global z_check
    
    #components of "z"
    x = randint(2,10)
    y = randint(2,10)
    d = randint(2,10)
    print "The components of z (x,y,d):", x,y,d,
    
    z = (x + y * (math.sqrt(d)) )
    print ''
    print "The value of z: ", z
    #create a conditional check for the values  'z' and 'z_comp' (for z compliment)
    z_comp = (x - y * (math.sqrt(d)) )
    print "The value of z_comp:", z_comp
    z_check = z * z_comp
    print "The z_check value:", z_check
    

z_valueGen()

print ""
print "*** Beginning search for a factor of 'n' ***"
def z_factorSearch():
    print ""
    
    
    Z = gcd(z_check,n)
    if Z != 1:
        print "A factor of 'n' has been found!"
        print Z , ", is the factor of 'n' "
        
    fac = 1
    if Z == 1:
        for i in range(1,cycle + 1):
            I =  (z**fac) % n
            fac = fac * i
            D = gcd(I,n)
            
            if  D != 1:
                print "A factor of 'n' has been found!"
                print D , ", is the factor of 'n' "
                break
    if D == 1:
        #This setup will run until a factor is found for the composite number created 
        # continue to generate random components for "z" until a factor is found for the composite value "n"
        z_valueGen()
        z_factorSearch()

        #final check for the factor generated tested against the factorial "B!" we created at the begnning
z_factorSearch()
