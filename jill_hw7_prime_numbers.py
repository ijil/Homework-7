#Jill Lee
#March 9, 2011
#This program takes a number from the user and lists all prime numbers from 2
#up to that number.

n=eval(input("Prime numbers up to? "))
user_list=list(range(2,n,1)) #makes a list from 2 to number entered by user
prime_numbers=[] #initializes the list of prime numbers

while len(user_list)!=0: #The program will remove each prime number from the
                         #first list and add it to the prime number list. This
                         #while loop will run until there are no more numbers
                         #left in user_list.
    prime_numbers.append(user_list[0]) #First, move the first number on the list
                                       #from user_list to prime_numbers. 
    for s in user_list: #Then look at the remaining numbers.
        if s%prime_numbers[-1]==0: #If they are multiples (remainder 0) of the
                                   #number just added,
            user_list.remove(s)    #remove them. 

print("Prime numbers:\n"+str(prime_numbers))
