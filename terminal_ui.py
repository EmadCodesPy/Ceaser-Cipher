from encryption_logic import encrypt_word, decrypt_word, encryption_key, decryption_key, find_index

def encrypt():
    word = input('What is the phrase you would like to encrypt: ')
    shift_num = find_index(word)
    phrase, index = encrypt_word(word, shift_num)
    key = encryption_key(index)
    print(f'Your encrypted phrase is: {phrase} \nYour encryption key is: {key}')

def decrypt():
    word = input('What is the phrase you would like to decrypt: ')
    key = int(input('What is your encryption key: '))
    index = decryption_key(key)
    phrase = decrypt_word(word, index)
    print(f'Your decrypted phrase is: {phrase}')

def main():
    func = input('What would you like to do? Encrypt(E), Decrypt(D): ')
    if func.upper() == 'E':
        encrypt()
    elif func.upper() == 'D':
        decrypt()
    else:
        print('Please enter a proper option.')

if __name__ == '__main__':
    main()
    