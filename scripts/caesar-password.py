#/usr/bin/env python3

chars_down = list('abcdefghijklmnopqrstuvwxyz')
chars_up = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
nums = list('0123456789')

def round_index(index, length):
    if index >= 0 and index < length: return index
    if index >= length: return index % length
    return round_index(length + index, length)

def find_index(item, ls) -> int:
    for i in range(len(ls)):
        if ls[i] == item: return i

while True:
    key = int(input('Type the key(number): '))
    message = input('Type the message: ')
    option = input('Encode or Decode?[e/d] ')

    if option != 'e' and option != 'd':
        print('Option not found. Try again.')
    
    for i in range(len(message)):
        message = list(message)
        if option == 'e':
            if message[i] in chars_up:
                message[i] = chars_up[round_index(find_index(message[i], chars_up) + key, len(chars_up))]
            elif message[i] in chars_down:
                message[i] = chars_down[round_index(find_index(message[i], chars_down) + key, len(chars_down))]
            elif message[i].isdigit():
                message[i] = str(round_index(int(message[i]) + key, 10))
        else: # decode
            if message[i] in chars_up:
                message[i] = chars_up[round_index(find_index(message[i], chars_up) - key, len(chars_up))]
            elif message[i] in chars_down:
                message[i] = chars_down[round_index(find_index(message[i], chars_down) - key, len(chars_down))]
            elif message[i] in nums:
                message[i] = str(round_index(int(message[i]) - key, 10))
    
    print(''.join(message))

