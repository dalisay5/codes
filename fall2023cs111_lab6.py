#FOR LOOPS
# Lab 6 - DNA Matching

# Given two DNA strands of equal length, write a complete Python program to compare the corresponding bases, and report mismatches. For example, suppose the input to your program are the following two DNA strands:

# CCATGGTC
# CCAGTGAC
# then your program should produce the following output:

# CCATGGTC
#    XX X 
# CCAGTGAC
# **Differences: 3
# In other words, your program should output the first strand, then on the next line output a space if the corresponding bases are the same and an ‘X’ if not, followed by the second strand, followed by a summary of the # of differences. If the strands are identical, the # of differences reported should be 0.



# TODO: Write the program

input1 = input(str())
input2 = input(str())
counter = 0
i=0

print(input1.upper())

for str in input2:
    
    if(str != input1[i]):
        print('X', end='')
        counter += 1
    else:
        print(' ', end= '')
    
    i+=1

print(f'\n{input2.upper()}\n**Differences: {counter}')
