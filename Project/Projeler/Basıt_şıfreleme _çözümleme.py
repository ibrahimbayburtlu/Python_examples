def encrypt(text,value,output=""):
    for char in text:
        output="{} {}".format(output,chr(ord(char)+value))
        return output

def decrypt(text, value, output=""):
    for char in text:
        output = "{}{}".format(output, chr(ord(char) - value))
    return output

i=int(input("Increment value:"))
text=input("Type your text:")
print("Encrypted text:{}".format(encrypt(text,i)))

text=input("\nType for decrypt:")
print("Decryted text:{}".format(decrypt(text,i)))