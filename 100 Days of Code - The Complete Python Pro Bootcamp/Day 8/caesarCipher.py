alphabet = 'abcdefghijklmnopqrstuvwxyz'
Type =input("type of 'encrypt' , type of 'decrypt'")
shift = int(input("enter a shift_key: "))
text=input("enter a message: ")

def encrypt(original_text,shift_key):
    output_text=""
    for char in original_text:
        new_position=alphabet.index(char)+shift_key


