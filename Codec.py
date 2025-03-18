def atbash(convertto): #Convert input text menggunakan atbash algorithm
    result = ""
    for char in convertto:
        if char.isalpha():
            if char.isupper():
                result += chr(90 - (ord(char) - 65))
            elif char.islower():
                result += chr(122 - (ord(char) - 97))
        elif char.isdigit():
            result += chr(57 - (ord(char) - 48))
        #elif char.isspace():
            #result += chr(32) #known bugs, spasi kadang ga kerender benar, sementara pakai underscore (_)
            #fixed, check on decoder section
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

def encoder(keyinput, textinput):
    r1_key , r2_key = checkkey(keyinput) #ngecek validity kunci
    try:
        for i, j in zip(range(15), r2_key):
            r2_key[i] = r2_key[i] * (-1)
    except TypeError:
        print("CODE INVALID! Process Stopped")
    else:
        pass

    atbashtext = list(atbash(textinput)) #convert atbash text jadi list per character
    ciphertext = []
    printable_range = list(range(32, 127)) #range untuk Printable ASCII CODE
    #printable_range.append(0)
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


def decoder(keyinput, cipherinput):
    r1_key , r2_key = checkkey(keyinput) #ngecek validity kunci
    try:
        for i, j in zip(range(15), r1_key):
            r1_key[i] = r1_key[i] * 1
    except TypeError:
        print("CODE INVALID! Process Stopped")
    else:
        pass

    decodedtext = []
    for i , char in enumerate(cipherinput):# nyari tau step r1 terakhir waktu encoding
        r1_index = i % 15
        r2_index = (i + r1_key[r1_index]) % 15 # nyari index r2 berdasarkan posisi dari r1_key[r1_index]
        #print(r1_key[r1_index], r2_key[r2_index], cipherinput[i]) #Ngecek setiap pasangan value r1r2 dan input[i]
        char = chr(ord(cipherinput[i])+r2_key[r2_index])
        char = chr(ord(char)-r1_key[r1_index])
        if char == chr(127):
            #pass
            decodedtext.append(" ")
        else:
            decodedtext.append(char)
        #print(ord(char))
    decodedtext = ''.join(decodedtext)
    plaintext = atbash(decodedtext)
    return plaintext

def main():
    # Example usage:
    kunci = 1562347319345834  # Example Key
    huruf = ("Sudah seminggu ku makan telur, telur ceplok dadar dan omelete")  # Example Text

    print("Ingin Encrypt atau Decrypt?")
    input1 = input("1 untuk Encrypt, 2 untuk Decrypt")
    if input1 == "1":
        print("Masukkan Kunci khusus (Bisa generate di file generator.py)")
        kunci = input("Simpan baik baik kode ini!")
        checkkey(kunci)
        huruf = input("Masukkan huruf untuk di Encrypt")
        encodedtext = encoder(kunci, huruf)
        print("Ciphered Text: " + encodedtext)
    elif input1 == "2":
        print("Masukan Kunci khusus yang dipakai saat generate encoded text")
        kunci = input()
        checkkey(kunci)
        huruf = input("Masukkan huruf untuk di Decrypt")
        print("Ciphered Text: " + decoder(kunci, huruf))

main()
pause = input()