from cryptography.fernet import Fernet

def crypter(msg_a_crypter, clef):
    f = Fernet(clef)
    texte_a_crypter = f.encrypt(msg_a_crypter.encode())
    return texte_a_crypter

def decrypter(msg_a_decrypter, clef):
    f = Fernet(clef)
    texte_a_decrypter = f.decrypt(msg_a_decrypter).decode()
    return texte_a_decrypter

texte = "NDZOKO Pascal stephene"
clef  = Fernet.generate_key()
texte_crypter = crypter(texte, clef)
print("texte Crypté : ",texte_crypter)
fichier = "message.lock"
with open(file=fichier,mode='wb') as fc:
    fc.write(texte_crypter)
    print("Enregistré avec succès dans message.lock")
    fc.close()
    
texte_decrypter = decrypter(texte_crypter, clef)
print("texte decrypté : ",texte_decrypter)