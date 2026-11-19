#This program uses some custom fonts, namely Plaza LET and NiseSegaSonic. If you are compiling this yourself for some reason, you might want to either download those fonts, or swap them out for something else in the code.


import customtkinter as ctk
from tkinter import filedialog

import customtkinter as ctk
from tkinter import filedialog, messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("red.json")

app = ctk.CTk()
app.title("Shadow Recompiled Save Converter")
app.geometry("650x450")
app.resizable(False, False)

selected_file = None

def oops_all_as():
    if not selected_file:
        status.configure(text="Where is that DAMN Xbox save file?")
        return

    try:
        save_path = filedialog.asksaveasfilename(
            title="Save Shadow Recompiled save file",
            defaultextension=".dat",
            filetypes=[("DAT Files", "*.dat"), ("All Files", "*.*")]
        )

        if not save_path:
            return

        with open(selected_file, "rb") as original:
            data = bytearray(original.read())

        data[0x04:0x18] = bytes.fromhex("AA " * 20)

        with open(save_path, "wb") as output:
            output.write(data)

        status.configure(text="File saved successfully!")

    except Exception as e:
        status.configure(text=f"Error: {e}")

def open_file():
    global selected_file

    filepath = filedialog.askopenfilename(
        title="Select a file (Must be an Xbox .dat save file)",
        filetypes=[
            ("Supported Files", "*.dat"),
            ("All Files", "*.*")
        ]
    )

    if filepath:
        if not filepath.lower().endswith(".dat"):
            messagebox.showerror(
                "Check file",
                "This file is not a .dat file. Please select a valid Xbox save file."
            )
            return

        selected_file = filepath
        file_label.configure(text=filepath)
        status.configure(text="Save loaded")

title = ctk.CTkLabel(
    app,
    text="SHADOW RECOMPILED",
    font=("NiseSegaSonic", 30)
)
title.pack(pady=(30, 20))

title = ctk.CTkLabel(
    app,
    text="sAVE CONVERTEr",
    font=("Plaza LET", 30)
)
title.pack(pady=(0, 15))

file_label = ctk.CTkLabel(
    app,
    text="No file selected",
    font=("Segoe UI", 12),
    wraplength=550
)
file_label.pack(pady=15)

open_button = ctk.CTkButton(
    app,
    text="Select Xbox file",
    command=open_file,
    width=180,
    height=40
)
open_button.pack(pady=10)

modify_button = ctk.CTkButton(
    app,
    text="Convert to Shadow Recompiled save",
    command=oops_all_as,
    width=180,
    height=40
)
modify_button.pack(pady=10)


status = ctk.CTkLabel(
    app,
    text="Ready",
    text_color="gray",
    font=("Segoe UI", 15)
)
status.pack(pady=30)

# Run
app.mainloop()


