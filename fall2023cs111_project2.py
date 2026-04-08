#If statements/ booleans
# TODO: Write your header comment here.
#A
# COPY AND PASTE YOUR CODE FROM THE PREVIOUS MILESTONE
# TODO: Write your code here.
import math
print('--------------------------------\n         UIC CS Track\n--------------------------------\n')



cs_major = str(input('QUESTION 1\nAre you a CS major? (Yes or No): '))


counter = 0
counter2 = 0
if((cs_major == 'YES') or (cs_major == 'yes') or (cs_major == 'Yes')):
    doNotForget = str(input('\nQUESTION 2\nHave you taken ENGR100? (Yes or No): ')) #Asks Question 2
    if((doNotForget == 'no') or (doNotForget == 'No') or (doNotForget == 'nO') or (doNotForget == 'NO') or (doNotForget == 'Yes') or (doNotForget == 'YES') or (doNotForget == 'yes') or (doNotForget == 'yeS') or (doNotForget == 'yEs')):
        taken11 = str(input('\nQUESTION 3\nHave you taken CS111? (Yes or No): ')) #level 1 input
        if((taken11 == 'Yes') or (taken11 == 'YES') or (taken11 == 'yes') or (taken11 == 'yeS') or (taken11 == 'yEs')):
            counter += 3
        elif((taken11 == 'nO') or (taken11 == 'no') or (taken11 == 'No') or (taken11 == 'NO')):
            taken12 = str(input('Have you taken CS112? (Yes or No): ')) #level 1 input
            if((taken12 == 'Yes') or (taken12 == 'YES') or (taken12 == 'yes') or (taken12 == 'yeS') or (taken12 == 'yEs')):
                counter += 3
            elif((taken12 == 'nO') or (taken12 == 'no') or (taken12 == 'No') or (taken12 == 'NO')):
                taken13 = str(input('Have you taken CS113? (Yes or No): ')) #level 1 input
                if((taken13 == 'Yes') or (taken13 == 'YES') or (taken13 == 'yes') or (taken13 == 'yeS') or (taken13 == 'yEs')):
                    counter += 3
                elif((taken13 == 'nO') or (taken13 == 'no') or (taken13 == 'No') or (taken13 == 'NO')):
                    counter += 0
                    counter2 += 3
    taken21 = str(input('\nQUESTION 4\nHave you taken CS141? (Yes or No): ')) #level 2 input
    if((taken21 == 'Yes') or (taken21 == 'YES') or (taken21 == 'yes') or (taken21 == 'yeS') or (taken21 == 'yEs')):
        counter += 3
    taken22 = str(input('\nQUESTION 5\nHave you taken CS151? (Yes or No): ')) #level 2  input
    if((taken22 == 'Yes') or (taken22 == 'YES') or (taken22 == 'yes') or (taken22 == 'yeS') or (taken22 == 'yEs')):
        counter += 3
        taken23 = str(input('\nQUESTION 6\nHave you taken CS211? (Yes or No): ')) #level 3 input
        if((taken23 == 'Yes') or (taken23 == 'YES') or (taken23 == 'yes') or (taken23 == 'yeS') or (taken23 == 'yEs')):
            counter += 3
        elif((taken23 == 'nO') or (taken23 == 'no') or (taken23 == 'No') or (taken23 == 'NO')):
            counter += 0
            counter2 += 3
        taken24 = str(input('\nQUESTION 7\nHave you taken CS251? (Yes or No): ')) #level 3 input
        if((taken24 == 'Yes') or (taken24 == 'YES') or (taken24 == 'yes') or (taken24 == 'yeS') or (taken24 == 'yEs')):
            counter += 4
            taken241 = str(input('Have you taken CS277? (Yes or No): ')) # level 3 input
            if((taken241 == 'Yes') or (taken241 == 'YES') or (taken241 == 'yes') or (taken241 == 'yeS') or (taken241 == 'yEs')):
                counter += 3
                taken242 = str(input('Have you taken CS377? (Yes or No): ')) #level 3 input
                if((taken242 == 'Yes') or (taken242 == 'YES') or (taken242 == 'yes') or (taken242 == 'yeS') or (taken242 == 'yEs')):
                    counter += 3
                elif((taken242 == 'nO') or (taken242 == 'no') or (taken242 == 'No') or (taken242 == 'NO')):
                    counter += 0
                    counter2 += 3
            elif((taken241 == 'nO') or (taken241 == 'no') or (taken241 == 'No') or (taken241 == 'NO')):
                counter += 0
                counter2 += 3
            taken243 = str(input('Have you taken CS401? (Yes or No): ')) #level 3 input
            if((taken243 == 'Yes') or (taken243 == 'YES') or (taken243 == 'yes') or (taken243 == 'yeS') or (taken243 == 'yEs')):
                counter += 3
            elif((taken243 == 'nO') or (taken243 == 'no') or (taken243 == 'No') or (taken243 == 'NO')):
                counter += 0
                counter2 += 3
        elif((taken24 == 'nO') or (taken24 == 'no') or (taken24 == 'No') or (taken24 == 'NO')):
            counter += 0
            counter2 += 4
        taken25 = str(input('\nQUESTION 8\nHave you taken CS261? (Yes or No): ')) #level 3 input
        if((taken25 == 'Yes') or (taken25 == 'YES') or (taken25 == 'yes') or (taken25 == 'yeS') or (taken25 == 'yEs')):
            counter += 4
            ############################################################################## 4th level
            taken31 = str(input('\nQUESTION 9\nHave you taken CS301? (Yes or No): '))# level 4 input
            if((taken31 == 'Yes') or (taken31 == 'YES') or (taken31 == 'yes') or (taken31 == 'yeS') or (taken31 == 'yEs')):
                counter += 3
            elif((taken31 == 'nO') or (taken31 == 'no') or (taken31 == 'No') or (taken31 == 'NO')):
                counter2 +=3
            taken32 = str(input('\nQUESTION 10\nHave you taken CS341? (Yes or No): '))# level 4 input
            if((taken32 == 'Yes') or (taken32 == 'YES') or (taken32 == 'yes') or (taken32 == 'yeS') or (taken32 == 'yEs')):
                counter += 3
            elif((taken32 == 'nO') or (taken32 == 'no') or (taken32 == 'No') or (taken32 == 'NO')):
                counter2 +=3
            taken33 = str(input('\nQUESTION 11\nHave you taken CS342? (Yes or No): '))# level 4 input
            if((taken33 == 'Yes') or (taken33 == 'YES') or (taken33 == 'yes') or (taken33 == 'yeS') or (taken33 == 'yEs')):
                counter += 3
            elif((taken33 == 'nO') or (taken33 == 'no') or (taken33 == 'No') or (taken33 == 'NO')):
                counter2 +=3
            taken34 = str(input('\nQUESTION 12\nHave you taken CS361? (Yes or No): '))#level 4 input
            if((taken34 == 'Yes') or (taken34 == 'YES') or (taken34 == 'yes') or (taken34 == 'yeS') or (taken34 == 'yEs')):
                counter += 4
            elif((taken34 == 'nO') or (taken34 == 'no') or (taken34 == 'No') or (taken34 == 'NO')):
                counter2 +=4
            taken35 = str(input('\nQUESTION 13\nHave you taken CS362? (Yes or No): '))#level 4 input
            if((taken35 == 'Yes') or (taken35 == 'YES') or (taken35 == 'yes') or (taken35 == 'yeS') or (taken35 == 'yEs')):
                counter += 4
                taken36 = str(input('\nQUESTION 14\nHave you taken CS499? (Yes or No): ')) #lvl4 
            elif((taken35 == 'nO') or (taken35 == 'no') or (taken35 == 'No') or (taken35 == 'NO')):
                counter2 +=4
            #################################################################################
        elif((taken25 == 'nO') or (taken25 == 'no') or (taken25 == 'No') or (taken25 == 'NO')):
            counter += 0
            counter2 += 21
    elif(((taken21 == 'nO') or (taken21 == 'no') or (taken21 == 'No') or (taken21 == 'NO')) or ((taken22 == 'nO') or (taken22 == 'no') or (taken22 == 'No') or (taken22 == 'NO'))):
            counter += 0
            counter += 6

elif((cs_major == 'no')):
    print('\n--------------------------------\n           Summary\n--------------------------------')
    print('\nSadly, you are not a CS major.')



print('\n--------------------------------\n           Summary\n--------------------------------')
if((cs_major == 'YES') or (cs_major == 'yes') or (cs_major == 'Yes')): #will go down 5 if's 
    print('\nYou are a CS major!')
    if(taken22 == 'YES') or (taken22 == 'yes') or (taken22 == 'Yes'):
        if((taken25 == 'YES') or (taken25 == 'yes') or (taken25 == 'Yes')):
            if((taken35 == 'YES') or (taken35 == 'yes') or (taken35 == 'Yes')):
                if((taken36 == 'YES') or (taken36 == 'yes') or (taken36 == 'Yes')):
                    print('Congratulations on your upcoming graduation!')
    if((doNotForget == 'no') or (doNotForget == 'No') or (doNotForget == 'nO') or (doNotForget == 'NO')):
        print('Do not forget to take ENGR100!')
print(f'\nRequired CS credits earned: {counter}.')
print(f'Required CS credits left: {counter2}.')



print('\nThank you for using App!\nClosing app...')
