#FUNCTIONS
#TODO: Write your header comment here.
#A, lab 11, Prof Hayes
# Milestone 5 - make a UIC-CS App
# This will be manually graded by the TAs. It must include:

# -Welcome Message when App is started############################################################
# -Menu that allows user:#########################################################################
#  1--to look up SCE restaurant hours##############################################################
#  2--get contact information for UIC student clubs################################################
#  3--allow you to “share” information with friends and add them to your contact list##############
#  4--assist with advising for a cs major, ds major, cs+design major, or cs minor##################

# TODO: Define your functions here.
#1######
def student_center(r_name):
    r_name = r_name.upper()
    sce_rests = {"PANDA EXPRESS": "not open this summer.     :(",
    "CHICK-FIL-A": "open this summer.",
    "CIRCLE BURGER": "not open this summer.",
    "CRAVE CHICAGO": "not open this summer.",
    "DUNKIN' DONUTS": "open this summer.",
    "MARKET @ HALSTED": "open this summer.",
    "MOE'S SOUTHWEST GRILL": "open this summer.",
    "SBARRO": "not open this summer.",
    "SUBWAY": "not open this summer.",
    "WOW BAO": "not open this summer.",
    "UNITED TABLE": 'open this summer.'
    }

    if r_name in sce_rests:
        print(f'{r_name} is {sce_rests[r_name]}')
    else:
        print('Not a valid answer, please restart entire program')
#2######
def cs_club_info(c_name):

    fullNames = {"WICS": "Women in Computer Science",
    "LOGICA": "Latinx Organization for Growth in Computing and Academics",
    "ACM": "Association for Computing Machinery",
    "LUG": "Linux User Group"
    }

    url = {"WICS": "https://wics.students.uic.edu/",
    "LOGICA": "https://logica.students.uic.edu/",
    "ACM": "https://acm.cs.uic.edu/about/",
    "LUG": "https://lug.cs.uic.edu/about.html" 
    }

    others = {
        "AIAA",
        "AICHE",
        "ASCE",
        "ASHRAE",
        "ASME",
        "BMES",
        "BSJ",
        "CMAA",
        "ECS",
        "EDT",
        "EMBS",
        "EWH",
        "ESW",
        "GDSC",
        "IEEE",
        "IISE",
        "NSBE",
        "OSTEM",
        "SAE",
        "SASE",
        "SHPE",
        "SSBC",
        "SWE",
        "VESE"
    }

    engrURL = 'https://engineering.uic.edu/undergraduate/student-groups/' 

    #makes the parameter input uppercase
    c_name = c_name.upper()

    #checks if parameters meets conditions
    if c_name in fullNames:
        if c_name != "LUG":
            return f'Stands for: {fullNames[c_name]}', f'website: {url[c_name]}', True
        else:
            return fullNames[c_name], url[c_name], False
    elif c_name in others:
        return "This is part of the general College of Engineering Clubs", f'website: {engrURL}', False
    else:
        return "Not a recognized club.", "", False
#3######
def contacts(amigos, new):

    #ERROR1: Checks if function has fewer than 2 elements, than it wont be added 
    if len(new) < 2:
        return len(amigos), False
    name = new[0]
    num = new[1]

    #ERROR2: Checks if function is called with non-string elements
    if type(name) != type(""):
        return len(amigos), False
    
    if type(num) != type(""):
        return len(amigos), False

    #ERROR3: Checks if function has more than 2 elements, if so only first two are added, while rest is gone
    # AND 
    #ERROR4: Checks format
    counter = 0
    if name not in amigos:
        if len(num.split("-")) == 3 and len(num) == 12 and len(new) >= 2:
            amigos[name] = num
            a = len(amigos) > counter
            counter += 1
        else:
            a = len(amigos) < counter
    else:
        return len(amigos), False
    return len(amigos), a

#4###### THIS FUNCTION DOES WORK BECAUSE I HAVE TO DOWNLOAD FILES, I DO NOT HAVE THOSE FILES
# def make_dict(filename):
#     file = open(filename)
#     list = file.readlines()
#     dict = {}
#     for line in list:
#         each = line.split()
#         dict[each[0]] = int(each[1])
#     return dict

# def iadvise(degree, courses):
#     degree = degree.upper()
#     url = "https://cs.uic.edu/undergraduate/"

#     needed_credits = 0
#     courses_dic = {}

#     if degree == "CSMINOR":
#         courses_dic = make_dict("csminor.txt")
#         needed_credits = 18
#     elif degree == "CSMAJOR":
#         courses_dic = make_dict("csmajor.txt")
#         needed_credits = 43
#     elif degree == "CS+DESIGNMAJOR":
#         courses_dic = make_dict("cs+designmajor.txt")
#         needed_credits = 27 
#     elif degree == "DSMAJOR":
#         courses_dic = make_dict("dsmajor.txt")
#         needed_credits = 27
#     else:
#         return None #If input is invalid 

#     earned = 0
#     remaining = []

#     for i,j in courses_dic.items(): #loops through keys/ values 
#         if i in courses: #gets the keys
#             earned += j #adds the speciic credit if found
#         elif i not in courses: #checks if i is not in courses
#             remaining.append(i) #appends the key to "remaining"

#     # return earned, needed_credits, remaining
#     print(f'\nYou have earned:{earned} credits\nYou have remaining:{needed_credits} credits for this major\nThe courses left to take are: {remaining}')







#################################################    
def welcome(name):
    print("\nHi " + name + ', I hope you are having a great day, Welcome to the menu.')
    option = input("*****Please enter the number associated with the menu option you desire below*****\n1.)Search up if a UIC Student Center East restaurant is open or closed during summer \n2.)Get information for UIC student clubs \n3.)Store one friend's name and phone number \n*****Just enter the number here*****:")

    if option == '1':
        restaurant = input('\n*****Please enter a resturaunt in the Student Center East*****: ')
        student_center(restaurant)

    elif option == '2':
        lst_clubs = input('*****Do you want a list of the COE club abbreviations? Yes or No*****:')
        lst_clubs = lst_clubs.upper()

        if lst_clubs == "YES":
            print("\nCS Clubs: WiCS, LOGiCA, ACM, LUG\nGeneral College of Engineering clubs: AIAA, AICHE, ASCE, ASHRAE, ASME, BMES, BSJ, CMAA, ECS, EDT, EMBS, EWH, ESW, GDSC, IEEE, IISE, NSBE, OSTEM, SAE, SASE, SHPE, SSBC, SWE, VESE")

        print('\nYou will recieve 3 returns, the first is the full form of the club abbreviation, the second is the club\'s listed website, the last return will return True if the website of the club you chose is still active and False if it isn\'t')
        UIC_club = input('*****Please enter an abbreviation of a UIC CS COE Club or a general COE Student Organization Club*****: ')
        print('\n')
        print(cs_club_info(UIC_club))

    elif option == '3':
        print('\nHere are some things to keep in mind:\n 1: If you enter less than two elements, it will not attempt to be added.\n 2: The phone number should be formatted: "123-456-7890". If what you entered is called with an improperly formatted phone number, it will not attempt to be added.')
        print('Also, once you store a friend inside this dictionary, it will return how many friends you have and if it was successfully added or not(True or False)')
        Ready_or_not = input('\n*****Have you read the policies above? Yes or No*****: ')
        Ready_or_not = Ready_or_not.upper()
        if Ready_or_not == "YES":
            Old_contacts = {}
            friend_number = input('\n**Enter a friend\'s first name and their phone number... Add a space between these two**: ')
            friend_number = friend_number.split()
            # New_contact = {friend_number[0]: friend_number[1]}

            dic = contacts(Old_contacts, friend_number)
            print(dic)
        else:
            print('\nInvalid answer....You should read the policies and say Yes..Please restart the program')



if __name__ == '__main__':
    # TODO: Call your functions here to test
    print('        ⣰⡀⠀⣠⡀⢀⣴⣾⡇⠀⣀⣀')
    print('       ⢰⡯⣳⡾⢻⣷⠯⠽⠿⠯⣉⣩⣿⢿⡄')
    print('    ⢀⣤⣾⠛⡽⠷⠛⠀⠀⠀⠀⢤⡤⠟⠋⣜⣏⣷⡄')
    print('     ⣷⣶⡌⠃⠀⠠⠞⣿⣍⡓⢦⡀⢣⣀⡰⣿⣟⣁')
    print(' ⠀⠀⠀⣇⣇⣇⡀⠀⠰⢋⣈⡏⠙⣧⠱⠀⠉⠛⡹⢸⡈⢻⡄')
    print('⠀ ⣠⣖⠛⠋⠉⠉⠓⢧⡀⣿⣄⢀⡿⠀⠀⠀⠀⠀⢨⡿⣭⡇')
    print(' ⠀⣇⠀⠀⠀⠰⠄⠀⠀⠈⠉⠉⠋⠀⠀⠀⠀⠀⠀⡸⠙⣎⠀⠀⠀⣀')
    print('⠀ ⠈⢏⠑⠢⡀⠀⠀⠀⠀⡠⠃⠀⠀⠀⠀⠀⠀⣶⣧⣤⡿⢀⣀⣤⢿⡙⢦')
    print('    ⠀⠈⠓⠦⠬⣑⣒⣒⡯⠴⠦⡤⠤⠤⠖⠀⠀⠏⠹⣾⣫⠭⠭⠴⠚⠙⣌⢧')
    print('⠀⠀⠀        ⠀⠀⣠⠟⠁⠀⣿⠲⣄⣽⡉⣹⣷⡶⢦⣼⣀⡀⠘⣾')
    print('⠀⠀⠀⠀     ⠀⠀⠀⡼⢁⡖⠀⠀⣿⡀⡘⢯⠻⡟⠁⠙⢆⠉⠉⠉⢳⡟')
    print('            ⠀⣷⠊⠀⠀⠀⢸⢸⣿⣸⠀⢯⠉⠒⢌⣧⠀⠀⠘⠁')
    print('⠀⠀    ⠀⠀⠀⠀⠀⢰⠃⠀⠀⠀⠀⢾⣾⠿⠃⠀⠈⣿⠟⠉⠉⢧')
    print('   ⡴⢦⡀⠀⠀⠀⢀⡴⠒⠋⠙⡿⠀⠀⠀⠀⢀⡾⠋⠀⠀⠀⠀⠀⣏⡒⣄⠈⢷⡀')
    print('  ⣰⡇⢀⠙⢦⠀⢰⠏⠀⠀⠀⠘⡇⠀⠀⠀⠀⠈⠁⠀UIC\'s⠹⡟⠛⠀⠀⢳')
    print('  ⣿⠀⡏⢦⣈⣇⣟⠀⠀⠀⠀⠈⢿⠀⠀Sparky ⠀   ⠀⢸⢧⠀⠀⢆⢸⡄')
    print('  ⠻⠞⣇⠈⠹⣄⠸⡀⠀⠀⠀⠀⠀⠀⠀D.⠀⢀⠀⠀⠀⠀⠀⢠⣷⠼⠃⠀⡼⣸⠁')
    print('⠀⠀⢸⡄⢻⣮⡳⢿⣄⠀⠀Dragon⢀⣠⠔⠃⠀⠀⡖⠒⠲⡽⠁⠀⠀⢠⡧⠋')
    print('⠀   ⠻⡄⠉⢾⣴⢮⠉⠛⠒⠒⠒⣉⠉⠀⢸⡟⠲⡄⢸⠷⠞⠁⠀⠀⣠⠟')
    print('⠀⠀⠀  ⠘⢦⡀⠉⠛⠰⢯⣙⡆⢰⣇⣙⡆⠸⠓⠊⠉⠀⠀⠀⠀⢀⡼⠋')
    print('⠀       ⠙⠦⣄⡀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡶⠛⠁')
    print('⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠉⠙⠲⠦⢤⣄⣀⣀⣀⣤⠶⠶⠚⠉')
    name = input('*****Hi, Welcome to the UIC iEasy app, please enter your name and click enter*****:')
    welcome(name)

