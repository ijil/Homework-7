#Jill Lee
#March 9, 2011
#This program creates a list from the numbers entered by the user and then removes
#duplicates in the list.

def removeDuplicates(somelist):
    for i in somelist:
        n=somelist.count(i)     #counts how many times a value appears
                                #in the list

        while n>1:              #If n is larger than 1 (which means that a value
            somelist.remove(i)  #appears more than once), a duplicate value will
            n=n-1               #get erased. Everytime a duplicate gets erased,
                                #n gets smaller by 1. When n becomes 1 (which
                                #must mean that only one occurance of a value is
                                #left), the value is not erased, and the for
                                #loop moves onto the next value in the list.

print("Enter number to add to list. Enter an asterisk(*) when you're done.")
x=input("Enter a number: ")
somelist=[]
while x!='*':
    somelist.append(eval(x))
    x=input("Enter a number: ")

print("Starting list:\n",somelist)

removeDuplicates(somelist)

print("Duplicates removed:\n",somelist)
