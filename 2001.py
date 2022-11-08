import random


def type_of_dice():
    """The function takes the cube type as string from the user
    and returns the cube type as int
    :rtype: int
    :return type of dice"""
    while True:
        type_of_dices = ['D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100']
        dice_type = input('Choose the type of dice to play: D3, D4, D6, D8, D10, D12, D20, D100 ')
        if dice_type in type_of_dices:
            dice_type_array = dice_type[1:]
            dice_type = ''.join(dice_type_array)
            dice_type = int(dice_type)
            break
        else:
            print('You entered the wrong type of dice')
    return dice_type


def user_throw():
    dice_type1 = type_of_dice()
    dice_type2 = type_of_dice()
    throw = random.randint(1, dice_type1) + random.randint(1, dice_type2)
    return throw


def comp_throw():
    type_of_dices = [3, 4, 6, 8, 10, 12, 20, 100]
    dice_type1 = random.choice(type_of_dices)
    dice_type2 = random.choice(type_of_dices)
    throw = random.randint(1, dice_type1) + random.randint(1, dice_type2)
    return throw


def game():
    user_points = user_throw()
    comp_points = comp_throw()
    print(f'Your points: {user_points}')
    print(f'Computer points: {comp_points}')
    while user_points < 2001 and comp_points < 2001:
        throw_user = user_throw()
        throw_comp = comp_throw()
        if throw_user == 7:
            user_points = user_points // 7
        elif throw_user == 11:
            user_points = user_points * 11
        else:
            user_points = user_points + throw_user
        print(f'Your points: {user_points}')

        if throw_comp == 7:
            comp_points = comp_points // 7
        elif throw_comp == 11:
            comp_points = comp_points * 11
        else:
            comp_points = comp_points + throw_comp
        print(f'Computer points: {comp_points}')

    if user_points > 2001 and comp_points < 2001:
        print('You won')
    elif user_points < 2001 and comp_points > 2001:
        print('Computer won')
    else:
        print('Draw')


if __name__ == '__main__':
    game()
