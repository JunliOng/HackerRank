import math

s = 'abcdefghijklmnopqs'
def encryption(s):
    stringlength = len(s)

    rowlength = math.sqrt(stringlength)
    rowlength_int = int(rowlength)

    decrypted = []

    if rowlength.is_integer()==True:
        for i in range(rowlength_int):
            decrypted.append(0)
            
        for index in range(rowlength_int):
            decrypted[index] = ''
            for verticalindex in range(rowlength_int):
    #            print("horizontal index is " + str(index))
    #            print("vertical index is " + str(verticalindex))
    #            print(rowlength_int)
                                
                decrypted[index] = decrypted[index] + (s[index + verticalindex * rowlength_int])


    decryptedvalue = ''

    for i in decrypted:
        decryptedvalue = decryptedvalue + i + " "

    else:

        for i in range(rowlength_int + 1):
            decrypted.append(0)

        for index in range(rowlength_int + 1):
            decrypted[index] = ''

            for verticalindex in range(rowlength_int+1):
    #                print(str(index +verticalindex * rowlength_int))
    #                print("adding " + s[index +verticalindex * rowlength_int])

    #                print("checker is " + str(index + verticalindex*rowlength_int))
    #                print("max index of string is " + str(stringlength))

                    if index + verticalindex * (rowlength_int+1) >= stringlength:
                        break
                    else:
                        decrypted[index] = decrypted[index] + (s[index + verticalindex * (rowlength_int+1)])

    decryptedvalue = ''

    for i in decrypted:
        decryptedvalue = decryptedvalue + i + " "
    
    return decryptedvalue

print(encryption(s))
