from typing import Tuple
import customtkinter as ctk
import qrcode
from PIL import Image, ImageTk
from tkinter.messagebox import *
from tkinter.filedialog import *
import pathlib
import os

class App(ctk.CTk):
    
    def __init__(self, ):
        super().__init__()
        self.title("Convertisseur")
        self.geometry("485x460")
        self.resizable(False, False)
        
        self.main_area = ctk.CTkFrame(self, fg_color="gray",corner_radius=0, width=485, height=150)
        self.main_area.place(x=0, y=0)
        
        self.lbl_title = ctk.CTkLabel(self.main_area, corner_radius=0, text="Generateur de QRCODE", font=ctk.CTkFont(size=24))
        self.lbl_title.place(x=124, y=15)
        
        self.lbl_subject = ctk.CTkLabel(self.main_area, corner_radius=0, text="Saisissez un contenu", font=ctk.CTkFont(size=14))
        self.lbl_subject.place(x=130, y=70)
        
        self.entry_subject = ctk.CTkEntry(self.main_area, width=270, corner_radius=0, font=ctk.CTkFont(size=13))
        self.entry_subject.place(x=40, y=100)
        
        self.btn_gen = ctk.CTkButton(self.main_area,text="Génerer",width=100, corner_radius=0, font=ctk.CTkFont(size=13), command=self.qrcode_gen)
        self.btn_gen.place(x=320, y=100)
        
        self.res_area = ctk.CTkFrame(self, fg_color="crimson",corner_radius=0, width=485, height=310)
        self.res_area.place(x=0, y=150)
        
        self.lbl_res_area = ctk.CTkLabel(self.res_area,text=None, fg_color="gray",height=150, width=150)
        self.lbl_res_area.place(x=167, y=30)
        
        self.btn_save = ctk.CTkButton(self.res_area,text="Enregistrer", width=150)#, command=self.save_qrcode)
        self.btn_save.place(x=167, y=210)
        self.img = Image
    
    def qrcode_gen(self):
        try:
            data = self.entry_subject.get()
            res = qrcode.QRCode( version=1,box_size=10,border=2
                )
            res.add_data(data)
            res.make(fit=True)
            res_img  = res.make_image(fill="black",back_color='white')
            res_img.save("test.png")
            pth = pathlib.Path()
            self.img = Image.open(str(pth.cwd())+"/test.png")
            img2 = ctk.CTkImage(self.img, size=[150, 150])
            self.lbl_res_area.configure(image=img2)
        except Exception:
            showerror("Attention","Veuillez inserer du contenu dans le champs")
    
    def save_qrcode(self):
        pass

if __name__=='__main__':
    app = App()
    app.mainloop()
