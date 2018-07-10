#set the intial sum to zero
sum = 0
#set the instial sqaures to zero
squares =0
#set the range from 1 to 100
for i in range(1,101):
    #add i value to sum
    sum = sum + i
    #add i2 value to squares
    squares = squares = i**2
    #diff is differnce betweeb sum of sqaures and squares sum
    diff =  sum**2 - squares
    #print the difference
print(diff)