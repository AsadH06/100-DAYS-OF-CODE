
def caesar_cipher():
    def encode(m, s):
        message_encode = ""
        for letter in m:
            if letter in alphabets:
                ind = alphabets.index(letter)
                shift_ind = (ind + s) % len(alphabets)
                message_encode += alphabets[shift_ind]
            else:
                message_encode += letter
        return message_encode
    def decode(m, s):
        message_decode = ""
        for letter in m:
            if letter in alphabets:
                ind = alphabets.index(letter)
                shift_ind = (ind - s) % len(alphabets)
                message_decode += alphabets[shift_ind]
            else:
                message_decode += letter
        return message_decode


    user_choice = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    message = input("Type your message: ").lower()
    shift = int(input("Type your shift number: "))
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    if user_choice == "encode":
        encoded_message = encode(message, shift)
        print(f"Here's the encoded result: {encoded_message}")
    elif user_choice == "decode":
        decoded_message = decode(message, shift)
        print(f"Here's the decoded result: {decoded_message}")
    else:
        print("Enter a valid option!")
        caesar_cipher()

    user_choice_continue = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
    if user_choice_continue == 'yes':
        caesar_cipher()


caesar_cipher()

"""
Sure! Let's take z with a shift of 2:

z is at index 25
25 + 2 = 27
But index 27 doesn't exist in a 26 letter list!
27 % 26 = 1 → which is b ✅

So it wraps around naturally. Now for decode, take b with shift of 2:

b is at index 1
1 - 2 = -1
-1 % 26 = 25 → which is z ✅

"""
