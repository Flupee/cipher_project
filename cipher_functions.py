# Functions for running an encryption or decryption.
def encrypt_letter(char, key_stream):
    '''(str, int) -> str
    This function will receive a character and a keystream value
    to get the encrypt the character.
    
    >>>encrypt_letter('L', 11)
    'X'
    >>>encrypt_letter('E', 25)
    'D'
    '''
    char = char.upper()
    #The ascii value for uppercase letters
    ascii_value = 65
    #Turn the letter to an ascii value and subtract 65 to get the 
    #value the of the letter on the alphabetical order
    letter_to_num = ord(char) - ascii_value
    #Get the encrypted value
    encrypt_num = letter_to_num + key_stream
    #Check for the case that the encrypt value is 26 or over
    if (encrypt_num >= 26):
        encrypt_num -= 26
    #Return the encrypt value as its letter value    
    return chr(encrypt_num + ascii_value)


def decrypt_letter(char, key_stream):
    ascii_value = 65
    letter_to_num = ord(char) - ascii_value        
    encrpyt_num = letter_to_num - key_stream
    if (encrpyt_num < 0):
        encrpyt_num += 26
    return chr(encrpyt_num + ascii_value)

# The values of the two jokers.
JOKER1 = 27
JOKER2 = 28

# Write your functions here:
def clean_message(message):
    '''(str) -> str
    This function will take a message as its parameter and return only its 
    alphabetical characters and in uppercase.
    
    >>> clean_message("hEllO&*( thiS<< is a mesS*age")
    "HELLOTHISISAMESSAGE"
    '''
    #Initialize copy variable
    copy = ""
    #For loop to check if the value in the string is a letter
    for letter in (message):
    #If the value is a letter, then add it to the copy variable
        if (letter.isalpha() == True):
            copy += letter
    #Set copy string to uppercase         
    copy = copy.upper()
    return copy


def swap_cards(card_list, index):
    if (index + 1 == len(card_list)):
        card_list[0], card_list[index] = card_list[index], card_list[0]
    else:
        card_list[index], card_list[index + 1] = card_list[index + 1], card_list[index]
        
def move_joker_1(card_list):
    index = 0
    index = card_list.index(JOKER1)
    if (index + 1 == len(card_list)):
        card_list[index], card_list[0] = card_list[0], card_list[index]
    else:
        card_list[index + 1], card_list[index] = card_list[index], card_list[index + 1]


def move_joker_2(card_list):
    index = 0
    index = card_list.index(JOKER2)
    #Joker 2 is the last card
    if (index + 1 == len(card_list)):
        card_list[index], card_list[0] = card_list[0], card_list[index]
        card_list[1], card_list[0] = card_list[0], card_list[1]
    #Joker 2 is the second last card
    elif (index + 2 == len(card_list)):
        card_list[index+1], card_list[index] = card_list[index], card_list[index+1]
        card_list[index+1], card_list[0] = card_list[0], card_list[index+1]
    #Joker 2 is anywhere else
    else:
        card_list[index + 1], card_list[index] = card_list[index], card_list[index + 1]
        card_list[index + 2], card_list[index + 1] = card_list[index + 1], card_list[index + 2]


def triple_cut(card_list):
    first_joker_index = 0
    second_joker_index = 0
    index1 = card_list.index(JOKER1)
    index2 = card_list.index(JOKER2)
    if(index1 < index2):
        first_joker_index = index1
        second_joker_index = index2
    else:
        first_joker_index = index2
        second_joker_index = index1
    card_list[second_joker_index+1:], card_list[:first_joker_index] = card_list[:first_joker_index], card_list[second_joker_index+1:]
    

def insert_top_to_bottom(card_list):
    index_length = len(card_list)-1
    bottom_num = card_list[index_length]
    if(bottom_num == JOKER2):
        bottom_num = JOKER1
    card_list[bottom_num:index_length], card_list[:bottom_num] = card_list[:bottom_num], card_list[bottom_num:index_length]

    
def get_card_at_top_index(card_list):
    top_card = card_list[0]
    if (top_card == JOKER2):
        top_card = JOKER1
    return card_list[top_card]

def get_next_value(card_list):
    move_joker_1(card_list)
    move_joker_2(card_list)
    triple_cut(card_list)
    insert_top_to_bottom(card_list)
    key_stream = get_card_at_top_index(card_list)
    return key_stream

def get_next_keystream_value (card_list):
    key_stream = get_next_value(card_list)
    while (key_stream == JOKER1 or key_stream == JOKER2):
        key_stream = get_next_value(card_list)
    return key_stream

def process_message(card_list, message, crypt):
    proper_message = clean_message(message)
    crypted_message = ''
    for i in range(len(proper_message)):
        key_stream = get_next_keystream_value(card_list)
        if(crypt == 'e'):
            crypted_message += encrypt_letter(proper_message[i], key_stream)
        elif(crypt == 'd'):
            crypted_message += decrypt_letter(proper_message[i], key_stream)
    return crypted_message

def process_messages(card_list, message_list, crypt):
    crypted_message_list = []
    for i in range(len(message_list)):
        crypted_message_list.append(process_message(card_list, message_list[i], crypt))
    return crypted_message_list

def read_messages(message_file):
    all_lines = message_file.readlines()
    return all_lines


def read_deck(deck_file):
    all_lines = deck_file.readlines()
    final_list = []
    for next_line in all_lines:
        final_list += next_line.split()
    final_list = list(map(int, final_list))
    return final_list
    