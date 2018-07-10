#set the intial value to zero
sum = 0
#set the range from 0 to 1000
for n in range(1,1000):
    #check the value is divisble by 3 or 5
    if(n%3 == 0 or n%5==0):
        #adding the n value to sum value
        sum = sum + n
        #return the cumulative sum value
        print(sum)
