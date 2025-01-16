import string

def caesar_encrypt(message, key):
    
    # Calcula o deslocamento no alfabeto
    shift = key % 26
    
    # Essa é a parte que vai mapear cada letra do alfabeto original para a nova posição na cifra.
    cipher = str.maketrans(string.ascii_lowercase,string.ascii_lowercase[shift:]+string.ascii_lowercase[:shift])
    # Coloca todas as letras da mensagem em minúsculo e aplica a tradução feita
    encrypted_message = message.lower().translate(cipher)
    
    return encrypted_message

def caesar_decrypt(encrypted_message,key):
    # Simplesmente desfazer a criptografia, calculando a re-alocação das letras para o alfabeto original.
    shift = 26-(key%26)
    # Utiliza o cálculo acima para colocar as letras nos locais originais novamente
    cipher = cipher = str.maketrans(string.ascii_lowercase,string.ascii_lowercase[shift:]+string.ascii_lowercase[:shift])

    # Traduz a mensagem criptografada de volta para a original.
    message = encrypted_message.translate(cipher)
    return message


    