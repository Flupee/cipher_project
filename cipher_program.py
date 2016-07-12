"""
Encrypt or decrypt the contents of a message file using a deck of cards.
"""

import cipher_functions

DECK_FILENAME = 'deck1.txt'
MSG_FILENAME = 'message1.txt'
MODE = 'e'  # 'e' for encryption, 'd' for decryption.


def main():
    """ () -> NoneType

    Perform the encryption using the deck from a file called DECK_FILENAME and
    the messages from a file called MSG_FILENAME. If MODE is 'e', encrypt;
    otherwise, decrypt.
    """
    deck_file = open(DECK_FILENAME, 'r')
    message_file = open(MSG_FILENAME, 'r')
    card_list = cipher_functions.read_deck(deck_file)
    message_list = cipher_functions.read_messages(message_file)
    messages = cipher_functions.process_messages(card_list, message_list, MODE)
    for the_message in messages:
        print(the_message)
main()
