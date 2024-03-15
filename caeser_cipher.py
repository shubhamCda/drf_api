from art import logo

print(logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_txt, shift_amnt):
    cipher_text_encrypt = ""
    for letter in plain_txt:
        position = alphabet.index(letter)
        new_position = position + shift_amnt
        new_letter = alphabet[new_position]
        cipher_text_encrypt += new_letter
    print(f"The encoded text is : {cipher_text_encrypt}")    
    

def decrypt(plain_text, shift_amnt):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position - shift_amnt
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The decoded text is : {cipher_text}")    
    

if direction == 'encode':
    encrypt(plain_txt=text, shift_amnt=shift)
else:
    decrypt(plain_text=text, shift_amnt=shift)