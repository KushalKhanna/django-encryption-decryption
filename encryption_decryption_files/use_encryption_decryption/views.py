from django.shortcuts import render
from cryptography.fernet import Fernet
from django.http import HttpResponse

# GENERATE NEW KEY
def generate_secret_key(request):
    try:
        key = Fernet.generate_key()
        with open("mykey.key", "wb") as mykey:
            key = mykey.write(key)
    except:
        return HttpResponse("EXCEPTION IN GENERATING SECRET KEY")
    return HttpResponse("KEY GENERATED SUCCESSFULLY")

# ENCRYPTION OF FILE
def encrypting_file(request):
    try:
        with open("mykey.key", "rb") as mykey:
            key = mykey.read()

        f = Fernet(key)

        with open("sensitive_info.csv", "rb") as original_file:
            original_content = original_file.read()

        encrypted_text = f.encrypt(original_content)

        with open("enc_sensitive_info", "wb") as encrypted_file:
            encrypted_file.write(encrypted_text)
    except:
        return HttpResponse("ERROR IN ENCRYPTING A FILE")
    return HttpResponse("FILE ENCRYPTED SUCCESSFULLY")

# DECRYPTION OF FILE
def decrypting_file(request):
    try:
        with open("mykey.key", "rb") as mykey:
            key = mykey.read()

        f = Fernet(key)
        
        with open("enc_sensitive_info", "rb") as encrypted_file:
            encrypted_text = encrypted_file.read()

        decrypted_text = f.decrypt(encrypted_text)

        with open("dec_sensitive_info", "wb") as decrypted_file:
            decrypted_text = decrypted_file.write(decrypted_text)
    except:
        return HttpResponse("ERROR IN DECRYPTING A FILE")
    return HttpResponse("FILE DECRYPTED SUCCESSFULLY")
