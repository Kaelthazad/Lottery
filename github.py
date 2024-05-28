import random
import datetime
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

def random_lottery_numbers(widget):
    sys_random = random.SystemRandom()
    result = []
    while len(result) < 6:
        rand_num = sys_random.randint(1, 45)
        if rand_num not in result:
            result.append(rand_num)
    result.sort()
    label_random.text = 'Lottery Numbers: {}'.format(result)

def predefined_lottery_numbers(widget):
    available_numbers = [34, 43, 27, 17, 12, 13, 33, 1, 39, 20, 26, 18, 14, 4, 2, 40, 24, 45, 38, 31, 11, 10, 37]
    result = random.sample(available_numbers, 6)
    result.sort()
    label_predefined.text = 'Lottery Numbers: {}'.format(result)

def datetime_lottery_numbers(widget):
    global label_datetime, label_datetime_numbers
    sys_random = random.SystemRandom()
    dt = datetime.datetime.now()
    label_datetime.text = 'Datetime: ' + str(dt)

    num_list = [int(d) for d in str(dt) if d.isdigit()]

    result = []
    for i in range(6):
        first_digit = sys_random.choice(num_list)
        second_digit = sys_random.choice(num_list)
        num = int(str(first_digit) + str(second_digit))

        while num in result or num > 45 or num == 0:
            first_digit = sys_random.choice(num_list)
            second_digit = sys_random.choice(num_list)
            num = int(str(first_digit) + str(second_digit))
        result.append(num)
    result.sort()

    label_datetime_numbers.text = 'Lottery Numbers: ' + ', '.join(str(x) for x in result)

def color_probability_lottery_numbers(widget):
    sys_random = random.SystemRandom()
    result = []
    color_probs = [21.6, 23.3, 21.3, 22.6, 11.2]
    colors = [
        [num for num in range(1, 11)],
        [num for num in range(11, 21)],
        [num for num in range(21, 31)],
        [num for num in range(31, 41)],
        [num for num in range(41, 46)]
    ]
    while len(result) < 6:
        selected_color = sys_random.choices(colors, weights=color_probs)[0]
        num = sys_random.choice(selected_color)
        if num not in result:
            result.append(num)
    result.sort()
    label_color.text = 'Lottery Numbers: ' + ', '.join(str(x) for x in result)

def custom_lottery_numbers(widget):
    result = []
    nums_picked = input_field.value
    nums_picked = [int(num.strip()) for num in nums_picked.split(',') if num.strip().isdigit()]

    if len(nums_picked) > 5:
        label_custom.text = 'You can enter up to 5 numbers only'
        return

    result.extend(nums_picked)
    sys_random = random.SystemRandom()
    while len(result) < 6:
        rand_num = sys_random.randint(1, 45)
        if rand_num not in result:
            result.append(rand_num)
    result.sort()
    label_custom.text = 'Lottery Numbers: ' + str(result)

def build(app):
    global label_random, label_predefined, label_datetime, label_datetime_numbers
    global label_color, label_custom, input_field

    main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

    label_random = toga.Label('1. Generating random lottery numbers between 1 and 45', style=Pack(padding=(0, 5)))
    button_random = toga.Button('Generate Random Numbers', on_press=random_lottery_numbers)
    
    label_predefined = toga.Label('2. Generating random lottery numbers from higher probability numbers', style=Pack(padding=(0, 5)))
    button_predefined = toga.Button('Generate Predefined Numbers', on_press=predefined_lottery_numbers)
    
    label_datetime = toga.Label('3. Generating lottery numbers using the current datetime digits', style=Pack(padding=(0, 5)))
    label_datetime_numbers = toga.Label('', style=Pack(padding=(0, 5)))
    button_datetime = toga.Button('Generate Datetime Numbers', on_press=datetime_lottery_numbers)
    
    label_color = toga.Label('4. Generating lottery numbers based on color probabilities', style=Pack(padding=(0, 5)))
    button_color = toga.Button('Generate Color Probability Numbers', on_press=color_probability_lottery_numbers)
    
    input_label = toga.Label('5. Enter numbers up to 5, separated by commas:', style=Pack(padding=(0, 5)))
    input_field = toga.TextInput(style=Pack(flex=1))
    button_custom = toga.Button('Generate Custom Numbers', on_press=custom_lottery_numbers)
    label_custom = toga.Label('', style=Pack(padding=(0, 5)))
    
    main_box.add(label_random)
    main_box.add(button_random)
    name_label = toga.Label('', style=Pack(padding_top=10))
    main_box.add(name_label)
    main_box.add(label_predefined)
    main_box.add(button_predefined)
    name_label = toga.Label('', style=Pack(padding_top=10))
    main_box.add(name_label)
    main_box.add(label_datetime)
    main_box.add(label_datetime_numbers)
    main_box.add(button_datetime)
    name_label = toga.Label('', style=Pack(padding_top=10))
    main_box.add(name_label)
    main_box.add(label_color)
    main_box.add(button_color)
    name_label = toga.Label('', style=Pack(padding_top=10))
    main_box.add(name_label)
    main_box.add(input_label)
    main_box.add(input_field)
    main_box.add(button_custom)
    main_box.add(label_custom)
    name_label = toga.Label('', style=Pack(padding_top=10))
    main_box.add(name_label)

    name_label = toga.Label('Developed by [박제우], saladin1229@gmail.com', style=Pack(padding_top=10))
    main_box.add(name_label)

    name_label = toga.Label('1. 랜덤', style=Pack(padding_top=10))
    main_box.add(name_label)

    name_label = toga.Label('2. 확률높았던 숫자 반 추려서 랜덤', style=Pack(padding_top=10))
    main_box.add(name_label)

    name_label = toga.Label('3. 현재시간 숫자 추출해서 랜덤', style=Pack(padding_top=10))
    main_box.add(name_label)

    name_label = toga.Label('4. 색에 따른 당첨 확률 적용해서 랜덤', style=Pack(padding_top=10))
    main_box.add(name_label)

    name_label = toga.Label('5. 번호 선택후 나머지 랜덤', style=Pack(padding_top=10))
    main_box.add(name_label)

    return main_box

def main():
    return toga.App('Lottery Numbers Generator', 'org.beeware.lottery_numbers', startup=build)

if __name__ == '__main__':
    main().main_loop()
