import sys
"""Caesar Cipher"""

try:
    import pyperclip  # pyperclip copies text to the clipboard.
except ImportError:
    pass  # If pyperclip is not installed, do nothing. It's no big deal

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('\n**Caesar Cipher - ex: a key of 2 means A is encrypted into C, etc,.')

# Let user enter if they are encrypting or decrypting
while True:
    print('Do you want to (e)ncrypt, (d)ecrypt, or (q)uit?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    elif response.startswith('q'):
        sys.exit('Goodbye!')
    print('Please enter the letter e or d.')

# let user enter the key to use
while True: # keep asking until user enters a valid key
    maxKey = len(SYMBOLS) - 1
    print('Please enter the key (0 to {}) to use.'.format(maxKey))
    response = input('> ').upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

# let the user enter the message to encrypt/decrypt
print('Enter the message to {}'.format(mode))
message = input('> ')

# caesar cipher only work on uppercase letters:
message = message.upper()

# store the encrypted/decrypted form of the message:
translated = ''

# encrypt/decrypt each symbol in the message:
for symbol in message:
    if symbol in SYMBOLS:
        # get the encrypted(or decrypted) number for this symbol.
        num = SYMBOLS.find(symbol)  # get the number of the symbol.
        if mode == 'encrypt':
            num += key
        elif mode == 'decrypt':
            num -= key

        #  handle the wrap-around if number is larger than the length of SYMBOLS or less than 0
        if num >= len(SYMBOLS):
            num -= len(SYMBOLS)
        elif num < 0:
            num += len(SYMBOLS)

        # add encrypted/decrypted number's symbol to translated
        translated += SYMBOLS[num]
    else:
        # just add the symbol without encrypting/decrypting
        translated += symbol

# Display the encrypted/decrypted string to the screen:
print(translated)


try:
    pyperclip.copy(translated)
    print('Full {}ed text copied to the clilpboard'.format(mode))
except:
    pass  # do nothing if pyperclip wasn't installed


