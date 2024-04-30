from cryptography.fernet import Fernet


# ouverture de la clé
with open("clefs.key",'rb') as f:
    clef = f.read()

# ouverture de l'objet à decoder
with open("WhatsApp Image 2023-09-06 à 23.57.20.jpg",'rb') as f:
    photo = f.read()


# decryptage de l'objet
unlock = Fernet(clef)
unlockPic = unlock.decrypt(photo)

# with open("WhatsApp Image 2023-09-06 à 23.57.20.jpg") as pf:
with open("decrypter002.jpg", 'wb') as pf:
    dec = pf.write(unlockPic)
    
