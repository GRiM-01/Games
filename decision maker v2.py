import random as r

def greet():
    u_in1 = list(set(item.strip() for item in input("Wazzzup, Can't make up your mind? I can help! Tell me your choices: ").split(sep=',')))
    return u_in1


def choose(u_in1):
    print('I choose:',r.choice(u_in1),'\n')


def again():

    while True:

        try:
            u_in2 = str(input('Still feeling indecisive? (Y/N): ').upper())

            if u_in2 == 'Y' or u_in2 == 'N':
                return u_in2

            else:
                print("Invalid Entry, type Y or N.",'\n')

        except ValueError:
            print("Invalid entry, type the LETTER Y or N.",'\n')


while True:

    u_in1 = greet()
    choose(u_in1)

    u_in2 = again()

    if u_in2 == 'Y':
        continue
    elif u_in2 == 'N':
        print("Bye, I'm always here if you need help deciding",'\n')
        break
