def atbash(convertto): #Convert input text jadi atbash cipher text
    result = ""
    for char in convertto:
        if char.isalpha():
            if char.isupper():
                result += chr(90 - (ord(char) - 65))
            elif char.islower():
                result += chr(122 - (ord(char) - 97))
        elif char.isdigit():
            result += chr(57 - (ord(char) - 48))
        else:
            result += char
    return result

def checkkey(keyinput: int): #Validasi input key, sesuai sama yg ketentuan atau engga
    if len(str(keyinput)) == 16:
        r1_key = [int(digit) for digit in str(keyinput)]
        idcode = r1_key[15]
        print("id code dari kunci:", idcode)
        r1_key.pop()
        r2_key = []
        for i in range(15):  # step 1 ngekali 2 setiap indeks genap
            if i % 2 == 0:
                r2_key.append(r1_key[i] * 2)
            else:
                r2_key.append(r1_key[i])
        for i, j in zip(range(15), r2_key):  # step 2 kalo lebih dri 10, dua digitnya ditambah
            if j >= 10:
                r2_key[i] = (j // 10) + (j % 10)
        keysum = [sum(r2_key)] # step 3 jumlahin semua angkanya
        if sum(r2_key) >= 10:
            keysum.remove(sum(r2_key))
            keysum.append(sum(r2_key) // 10)
            keysum.append(sum(r2_key) % 10)
        if idcode == 10 - keysum[1]:
            print("Kunci diterima!")
            return r1_key, r2_key
        else:
            print("Kunci ditolak! periksa ulang kunci")
            return None, None
    else:
        print("Kunci ditolak! hanya menerima 16 digit kunci")
        return None, None

def coder(keyinput, textinput):
    r1_key , r2_key = checkkey(keyinput)
    try:
        for i, j in zip(range(15), r2_key):
            r2_key[i] = r2_key[i] * (-1)
    except TypeError:
        print("CODE INVALID! Process Stopped")
    else:
        print("Valid r1_key: "+ str(r1_key)+"\n"+"Valid r2_key: "+ str(r2_key))

    atbashtext = list(atbash(textinput)) #convert atbash text jadi list per character
    # print("Atbash Text:" +atbash(textinput))
    ciphertext = []
    printable_range = list(range(32, 127)) #range untuk Printable ASCII CODE
    printable_length = len(printable_range)
    for i, char in enumerate(atbashtext):
        # Geser maju r1_key
        forward_shift = r1_key[i % 15] #15 Hardcoded key_length
        current_pos = printable_range.index(ord(char))
        if forward_shift != 0:
            new_pos = (current_pos + forward_shift) % printable_length
            new_char = chr(printable_range[new_pos])
        else:
            new_char = char

        # Index r2_key berdasarkan pergerseran r1_key
        r2_index = (i + forward_shift) % 15 #15 Hardcoded key_length

        # Geser mundur dengan r2_key
        backward_shift = r2_key[r2_index]
        current_pos = printable_range.index(ord(new_char))
        if backward_shift != 0:
            new_pos = (current_pos + backward_shift) % printable_length
            new_char = chr(printable_range[new_pos])
        ciphertext.append(new_char)
    return ''.join(ciphertext)


kunci = 1562347319345834 #PlaceHolder Key
huruf = "01234 56789"
print("Ciphered Text: "+ coder(kunci, huruf))
