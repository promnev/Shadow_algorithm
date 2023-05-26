import random
import time

level = 0
table_list = []

print(
    'The game generates a 2-, 3-, or 4-digit number depending on the selected difficulty level\nand a simple algorithm based on the digits of this number and one simple arithmetic operation\n(addition, or modulo difference), after which it returns 9 pairs of numbers (before and after transformation by the algorithm).\nYour task is to understand the algorithm and calculate the pair for the 10th number.')

level_question = input('Please select the difficulty level by typing the appropriate command: flexi\perm\senior\n')

if level_question == 'flexi':
    level = 1
if level_question == 'perm':
    level = 2
if level_question == 'senior':
    level = 3

base_len = level + 1
random_scope = random.randint(2, base_len)
random_base_indexes_list = random.choices([n + 1 for n in range(base_len)], k=random_scope)
random_aggregator = random.choice(['+', '-'])


def generate_base(level):
    if level == 1:
        return random.randint(10, 99)
    if level == 2:
        return random.randint(100, 999)
    if level == 3:
        return random.randint(1000, 9999)


def generate_base_list(level):
    base_list = []

    for n in range(11):
        base = generate_base(level)
        base_list.append(base)

    base_set = set(base_list)

    if len(base_list) == len(base_set):
        return base_list
    else:
        return generate_base_list(level)


def algorithm(base):
    global result
    base_as_list = [n for n in str(base)]
    increment_list = [base_as_list[(n - 1)] for n in random_base_indexes_list]
    increment_str = ''.join(increment_list)
    increment_int = int(increment_str)

    if random_aggregator == '+':
        result = base + increment_int
    if random_aggregator == '-':
        result = abs(base - increment_int)

    return result


def play():
    enter_text = 'algorithm generation'
    loading_text = '.....\n'

    for i in enter_text:
        time.sleep(0.01)
        print(i, end='', flush=True)

    for i in loading_text:
        time.sleep(0.5)
        print(i, end='', flush=True)

    base_list = generate_base_list(level)

    for n in base_list:
        table_list.append(f'{n} {algorithm(n)}')

    for n in table_list[:9]:
        print(n)

    ten_value = table_list[10].split(' ')
    print(ten_value[0])

    answer = ten_value[1]

    game_over = False

    while not game_over:
        question = input('what number should be the next?')

        if question == answer:
            print('Right!\n')
            game_over = True
        #elif question == 'debug':
            #print(answer)
        else:
            print('Wrong')

play()
