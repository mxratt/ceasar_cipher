import time
import random
import os

# set console size
size = 'mode 100,8'
os.system(size)

# default data collection
output = ""
cipher = "cipher.log"
dice = int()
value = int(1)
step = 0
extra = 0
key = []
OTP = []
OTP_request = ""
alp = [
        "A",  # 0
        "B",  # 1
        "C",  # 2
        "D",  # 3
        "E",  # 4
        "F",  # 5
        "G",  # 6
        "H",  # 7
        "I",  # 8
        "J",  # 9
        "K",  # 10
        "L",  # 11
        "M",  # 12
        "N",  # 13
        "O",  # 14
        "P",  # 15
        "Q",  # 16
        "R",  # 17
        "S",  # 18
        "T",  # 19
        "U",  # 20
        "V",  # 21
        "W",  # 22
        "X",  # 23
        "Y",  # 24
        "Z",  # 25
        "A",  # 0
        "B",  # 1
        "C",  # 2
        "D",  # 3
        "E",  # 4
        "F",  # 5
        "G",  # 6
        "H",  # 7
        "I",  # 8
        "J",  # 9
        "K",  # 10
        "L",  # 11
        "M",  # 12
        "N",  # 13
        "O",  # 14
        "P",  # 15
        "Q",  # 16
        "R",  # 17
        "S",  # 18
        "T",  # 19
        "U",  # 20
        "V",  # 21
        "W",  # 22
        "X",  # 23
        "Y",  # 24
        "Z"   # 25
]

# create or overwrite output.txt
file = open(cipher, "w")
file.writelines("")
file.close()

# ask for input
word = input("input: ").upper()  # convert input to uppercase
length = len(word)  # get length of input in total character sum
# ask if this encryption will have a One-Time-Pad included, applying a shift key to the original key
while OTP_request != "y" or "n":
    OTP_request = input("one time pad(y/n): ").lower()
    if OTP_request == "y":
        OTP_request = True
        break
    elif OTP_request == "n":
        OTP_request = False
        break
    else:
        print("\nInvalid Input!\n")

while step != length:  # each loop increases step by 1. once step is equal to the length of the input the loop breaks
    output = word[step]  # splits input into characters, proceeds to the next char each loop
    dice = random.randint(1, 26)  # roll the dice, gives back a pseudo-random number
    shift = random.randint(1, 73)  # shift that generates the one time key, and applies to the original key

    # if output isn't in the alp list it'll pass as itself, unencoded
    if output not in alp and extra != length:
        output = output
        extra += 1
        continue
    # check which letter = output, then applies the cipher
    elif output == alp[0]:
        output = alp[abs(0 + dice)]
    elif output == alp[1]:
        output = alp[abs(1 + dice)]
    elif output == alp[2]:
        output = alp[abs(2 + dice)]
    elif output == alp[3]:
        output = alp[abs(3 + dice)]
    elif output == alp[4]:
        output = alp[abs(4 + dice)]
    elif output == alp[5]:
        output = alp[abs(5 + dice)]
    elif output == alp[6]:
        output = alp[abs(6 + dice)]
    elif output == alp[7]:
        output = alp[abs(7 + dice)]
    elif output == alp[8]:
        output = alp[abs(8 + dice)]
    elif output == alp[9]:
        output = alp[abs(9 + dice)]
    elif output == alp[10]:
        output = alp[abs(10 + dice)]
    elif output == alp[11]:
        output = alp[abs(11 + dice)]
    elif output == alp[12]:
        output = alp[abs(12 + dice)]
    elif output == alp[13]:
        output = alp[abs(13 + dice)]
    elif output == alp[14]:
        output = alp[abs(14 + dice)]
    elif output == alp[15]:
        output = alp[abs(15 + dice)]
    elif output == alp[16]:
        output = alp[abs(16 + dice)]
    elif output == alp[17]:
        output = alp[abs(17 + dice)]
    elif output == alp[18]:
        output = alp[abs(18 + dice)]
    elif output == alp[19]:
        output = alp[abs(19 + dice)]
    elif output == alp[20]:
        output = alp[abs(20 + dice)]
    elif output == alp[21]:
        output = alp[abs(21 + dice)]
    elif output == alp[22]:
        output = alp[abs(22 + dice)]
    elif output == alp[23]:
        output = alp[abs(23 + dice)]
    elif output == alp[24]:
        output = alp[abs(24 + dice)]
    elif output == alp[25]:
        output = alp[abs(25 + dice)]
    # if user wants an OTP code, this applies the code shift to the original key
    if OTP_request:
        dice += shift  # add shift
    # this prevents characters that aren't letters from being keyed
    if output in alp:
        key.append(abs(dice))  # add the newest key list to key list (this gets printed after the loop finishes)
        if OTP_request:
            OTP.append(abs(shift))
    print(output, end="")
    file = open(cipher, "a")
    file.writelines(output)
    step += 1
file.write("\n{}".format(key))
if OTP_request:
    file.write("\n{}".format(OTP))
file.close()
print("\n[", *key, "]")
if OTP_request:
    print("[", *OTP, "]")
else:
    print("")
print("check cipher.log")
time.sleep(300)
