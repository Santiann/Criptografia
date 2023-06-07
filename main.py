def countVowels(word):
    vowels = "aeiou"
    return sum(1 for char in word.lower() if char in vowels)

def encrypt(word, key):
    encrypted_word = ""
    key_length = len(key)
    for i, char in enumerate(word):
        key_char = key[i % key_length]
        shift = ord(key_char.lower()) - ord('a') + 1 
        encrypted_char = chr((ord(char.lower()) - ord('a') + shift) % 26 + ord('a'))  
        encrypted_word += encrypted_char.upper() if char.isupper() else encrypted_char
    return encrypted_word

def decrypt(encrypted_word, key):
    decrypted_word = ""
    key_length = len(key)
    for i, char in enumerate(encrypted_word):
        key_char = key[i % key_length]
        shift = ord(key_char.lower()) - ord('a') + 1
        decrypted_char = chr((ord(char.lower()) - ord('a') - shift) % 26 + ord('a'))
        decrypted_word += decrypted_char.upper() if char.isupper() else decrypted_char
    return decrypted_word

# Ask the user for the word and key
word = input("Enter the word: ")
key = input("Enter the key: ")

# Encrypt the word using the key
encrypted_word = encrypt(word, key)
print("Encrypted word:", encrypted_word)

# Decrypt the word using the key
decrypted_word = decrypt(encrypted_word, key)
print("Decrypted word:", decrypted_word)

print(ord(word[0]))
print(ord(decrypted_word[0]))
