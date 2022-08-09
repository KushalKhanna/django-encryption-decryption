# from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.query import QuerySet

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

from public_private_key.models import Messages

import binascii
import base64

def home(request):
    return render(request, "public_private_key/home.html", {"home_variable":"ENCRYPTION AND DECRYPTION OF DATA"})

def generate_keys(request):
    new_key = RSA.generate(4096)

    try:
        private_key = new_key.exportKey("PEM")
        public_key = new_key.publickey().exportKey("PEM")

        fd = open("private.pem", "wb")
        fd.write(private_key)
        fd.close()

        fd = open("public.pem", "wb")
        fd.write(public_key)
        fd.close()
    except:
        return HttpResponse("EXCEPTION OCCURED !")
    return HttpResponse("KEYS GENERATED SUCCESSFULLY !")

def get_public_key(request):

    f = open("public.pem", "r")
    if f.mode == 'r':
       contents = f.read()
       # print(contents)
    return HttpResponse(contents)

def encrypted_text(request):
    msg1 = "HIRE ME ! ;)"

    msg = bytes(msg1, 'utf-8')
    key = RSA.import_key(open('public.pem').read())
    cipher = PKCS1_OAEP.new(key)
    ciphertext = cipher.encrypt(msg)

    myB64e = base64.b64encode(ciphertext)

    newMessage = Messages.objects.get_or_create(message=myB64e)[0]
    newMessage.save()

    return HttpResponse(myB64e)

def decrypted_text(request):

    encodedText1 = Messages.objects.last().message
    encodedText = base64.b64decode(encodedText1)
    print(type(encodedText))
    print(encodedText)

    key = RSA.import_key(open('private.pem').read())
    cipher = PKCS1_OAEP.new(key)
    plaintext = cipher.decrypt(encodedText)
    return HttpResponse(plaintext)


# IGNORE BELOW

    # ENCRYPTION
    # key = RSA.import_key(open('public.pem').read())
    # cipher = PKCS1_OAEP.new(key)
    # ciphertext = cipher.encrypt(message)
    # print(ciphertext)

    # allMessages = QuerySet.reverse()[0]
    # allMessages = Messages.objects.values_list('message', flat=True)
    # arr_list = []
    # for i in allMessages:
    # DECRYPTION
        # print(i)
        # arr_list.append(i)
        # decoded_base64_str = base64.b64decode(i)
        # b64_string += "=" * ((4 - len(b64_string) % 4) % 4)
        # decoded_base64_str = base64.b64decode(i * (-len(i) % 4))
        # print(decoded_base64_str)
        # key = RSA.import_key(open('private.pem').read())
        # cipher = PKCS1_OAEP.new(key)
        # plaintext = cipher.decrypt(i)
        # print(plaintext)
        # arr_list.append(plaintext + "; ")
        # print (plaintext.decode("utf-8"))
    # return HttpResponse("plaintext")
    # # pub_key = get_text(request)
    # encryptor = PKCS1_OAEP.new(pub_key)
    # encrypted = encryptor.encrypt(msg)
    # # return render(request, "public_private_key", context=encrypted)
    # return HttpResponse("Encrypted:",binascii.hexlify(encrypted))
# def decrypt_try_func(request):
#     default_length = 4096/8
#     encrypt_str = str(data["content"])
#     sign_str = str(data["sign"])
#     try:
#         allMessages = Messages.objects.values_list('message', flat=True)
#
#         for i in allMessages:
#             key = RSA.import_key(open('private.pem').read())
#             # rsa_private_key = RSA.importKey(private_key)
#             encrypt_byte = base64.b64decode(i)
#             length = len(encrypt_byte)
#             cipher = PKCS115_Cipher(key)
#             if length < default_length:
#                 decrypt_byte = cipher.decrypt(encrypt_byte, 'failure')
#             else:
#                 offset = 0
#                 res = []
#                 while length - offset > 0:
#                     if length - offset > default_length:
#                         res.append(cipher.decrypt(encrypt_byte[offset: offset +
#                             default_length], 'failure'))
#                     else:
#                         res.append(cipher.decrypt(encrypt_byte[offset:], 'failure'))
#                     offset += default_length
#                 decrypt_byte = b''.join(res)
#             decrypted = decrypt_byte.decode()
#     return "Hello"

# def decryption_function():
#     decryptor = PKCS1_OAEP.new(keyPair)
#     decrypted = decryptor.decrypt(encrypted)
#     print('Decrypted:', decrypted)


# if __name__ == '__main__':
#     pub_key = public_key_generate()
#     public_key_display(pub_key)
#     # print("PUBLIC KEY: " + pub_key)
#     pri_key = private_key_generate()
#     private_key_display(pri_key)
#
#     encryption_function(pub_key)
