#to optimize the algorthim i have used fractions
#import fractions funtion
import fractions
#define a function with ar argument n
def smallestdivisble(n):
    #set the intial value to 1
    number = 1
    #set the range
    for i in range(1,n+1):
        #mutiply the i value with cureent number value and divide it wilth gdc for i and current number value
        number = (number*i)/fractions.gcd(number,i)
        #return the number
    return number
#print the smallest divsible value.Final Required Value.Change the Limit required at the end of the function
print ("Smallest Divisble Value by 1 to 20 is"+str(smallestdivisble(20)))