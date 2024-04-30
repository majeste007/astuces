from cryptography.fernet import Fernet

try:
    cle = Fernet.generate_key()
    with open('clefs.key','wb') as f:
        f.write(cle)
    fernet = Fernet(cle)

    with open("WhatsApp Image 2023-09-06 à 23.57.20.jpg",'rb') as f:
        photo = f.read()

    lock = fernet.encrypt(photo)
    with open('WhatsApp Image 2023-09-06 à 23.57.20.jpg','wb') as lp:
        lp.write(lock)
    print("Photo verrouiller")
except Exception:
    print("Une erreur s'est produite")