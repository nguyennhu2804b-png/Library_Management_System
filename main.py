import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Library Management System - Test")
root.geometry("400x250")

label = tk.Label(root, text="Hệ thống Quản lý Thư viện\n(Môi trường của Như đã sẵn sàng!)", font=("Arial", 12))
label.pack(pady=30)

def check():
    messagebox.showinfo("Thành công", "Tkinter và Python đã kết nối hoàn hảo!")

btn = tk.Button(root, text="Nhấn để kiểm tra", command=check, bg="green", fg="white")
btn.pack()

root.mainloop()