#set the intial values
first,second = 1,1
#set the intial result to zero
total_sum = 0
#specify the first value is below 4 million
while first <= 400000:
    #checking the first value is even or not
    if first%2 ==0 :
        #add the even first value to total_sum i.e result
        total_sum = total_sum + first
        #as per the fibonacci series,second value will be sum of first and second
    first,second = second,first+second
    #print the final sum of even numbers
    print(total_sum)