import time  # import to add pause

#  user responses
answer_A = ['A', 'a']
answer_B = ['B', 'b']
answer_C = ['C', 'c']
yes = ['Y', 'y', 'Yes', 'yes']
no = ['N', 'n', 'No', 'no']
funeral_names = ['mom', 'aunt', 'uncle', 'dog', 'cat', 'dad', 'brother', 'sister', 'grandma', 'grandpa']

#  objects to grab

toy_pokeball = 0
Baseball_Bat = 0
Golf_Club = 0
Molotov = 0
Pride_Flag = 0

required = "\nUse only A, B, or C\n"  # if user input is wrong
required_2 = '\nUse only Yes or No\n'


def intro():
    print('One day after school you are walking home when something familiar on the '
          'ground catches your eye, \nwhen you get closer to see it, you realize why it '
          'was familiar to you. It was a small toy Pokeball, how odd\n '
          'Do you want to pick it up? Y/N')
    choice = input('>>> ')
    if choice in yes:
        toy_pokeball = 1  # adds pokeball
    elif choice in no:
        toy_pokeball = 0
    else:
        print(required_2)
        print('')
        intro()
    if toy_pokeball > 0:
        print('')
        option_home()
    else:  # if the pokeball wasn't grabbed
        print('')
        option_call()


def option_home():
    if toy_pokeball == 1:
        print('When you got back to your house you were so excited to put your new pokeball on your shelf that you '
              'forgot to lock your door')
        time.sleep(1)
    print('After a few hours of doing homework and studying in your room, you hear a crash coming from downstairs')
    print('You consider your options before acting, you could go downstairs to see what\'s happening '
          'or you could just stay in your room, where it\'s safe.')
    print('Would you like to go and check out the noise? Y/N')
    choice = input('>>> ')
    if choice in yes:
        option_battle()
    elif choice in no:
        option_room()
    else:
        print(required_2)


def option_call():
    print("Your phone rings and it's your friend Austin calling to invite you to the golf course with him")
    print('what will you do?')
    time.sleep(1)
    print("""    A. Tell him yes
    B. tell him no and thank him
    C. tell him no and try to give an excuse""")
    choice = input(">>> ")
    if choice in answer_A:
        print('You tell him that you have to drop your backpack off at home and then you will be on the way.\n')
        option_golf()
    elif choice in answer_B:
        print("You thank him for offering but tell him that you aren't up for it today\n")
        option_home()
    elif choice in answer_C:
        print('')
        option_excuse()
    else:
        print(required)
        print('')
        option_call()


def option_golf():
    print("yeet")


def option_funeral():
    print('"Oh no!" says Austin "Who died?"\n')
    time.sleep(2)
    print('Quick! come up with something!!\n')
    lie = input("it was my ")
    print("Uhm yeah it was my {0}\n".format(lie))
    time.sleep(2)
    if lie.lower() in funeral_names:
        print('"Oh I\'m sorry to hear that, I hope you have a good day and I am sorry for your loss"')
        time.sleep(1)
        print("Good, you don't need Austin anyway. He was probably planning on murdering you or something\n"
              "he definitely seems shifty sometimes\n")
        option_home()
    else:  # if the input is not in the list
        print('"I don\'t know about that, sounds kind of fishy to me"\n')
        print('Ah heck, he didn\'t believe you, your embarrassment is immeasurable for you have been found\n'
              'out as the bad person that you are, for shame\n\n')
        print('You lose\n')
        option_funeral()
        # time.sleep(1)
        # print('try again? Y/N')
        # choice = input(print('>>> '))
        # if choice in yes:
        #     print('')
        #     intro()
        # else:
        #     print('\nThe End')


def option_excuse():
    print('I would love to but I actually...')
    time.sleep(1)
    print("""          A. have homework to do
          B. have to go to a funeral
          C. have to go to a play with my mom""")
    choice = input(">>> ")
    if choice in answer_A:
        print('Austin tells you that he understands and wishes you a good day')
        time.sleep(1)
        print('You continue on your way\n')
        option_home()
    elif choice in answer_B:
        print('')
        option_funeral()
    elif choice in answer_C:
        print("Austin says that it's okay and that he will see you tomorrow at school\n")
        option_home()
    else:
        print(required)
        print('')
        option_excuse()


intro()
