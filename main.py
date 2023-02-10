import customtkinter
import tkinter

# root = tkinter.Tk()
# label = tkinter.Label(root)
# label.pack()


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

def login():
    print("You are loged In")

frame=customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label=customtkinter.CTkLabel(master=frame, text="Login System", font=("Roboto", 24))
label.pack(pady=12, padx=10)

entry_1=customtkinter.CTkEntry(master=frame, placeholder_text="User Name")
entry_1.pack(pady=12, padx=10)

entry_2=customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry_2.pack(pady=12, padx=10)

button=customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady = 12, padx = 10)

checkbox=customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady = 12, padx = 10)

root.mainloop()


