#set the range for 'a' from range of 0 to 1000
for a in range(0,1000):
    ##set the range for 'b' from range of 0 to 1000
    for b in range(0,1000):
        #obtain 'c' value subracting a and b from 1000
        c= 1000- a -b
        #check whether c is greater thean zero and not
        if c>0:
            #check whether pythagorean is satisfied or not
            if c**2 == (a**2) + (b**2):
                #print product of 'a','b','c'
                print(a*b*c)