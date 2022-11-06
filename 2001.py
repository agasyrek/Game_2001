import random


def game():
    gamer1 = 0
    gamer2 = 0
    throw_dice = input('Throw the dices ')
    throw1 = random.randint(1, 6) + random.randint(1, 6)
    throw2 = random.randint(1, 6) + random.randint(1, 6)
    gamer1 = gamer1 + throw1
    gamer2 = gamer2 + throw2
    print(f'Gamer 1 points: {gamer1}')
    print(f'Gamer 2 points: {gamer2}')
    while gamer1 < 2001 and gamer2 < 2001:
        throw_dice = input('Throw the dices ')
        throw1 = random.randint(1, 6) + random.randint(1, 6)
        throw2 = random.randint(1, 6) + random.randint(1, 6)
        # print(f'throw1 {throw1}')
        # print(f'throw2 {throw2}')

        if throw1 == 7:
            gamer1 = gamer1 // 7
        elif throw1 == 11:
            gamer1 = gamer1 * 11
        else:
            gamer1 = gamer1 + throw1
        print(f'Gamer 1 points: {gamer1}')

        if throw2 == 7:
            gamer2 = gamer2 // 7
        elif throw2 == 11:
            gamer2 = gamer2 * 11
        else:
            gamer2 = gamer2 + throw2
        print(f'Gamer 2 points: {gamer2}')

    if gamer1 > 2001 and gamer2 < 2001:
        print('The winner is: Gamer 1')
    elif gamer1 < 2001 and gamer2 > 2001:
        print('The winner is: Gamer 2')
    else:
        print('Draw')


if __name__ == '__main__':
    game()
