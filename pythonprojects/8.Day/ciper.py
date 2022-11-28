alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Please input your text\n").lower()
shift = int(input("Type the shift number:\n"))

# def encrypt_func(plain_text, shift_amount):
#     list_plain = list(plain_text)
#     cipher_text = ""
#     for i in range(0, len(list_plain)):
#         list_plain[i] = alphabet[alphabet.index(list_plain[i])+shift_amount]
#     cipher_text = ''.join(list_plain)
#     print(cipher_text)
#
# def decrypt_func(crypt_text, shift_count):
#     list_crypt = list(crypt_text)
#     plain_text = ""
#     for i in range(0, len(list_crypt)):
#         list_crypt[i] = alphabet[alphabet.index(list_crypt[i])-shift_count]
#     plain_text = ''.join(list_crypt)
#     print(plain_text)



#
# if direction == "encode":
#     encrypt_func(text,shift)
# elif direction == "decrypt":
#     decrypt_func(text, shift)

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        end_text += alphabet[alphabet.index(letter) + shift_amount]
    print(f"Here is the {direction}d result: {end_text}")


caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
