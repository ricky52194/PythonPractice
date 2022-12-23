#Caesar Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift, direction):
#Handle very large shifts - a shift of 26 lands back on the same letter - find out how many times it loops back to the same letter and then use the remainder to adjust index
  if shift > 26:
    shift = shift % 26
  #Encode Message
  if direction == 'encode':
    encrypted = ""
    #Account for spaces in text
    for letter in text:
      if letter == ' ':
        encrypted += " "
      else:
        #Adjust new index
        new_index = alphabet.index(letter) + shift
        if new_index > 25:
          encrypted += alphabet[new_index - 26]
        else:
          encrypted += alphabet[alphabet.index(letter) + shift]
    print(f"The encoded text is {encrypted}")
  #Decode Message
  else:
    decrypted = ""
    for letter in text:
      decrypted += alphabet[alphabet.index(letter) - shift]
    print(f"The decoded text is {decrypted}")

caesar(text, shift, direction)