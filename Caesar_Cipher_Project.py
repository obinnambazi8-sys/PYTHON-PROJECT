
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(originaltext,shiftamount,encode_or_decode):
    decrypted_letter = ''
    if encode_or_decode == "decode":
        shiftamount *= -1
    for letter in originaltext:
        if letter in alphabet:
            decryptedposition = alphabet.index(letter) + shiftamount
            decryptedposition %=len(alphabet)
            decrypted_letter += alphabet[decryptedposition] 
        else:
            decrypted_letter += letter
    print(f"Here is the encoded text: {decrypted_letter}")

should_continue =True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(originaltext=text,shiftamount=shift,encode_or_decode=direction)

    go_again=input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n ").lower().strip()
    if go_again == 'no':
        should_continue = False
        print("Goodbye")