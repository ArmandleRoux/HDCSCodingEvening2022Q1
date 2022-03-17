"""Function that does a basic character check through a dictionary 
and replaces the corresponding characters from letters to morse code"""
def to_morse(sentence):
    morse_dict = {}  
    with open("morse.txt", "r") as morse_file:
        for line in morse_file:
            data = line.split(", ")
            morse_dict[data[0]] = data[1].replace("\n", "")
    morse_sentence = ""
    for char in sentence:
        if char == " ":
            morse_sentence += "/ "
        else:
            morse_sentence += morse_dict[char] + " " 
    return morse_sentence


"""Function that does a basic character check through a dictionary 
and replaces the corresponding characters from morse code to letters"""
def morse_to_normal(sentence):
    morse_dict = {}  
    with open("morse.txt", "r") as morse_file:
        for line in morse_file:
            data = line.split(", ")
            morse_dict[data[1].replace("\n", "")] = data[0]
    normal_sentence = ""
    morse_sentence = sentence.split(" ")
    for char in morse_sentence:
        if char == "/":
            normal_sentence += " "
        else:
            normal_sentence += morse_dict[char]
    return normal_sentence


"""Infite loop that will break if user types '0' otherwise they 
can choose to encrypt a sentence to morse code or decrypt from 
morse code to normal letters"""  
while True:
    print("-"*80)
    print("Please select an option by entering the menu number:\n"
             "1. Encrypt to Morse Code\n"
            "2. Decrypt from Morse Code\n"
            "0. Exit")
    print("-"*80)
    user_choice = input(">")
    print("-"*80)
    if user_choice == "1":
        sentence = input("Please enter an sentence in all caps: \n>").upper()
        print("-"*80)
        print(f"Here is your sentence in morse code: \n{to_morse(sentence)}")
    elif user_choice == "2":
        sentence = input("Please enter a morse sentence: \n>").upper()
        print("-"*80)
        print(f"Here is your decoded sentence: \n{morse_to_normal(sentence)}")
    elif user_choice == "0":
        break
