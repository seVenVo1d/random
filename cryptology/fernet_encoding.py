from cryptography.fernet import Fernet


key = Fernet.generate_key()
encryption_type = Fernet(key)


def encrypt_script(filePATH):
    """
    Encrypting the python script with fernet for a given file path

    Args:
        file_name [str]: the name of the python script that is
        going to be encrypted
    """
    with open(filePATH, 'rb') as f:
        data = f.read()

    with open(filePATH + 'f', 'wb') as f:
        f.write(encryption_type.encrypt(data))


def read_binary_script(encfilePATH):
    """
    Reading the binary string for the use of the exec function.
    """
    with open(encfilePATH, 'rb') as f:
        data = f.read()
        return data


filePATH = 'hello.py'   # It can be full or relative path
encfilePATH = 'hello.pyf'    # It can be full or relative path

# Encoding the python script
encrypt_script(filePATH)

# Reading the encoded python script
encrypted_script = read_binary_script(encfilePATH)

# Decrypting the python script
decrypted_script = encryption_type.decrypt(encrypted_script)

# Executing the code
exec(decrypted_script)
