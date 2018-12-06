#!/bin/bash
#The following program is meant to run through the  Diffe-Hellman/Public Key Exchange
# + encryption schemes
# + the following code is divided into sections Steps "0-4"
# + need to clean-up code...sperate in to various functions...create "main" function
# + make a call to "expmod" function for both genrated-key and the shared-key
# + this could possibly fix the current issue


# Step(0): Public-key generation "p" & "g"

echo "                  ...Initializing Diffe-Hellman Key Exchange...           "
echo "###################################################################################"
echo "Generating a public keys 'p'&'g'... >  " # obtain a positive prime value from the user"

p=0  # first public key to begin key exchange and generation
g=0  # second public key to initiate key echange and generation
a=0  # private key selection for user(A)
b=0  # private key selection for user(B)
x=0  # generated key for user(A)
y=0  # generated key for user(B)
ka=0 # secret key for user(A)
kb=0 # secret key for user(B)

prime_checker()
{
local isPrime=true
h=$1
local j=$(echo "sqrt($h)" | bc)


i=2
while [ $i -le $j ]
        do
        if [ "$(( h % i ))" == 0 ]
        then
                isPrime=false
        fi
        (( i++ ))
        done

if [  "$isPrime" = true ]
then
        return 0
fi

if [  "$isPrime" = false ]
then
        return 1
fi
}

random_prime()
{

local validPrime=false
while [ "$validPrime" = false ]
do

        prime=$(shuf -i 100-10000 -n 1)
        if prime_checker $prime
        then
                validPrime=true
        fi

done

if [ "$validPrime" = true ]
then
        return 0
fi
}

random_prime
echo "Obtained Public-key 'p': $prime..."

expmod()
{

local g=$1
local n=$2
local p=$3

local prod=1

for (( i=1; i<=$n; i++ ))
        do
                prod=$(( ((g*prod % p ) + p) % p ))
done
echo $prod
}

primitive_root_checker()
{
local p=$1
local g=$2
local n=$(( (p-1)/2 ))
local dummy
local isPrimitive=true

for (( i=1; i<=$n; i++ ))
do
        dummy=$(expmod $g $i $p)
        if [ "$dummy" -eq 1 ]
        then
                isPrimitive=false
        fi
done

if [ "$isPrimitive" = true ]
then
        return 0
fi

if [ "$isPrimitive" = false ]
then
        return 1
fi
}

random_primitive()
{

local p=$1
local m=$((p-1))
local validPrimitive=false
while [ "$validPrimitive" = false ]
do

        g=$(shuf -i 2-$m -n 1)
        if primitive_root_checker "$p" "$g"
        then
                validPrimitive=true
        fi

done

if [ "$validPrimitive" = true ]
then
        return 0
fi
}


random_primitive "$prime"
echo "Obtained 2nd Public-key 'g': $g..."



# Step(1): Private key slection by user "A" and user "B"

echo "                  ...Initializing private-key selection...           "
echo "###################################################################################"

echo -n "Please select a private-key for user(A) > "
read a

echo -n "Please select a private-key for user(B) > "
read b




# Step(2): Compute the public-key values for user "A" and user "B"; (i.e) x=(g^(a) mod p)...

x=$(expmod $g $a $prime)
y=$(expmod $g $b $prime)

echo "user(A) has generated key > $x "
echo "user(B) has generated key > $y "




# Step(3): Exchange public-keys inorder to generate secret-key (decryption-key)

echo "                  ...Swapping generated keys...   "
echo "#############################################################################"
echo "user(A) receives generated key > $y "
echo "user(B) receives generated key > $x "




# Step(4): Create secret key (decryption key) for both users(A,B) using the exchanged key set

echo "                  ...Sharing secret decryption-keys...    "
echo "#############################################################################"


sa=$(expmod $y $a $prime )
sb=$(expmod $x $b $prime )

echo "Users have created and shared secret keys:  ($sa,$sb) "