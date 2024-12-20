# Shift is a length of last word
alphabet_upper = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
alphabet_lower = [chr(i) for i in range(ord('a'), ord('z') + 1)]

def caesar_cipher(word, shift):
    result = ''
    for char in word:
        if char in alphabet_upper:
            index = alphabet_upper.index(char)
            new_index = (index + shift) % len(alphabet_upper)
            result += alphabet_upper[new_index]
        elif char in alphabet_lower:
            index = alphabet_lower.index(char)
            new_index = (index + shift) % len(alphabet_lower)
            result += alphabet_lower[new_index]
        else:
            result += char
    return result


def encrypt_text(text):
    words = text.split()
    encrypted_words = []
    
    for word in words:
        # Remove punctuation from the word before applying the shift
        clean_word = ''.join([char for char in word if char.isalpha()])
        shift = len(clean_word)  # The shift is the length of the word
        print(shift)
        encrypted_word = caesar_cipher(clean_word, shift)
        
        # Reattach punctuation to the encrypted word
        encrypted_index = 0
        encrypted_word_with_punctuation = ''
        for char in word:
            if char.isalpha():
                encrypted_word_with_punctuation += encrypted_word[encrypted_index]
                encrypted_index += 1
            else:
                encrypted_word_with_punctuation += char
        
        encrypted_words.append(encrypted_word_with_punctuation)
    
    return ' '.join(encrypted_words)


# Input text to encrypt
text = input("Enter text to encode: ")
encrypted_text = encrypt_text(text)
print(f"Encrypted text: {encrypted_text}")




#           You say shift
# print("Welcom to Caesar cipher")
#
# eng_upper = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
# eng_lower = [chr(i) for i in range(ord('a'), ord('z') + 1)]
# rus_upper = [chr(i) for i in range(ord("А"), ord("Я") + 1)]
# rus_lower = [chr(i) for i in range(ord("а"), ord("я") + 1)]
#
# eng = eng_upper + eng_lower
# rus = rus_upper + rus_lower
#
# shift = int(input("Enter shift encode (n) or decode (-n): "))
#
# language = input("Choose language (rus / eng): ")
# if language == 'eng':
#     alphabet_upper = eng_upper
#     alphabet_lower = eng_lower
# elif language == 'rus':
#     alphabet_upper = rus_upper
#     alphabet_lower = rus_lower
# else:
#     print("Invalid language selected.")
#     exit()
#
# text = input("Enter the text to encode or decode: ")
#
# result = ''
# for char in text:
#     if char in alphabet_upper:
#         # Uppercase letter
#         index = alphabet_upper.index(char)
#         new_index = (index + shift) % len(alphabet_upper)
#         result += alphabet_upper[new_index]
#     elif char in alphabet_lower:
#         # Lowercase letter
#         index = alphabet_lower.index(char)
#         new_index = (index + shift) % len(alphabet_lower)
#         result += alphabet_lower[new_index]
#     else:
#         # Non-alphabetical characters remain unchanged
#         result += char
#
# print(f"Result: {result}")