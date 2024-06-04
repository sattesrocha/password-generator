import tkinter as tk
from tkinter import messagebox
from random import choice

def generate_passwords():
    try:
        num = int(entry_quantity.get())
        length = int(entry_length.get())
    except ValueError:
        if lang == 'en':
            messagebox.showerror("Error", "Please enter valid integer values for quantity and length.")
        else:
            messagebox.showerror("Erro", "Por favor, insira valores inteiros válidos para quantidade e tamanho.")
        return

    strings = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
               "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!",
               "@", "#", "$", "%", "&", "*")

    passwords = []

    for _ in range(num):
        password = ''.join(choice(strings) for _ in range(length))
        passwords.append(password)

    text_output.delete(1.0, tk.END)
    for password in passwords:
        text_output.insert(tk.END, password + '\n')

def main_window():
    global entry_quantity, entry_length, text_output

    window = tk.Tk()
    window.title("PWGen - Password Generator")
    window.configure(bg="#282c34")

    frame = tk.Frame(window, bg="#282c34")
    frame.pack(pady=20)

    if lang == 'en':
        welcome_label = tk.Label(frame, text="Welcome to PWGen!", font=("Helvetica", 16, "bold"), bg="#282c34", fg="#61dafb")
        label_quantity = tk.Label(frame, text="Quantity:", font=("Helvetica", 12), bg="#282c34", fg="#abb2bf")
        label_length = tk.Label(frame, text="Length:", font=("Helvetica", 12), bg="#282c34", fg="#abb2bf")
        button_generate = tk.Button(frame, text="Generate", font=("Helvetica", 12), bg="#61dafb", fg="#282c34", command=generate_passwords)
    else:
        welcome_label = tk.Label(frame, text="Bem-vindo ao PWGen!", font=("Helvetica", 16, "bold"), bg="#282c34", fg="#61dafb")
        label_quantity = tk.Label(frame, text="Quantidade:", font=("Helvetica", 12), bg="#282c34", fg="#abb2bf")
        label_length = tk.Label(frame, text="Tamanho:", font=("Helvetica", 12), bg="#282c34", fg="#abb2bf")
        button_generate = tk.Button(frame, text="Gerar", font=("Helvetica", 12), bg="#61dafb", fg="#282c34", command=generate_passwords)

    welcome_label.grid(row=0, column=0, columnspan=2, pady=10)
    label_quantity.grid(row=1, column=0, sticky='e', padx=5, pady=5)
    entry_quantity = tk.Entry(frame, font=("Helvetica", 12), bg="#abb2bf", fg="#282c34")
    entry_quantity.grid(row=1, column=1, padx=5, pady=5)
    label_length.grid(row=2, column=0, sticky='e', padx=5, pady=5)
    entry_length = tk.Entry(frame, font=("Helvetica", 12), bg="#abb2bf", fg="#282c34")
    entry_length.grid(row=2, column=1, padx=5, pady=5)
    button_generate.grid(row=3, column=0, columnspan=2, pady=10)

    text_output = tk.Text(window, height=10, width=50, font=("Helvetica", 12), bg="#282c34", fg="#abb2bf")
    text_output.pack(pady=10)

    window.mainloop()

def select_language():
    global lang

    def set_language(selected_lang):
        global lang
        lang = selected_lang
        lang_window.destroy()
        main_window()

    lang_window = tk.Tk()
    lang_window.title("Select Language / Escolha o Idioma")
    lang_window.configure(bg="#282c34")

    lang_label = tk.Label(lang_window, text="Choose Language / Escolha o Idioma", font=("Helvetica", 16, "bold"), bg="#282c34", fg="#61dafb")
    lang_label.pack(pady=20)

    button_en = tk.Button(lang_window, text="English", font=("Helvetica", 12), bg="#61dafb", fg="#282c34", command=lambda: set_language('en'))
    button_en.pack(pady=10)

    button_pt = tk.Button(lang_window, text="Português", font=("Helvetica", 12), bg="#61dafb", fg="#282c34", command=lambda: set_language('pt'))
    button_pt.pack(pady=10)

    lang_window.mainloop()

if __name__ == "__main__":
    select_language()
