from cryptography.fernet import Fernet

#Generates a key and save it into a file
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
        print('Your new secret key is: ' + key.decode('utf-8'))

#Load the previously generated key
def load_key():
    return open("secret.key", "rb").read()

#Encrypts a message
def encrypt_message(message):
    key = load_key()
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    print('-> ' + encrypted_message.decode('utf-8'))

#Decrypts an encrypted message
def decrypt_message(encrypted_message):
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    print('-> ' + decrypted_message.decode())

def init():
    usage = open('usage.txt', 'r').read()
    select = input(usage)

    try:
        if (select not in ['1', '2', '3']):
            return print('Please, enter a valid command!')
        
        if (select == '1'):
            return generate_key()
            
        message = input('Message for encrypt or decrypt: ')

        if (select == '2'):
            return encrypt_message(message)
        if (select == '3'):
            return decrypt_message(f'{message}'.encode('utf-8'))
    except:
        print('An error has occurred!')

init()

