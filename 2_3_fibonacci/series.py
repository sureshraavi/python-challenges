def fibonacci(n):
    n1, n2 = 0,1
    count = 0

    if n <=0:
        print ("please enter a positive integer")
    elif n ==1:
        print ("Fibonacci sequence upto",n,":")
        print(n1)
    else:
        print ("Fibonacci sequence:")
        while count < n:
            print(n1)
            nth = n1+ n2
            # update values
            n1 = n2
            n2 = nth
            count += 1

#calling fuction 
fibonacci(50)


def lucas(n):
    n1, n2 = 2,1
    count = 0

    if n <=0:
        print ("please enter a positive integer")
    elif n ==1:
        print ("Fibonacci sequence upto",n,":")
        print(n1)
    else:
        print ("Fibonacci sequence:")
        while count < n:
            print(n1)
            nth = n1+ n2
            # update values
            n1 = n2
            n2 = nth
            count += 1

#calling fuction 
lucas(12)

def sum_series(n, n1=0, n2=1):
    count = 0

    if n <=0:
        print ("please enter a positive integer")
    elif n ==1:
        print ("Fibonacci sequence upto",n,":")
        print(n1)
    else:
        print ("Fibonacci sequence:")
        while count < n:
            print(n1)
            nth = n1+ n2
            # update values
            n1 = n2
            n2 = nth
            count += 1

#calling fuction 
sum_series (22, 3, 2)