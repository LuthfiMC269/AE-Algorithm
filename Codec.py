def atbash(convertto):
    result = ""
    for char in convertto:  # atbash cipher algorithm
        if char.isalpha():
            if char.isupper():
                result += chr(90 - (ord(char) - 65))
            elif char.islower():
                result += chr(122 - (ord(char) - 97))
        else:
            result += char
    return result

def checkkey(keyinput: int):
    if len(str(keyinput)) == 16:
        key = [int(digit) for digit in str(keyinput)]
        idcode = key[15]
        print("id code dari kunci:", idcode)
        key.pop()
        print("kunci tanpa id code:", key)
        for i in range(15):  # step 1 ngekali 2 setiap indeks genap
            if i % 2 == 0:
                key[i] *= 2
        for i, j in zip(range(15), key):  # step 2 kalo lebih dri 10, dua digitnya ditambah
            if j >= 10:
                key[i] = (j // 10) + (j % 10)
        keysum = [sum(key)] # step 3 jumlahin semua angkanya
        if sum(key) >= 10:
            keysum.remove(sum(key))
            keysum.append(sum(key) // 10)
            keysum.append(sum(key) % 10)
        if idcode == 10 - keysum[1]:
            print("Code diterima!")
            return key
    else: print("CODE INVALID!")

def coder(keyinput, textinput):
    validkey = checkkey(keyinput)
    print("Valid key:",validkey)
    textbash = list(atbash(textinput)) #convert atbash text jadi list per character
    # print(textbash)
    # endtext = []
    # for i in range(textbash.__len__()):
    # endtext.append(chr(ord(textbash[i])))
    # print(endtext)

kunci = 4104710160500832 #PlaceHolder Key
huruf = "Hello World!"
kunci2 = 5393710083348027
coder(kunci, huruf)
# print(chr(ord(huruf)+1))
# print(chr(ord(text[0])+key[0]))