# my_list = []
# for i in range(0,5):
#     my_list.append(int(input()))
# print("Finish of the input")
# shift_num = int(input())
#
# while shift_num > 0:
#     temp_value = my_list.pop()
#     my_list.insert(0, temp_value)
#     shift_num -= 1
# else:
#     while shift_num < 0:
#         temp_value = my_list.pop()
#         my_list.append(temp_value)
#         shift_num += 1
# print (my_list)


# def select_method():
#     question = input("Select method coding (c) or decoding (d): ")
#     question = question.lower()
#     if question == "c":
#         coding(question)
#     elif question == "d":
#         decoding(question)
#     else:
#         print("Invalid choice!")
#
# def coding(question):
#     if question == "c":
#         data_user = list(input("Enter you string: "))
#         shift = int(input("How many to shift the string: "))
#         for x in data_user:
#             a = int(ord(x))
#             b = a+shift
#             print(str(chr(b)), end="")
#
# def decoding(question):
#     if question == "d":
#         data_user = list(input("Enter your string: "))
#         shift = int(input("How many to shift the string: "))
#         for x in data_user:
#             a = int(ord(x))
#             b = a - shift
#             print(str(chr(b)),end = "")
#
# select_method()
message = "This is my secret message"
key = 13
mode = "encrypt"
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
translated = ""
message = message.upper()

for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)  # get the number of the symbol
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
        num = num - key
    if num >= len(LETTERS):
        num = num - len(LETTERS)
    elif num < 0:
        num = num + len(LETTERS)
    translated = translated + LETTERS[num]
else:
    translated = translated + symbol
print(translated)
pyperclip.copy(translated)