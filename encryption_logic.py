#Encyption using ceaser cypher

def find_index(word):
    if len(word) <= 27:
        return len(word)
    else:
        return len(word)%27

def encrypt_word(word, index):
    alph = 'abcdefghijklmnopqrstuvwxyz '
    new_word = ''
    curr = 0
    for letter in word:
        if letter not in alph:
            raise ValueError('Please enter something from the alphabet')
        for i in alph:
            if i.lower() == letter.lower():
                if curr + index >= 27:
                    new_word+= alph[(curr+index-27)]
                else:
                    new_word+= alph[curr+index]
                curr = 0
                break
            else:
                curr += 1
    return new_word, index

def decrypt_word(word, index):
    alph = 'abcdefghijklmnopqrstuvwxyz '
    new_word = ''
    curr = 0
    for letter in word:
        for i in alph:
            if i.lower() == letter.lower():
                new_word += alph[curr-index]
                curr = 0
                break
            else:
                curr += 1
    return new_word

def encryption_key(index):
    key = index * 123456789 * 987654321
    return int(key)

def decryption_key(index):
    key = index / (123456789 * 987654321)
    return int(key)

