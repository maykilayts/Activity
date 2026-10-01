import customtkinter as ctk
from PIL import Image
app = ctk.CTk()
app.geometry("500x400")
app.config(bg='white')
app.title("Security")

background_image = ctk.CTkImage(
light_image=Image.open("picture.gif"),
dark_image=Image.open("picture.gif"),
size=(1000, 650)
)

background_label = ctk.CTkLabel(app, image=background_image, text="")
background_label.place(x=0, y=0, relwidth=1, relheight=1)

page1 = ctk.CTkFrame(app, width=400, height=300, fg_color="#222F5B")
page1.place(relx=0.5, rely=0.5, anchor='center')
page1.pack_propagate(False) 

login_label = ctk.CTkLabel(page1, text="Login", font=("Cosmic sans", 30))
login_label.pack(padx=15, pady=15)

username = ctk.CTkEntry(page1, width=300, height=40,
placeholder_text="Enter Username", fg_color="transparent")
username.pack(pady=10)


password = ctk.CTkEntry(page1, width=300, height=40,
placeholder_text="Enter Password", show="*", fg_color="transparent")
password.pack(pady=10)

login_button = ctk.CTkButton(page1, text="Login", width=300, height=40)
login_button.pack(pady=10)



app.mainloop()
