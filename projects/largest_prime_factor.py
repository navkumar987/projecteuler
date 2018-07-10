#define a funtion with a argument n
def largestprimefactor(n):
    #find the number divsible by 2 or not
    i=2
    #set the intial prime factor to zero
    primefactor =0
    #check the half of specified value is less than the intial value 2 or not
    while i <= n/i:
        #to check the value is divisble by 2 or not
        if n%i ==0:
            #if it is divisble by i set the primefactor to i
            primefactor = i
            #divide the n value with i and set it to n
            n= n/i
            #if is not divisble by i
        else:
            #add 1 to i and loop will continue
            i = i+ 1
            #check primefactor is less than the final n value
    if primefactor<n:
        #set the value of prime factor value to n if the above condition is true
        primefactor =n
        #return the prime factore
    return primefactor
#call the defined fundtion with required n value
print (largestprimefactor(600851475143))



