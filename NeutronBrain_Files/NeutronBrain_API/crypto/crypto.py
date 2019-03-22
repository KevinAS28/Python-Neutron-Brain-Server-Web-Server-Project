from Crypto.Cipher import AES

def Padding(data, padder=b"\0"):
    if (type(data)!=bytes):
        try:
            data = data.encode("utf-8")
        except:
            pass
    while ((len(data)%16)!=0):
        data += padder
    return data
def Depadding(data, depadder=b"\0"):
    return data.rstrip(depadder)

AES_PASSWORD = """F<{Z[C?AY)L7!Yc@"""
AES_IV = """nrB27PNZTnn-N^dR"""

def Encrypt_AES(data):
    aes = AES.new(AES_PASSWORD, AES.MODE_CBC, AES_IV)
    return aes.encrypt(Padding(data))

def Decrypt_AES(data):
    aes = AES.new(AES_PASSWORD, AES.MODE_CBC, AES_IV)
    return Depadding(aes.decrypt(data))

def AFD(file, result=""): #AES File Decrypt
    if not (len(result)):
        result=file.rstrip(Enc_Extension)
    Check_File_Internal(result)
    with open(file, "rb") as baca:
        with open(result, "wb") as tulis:
            tulis.write(Decrypt_AES(baca.read()))

def AFE(file, result=""): #AES File Encrypt
    if not len(result):
        result=file+Enc_Extension
    Check_File_Internal(result)
    with open(file, "rb") as baca:
        with open(result, "wb") as tulis:         
            tulis.write(Encrypt_AES(baca.read()))

if __name__=="__main__":
    print(Decrypt_AES(Encrypt_AES("Encryption and Decryption Works!")))
    