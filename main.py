import tkinter as tk
from tkinter import filedialog, messagebox
import os

# >>> FUNCTIONS <<<

def encrypt(this_file, key):
    try:
        with open(this_file, 'rb') as file:
            data = file.read()
        
        encrypted_data = bytearray([byte ^ key for byte in data])
        new_file = this_file + '.encrypted'

        with open(new_file, 'wb') as file:
            file.write(encrypted_data)

        os.remove(this_file)
        return new_file
    
    except Exception as e:
        messagebox.showerror("Error", "Error")
        return None

def decrypt(this_file, key):
    try:
        with open(this_file, 'rb') as file:
            data = file.read()
        
        decrypted_data = bytearray([byte ^ key for byte in data])
        
        if this_file.endswith('.encrypted'):
            new_file = this_file.replace('.encrypted', '')
        else:
            messagebox.showerror("Error", "Error")
            return None
        
        with open(new_file, 'wb') as file:
            file.write(decrypted_data)
        
        os.remove(this_file)
        return new_file
    
    except Exception as e:
        messagebox.showerror("Error", "Error")
        return None

def select_file():
    file_path = filedialog.askopenfilename(title="Select File")

    if file_path:
        entry_file_path.delete(0, tk.END)
        entry_file_path.insert(0, file_path)

def encrypt_file():
    file_path = entry_file_path.get()
    key = entry_key.get()
    
    if not file_path:
        messagebox.showwarning("Error", "Select File")
        return
    
    if not key.isdigit():
        messagebox.showwarning("Error", "Key must be a number")
        return
    
    key = int(key) % 256
    new_file_path = encrypt(file_path, key)

    if new_file_path:
        messagebox.showinfo("Success", f"{new_file_path}")

def decrypt_file():
    file_path = entry_file_path.get()
    key = entry_key.get()

    if not file_path:
        messagebox.showwarning("Error", "Select File")
        return
    
    if not key.isdigit():
        messagebox.showwarning("Error", "Key must be a number")
        return
    
    key = int(key) % 256
    new_file_path = decrypt(file_path, key)

    if new_file_path:
        messagebox.showinfo("Success", f"{new_file_path}")

# >>> GUI <<<

window = tk.Tk()
window.title("Simple Encryption")

label_file = tk.Label(window, text="File path:")
label_file.grid(row=0, column=0)

entry_file_path = tk.Entry(window, width=30)
entry_file_path.grid(row=0, column=1, padx=5, pady=5)

button_browse = tk.Button(window, text="Select File", command=select_file)
button_browse.grid(row=0, column=2)

label_key = tk.Label(window, text="Enter key:")
label_key.grid(row=1, column=0)

entry_key = tk.Entry(window, width=30)
entry_key.grid(row=1, column=1)

button_encrypt = tk.Button(window, text="Encrypt", command=encrypt_file)
button_encrypt.grid(row=2, column=0)

button_decrypt = tk.Button(window, text="Decrypt", command=decrypt_file)
button_decrypt.grid(row=2, column=2)

window.mainloop()