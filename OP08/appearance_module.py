import tkinter as tk

def apply_appearance_settings(root):
    root.geometry("600x400")


    style_font = ("Arial", 12)
    style_bg = "#D3D3D3"
    style_fg = "#333333"

    for widget in root.winfo_children():
        if isinstance(widget, tk.Label):
            widget.config(font=style_font, bg=style_bg, fg=style_fg)
        elif isinstance(widget, tk.Button):
            widget.config(font=style_font, bg="#00ced1", fg="white")
        elif isinstance(widget, tk.Entry):
            widget.config(font=style_font, bg="#FAFAFA", fg="#333333")