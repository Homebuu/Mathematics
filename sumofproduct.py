import tkinter as tk
from tkinter import messagebox , ttk
from math import pow, sqrt, sin, cos, tan, radians
from sympy import symbols, diff, integrate
import webbrowser

# ฟังก์ชันสำหรับแสดงเมนูหลัก
def show_main_menu():
    global main_menu
    main_menu = tk.Tk()
    main_menu.title("โปรแกรมคำนวณ")
    main_menu.geometry("300x300")
    main_menu.config(bg="#87CEEB")
    main_menu.resizable(False, False)

    tk.Label(main_menu, text="กรุณาเลือกฟังก์ชัน:", bg="#87CEEB").pack(pady=10)

    # ปุ่มสำหรับเลือกฟังก์ชันต่างๆ
    tk.Button(main_menu, text="สูตรคูณ", command=show_multiplication_table_window, bg='#00a8e8', fg='white', font=("Arial", 10, "bold"), relief='flat', width=10, cursor='hand2').pack(pady=5)
    tk.Button(main_menu, text="การยกกำลัง", command=show_power_window, bg='#00a8e8', fg='white', font=("Arial", 10, "bold"), relief='flat', width=10, cursor='hand2').pack(pady=5)
    tk.Button(main_menu, text="พีทาโกรัส", command=show_pythagoras_window, bg='#00a8e8', fg='white', font=("Arial", 10, "bold"), relief='flat', width=10, cursor='hand2').pack(pady=5)
    tk.Button(main_menu, text="Sin, Cos, Tan", command=show_trig_window, bg='#00a8e8', fg='white', font=("Arial", 10, "bold"), relief='flat', width=10, cursor='hand2').pack(pady=5)
    tk.Button(main_menu, text="การหาปริพันธ์ (Integreta)", command=show_integration_window, bg='#00a8e8', fg='white', font=("Arial", 10, "bold"), relief='flat', width=30, cursor='hand2').pack(pady=5)
    tk.Button(main_menu, text="การหาอนุพันธ์ (differentiation)", command=show_differentiation_window, bg='#00a8e8', fg='white', font=("Arial", 10, "bold"), relief='flat', width=30, cursor='hand2').pack(pady=5)

# ฟังก์ชันสำหรับแสดงสูตรคูณ
def show_multiplication_table_window():
    def show_multiplication_table():
        try:
            number = int(entry.get())
            result = ""
            for i in range(1, 13):
                result += f"{number} x {i} = {number * i}\n"
            result_label.config(text=result)
        except ValueError:
            messagebox.showerror("Invalid Input", "กรุณาใส่ตัวเลขเท่านั้น")

    window = tk.Toplevel(main_menu)
    window.title("สูตรคูณ")
    window.geometry("300x400")
    window.config(bg="#87CEEB")
    window.resizable(False, False)

    tk.Label(window, text="กรุณาใส่แม่สูตรคูณ:", bg="#87CEEB").pack(pady=10)
    entry = tk.Entry(window)
    entry.pack()
    tk.Button(window, text="แสดงสูตรคูณ", command=show_multiplication_table, bg='#00a8e8', fg='white', font=("Arial", 10, "bold"), relief='flat', width=10, cursor='hand2').pack(pady=5)
    result_label = tk.Label(window, text="", justify="left", bg="#87CEEB")
    result_label.pack(pady=10)

# ฟังก์ชันสำหรับการยกกำลัง
def show_power_window():
    def calculate_power():
        try:
            base = float(entry_base.get())
            exponent = float(entry_exponent.get())
            result = pow(base, exponent)
            result_label.config(text=f"ผลลัพธ์: {result}")
        except ValueError:
            messagebox.showerror("Invalid Input", "กรุณาใส่ตัวเลขเท่านั้น")

    window = tk.Toplevel(main_menu)
    window.title("การยกกำลัง")
    window.geometry("300x200")
    window.config(bg="#87CEEB")
    window.resizable(False, False)

    tk.Label(window, text="ฐาน:", bg="#87CEEB").pack()
    entry_base = tk.Entry(window)
    entry_base.pack()
    tk.Label(window, text="เลขยกกำลัง:", bg="#87CEEB").pack()
    entry_exponent = tk.Entry(window)
    entry_exponent.pack()
    tk.Button(window, text="คำนวณ", command=calculate_power, bg='#00a8e8', fg='white', font=("Arial", 10, "bold"), relief='flat', width=10, cursor='hand2').pack(pady=5)
    result_label = tk.Label(window, text="", bg="#87CEEB")
    result_label.pack(pady=10)

# ฟังก์ชันสำหรับพีทาโกรัส
def show_pythagoras_window():
    def calculate_pythagoras():
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            result = sqrt(a**2 + b**2)
            result_label.config(text=f"c = {result}")
        except ValueError:
            messagebox.showerror("Invalid Input", "กรุณาใส่ตัวเลขเท่านั้น")

    window = tk.Toplevel(main_menu)
    window.title("พีทาโกรัส")
    window.geometry("300x200")
    window.config(bg="#87CEEB")
    window.resizable(False, False)

    tk.Label(window, text="a:", bg="#87CEEB").pack()
    entry_a = tk.Entry(window)
    entry_a.pack()
    tk.Label(window, text="b:", bg="#87CEEB").pack()
    entry_b = tk.Entry(window)
    entry_b.pack()
    tk.Button(window, text="คำนวณ", command=calculate_pythagoras, bg='#00a8e8', fg='white', font=("Arial", 10, "bold"), relief='flat', width=10, cursor='hand2').pack(pady=5)
    result_label = tk.Label(window, text="", bg="#87CEEB")
    result_label.pack(pady=10)

# ฟังก์ชันสำหรับการคำนวณ Sin, Cos, Tan
def show_trig_window():
    def calculate_trig():
        try:
            angle = radians(float(entry_angle.get()))
            sin_val = sin(angle)
            cos_val = cos(angle)
            tan_val = tan(angle)
            result_label.config(text=f"sin: {sin_val}\ncos: {cos_val}\ntan: {tan_val}")
        except ValueError:
            messagebox.showerror("Invalid Input", "กรุณาใส่ตัวเลขเท่านั้น")

    window = tk.Toplevel(main_menu)
    window.title("Sin, Cos, Tan")
    window.geometry("300x200")
    window.config(bg="#87CEEB")
    window.resizable(False, False)

    tk.Label(window, text="มุม (องศา):", bg="#87CEEB").pack()
    entry_angle = tk.Entry(window)
    entry_angle.pack()
    tk.Button(window, text="คำนวณ", command=calculate_trig, bg='#00a8e8', fg='white', font=("Arial", 10, "bold"), relief='flat', width=10, cursor='hand2').pack(pady=5)
    result_label = tk.Label(window, text="", bg="#87CEEB")
    result_label.pack(pady=10)

x = symbols('x')

# ฟังก์ชันสำหรับการอินติเกรด (placeholder)

def show_integration_window():
    def calculate_integration():
        try:
            expr = entry_expression.get()
            integral = integrate(expr, x)
            result_label.config(text=f"∫({expr}) dx = {integral}")
        except Exception as e:
            messagebox.showerror("Error", f"เกิดข้อผิดพลาด: {e}")

    # สร้างหน้าต่างใหม่สำหรับหาปริพันธ์
    window = tk.Toplevel(main_menu)
    window.title("Integration")
    window.geometry("300x200")
    window.config(bg="#87CEEB")
    window.resizable(False, False)

    tk.Label(window, text="ใส่สมการที่ต้องการหาปริพันธ์ (ใช้ x เป็นตัวแปร):", bg="#87CEEB").pack()
    entry_expression = tk.Entry(window)
    entry_expression.pack()
    tk.Button(window, text="คำนวณ", command=calculate_integration, bg='#00a8e8', fg='white', font=("Arial", 10, "bold"), relief='flat', width=10, cursor='hand2').pack(pady=5)
    result_label = tk.Label(window, text="", bg="#87CEEB")
    result_label.pack(pady=10)


# ฟังก์ชันการหาอนุพันธ์ (Differentiation)
def show_differentiation_window():
    def calculate_derivative():
        try:
            expr = entry_expression.get()
            derivative = diff(expr, x)
            result_label.config(text=f"d/dx({expr}) = {derivative}")
        except Exception as e:
            messagebox.showerror("Error", f"เกิดข้อผิดพลาด: {e}")

    window = tk.Toplevel(main_menu)
    window.title("Differentiation")
    window.geometry("300x200")
    window.config(bg="#87CEEB")
    window.resizable(False, False)

    tk.Label(window, text="ใส่สมการที่ต้องการหาอนุพันธ์ (ใช้ x เป็นตัวแปร):", bg="#87CEEB").pack()
    entry_expression = tk.Entry(window)
    entry_expression.pack()
    tk.Button(window, text="คำนวณ", command=calculate_derivative, bg='#00a8e8', fg='white', font=("Arial", 10, "bold"), relief='flat', width=10, cursor='hand2').pack(pady=5)
    result_label = tk.Label(window, text="", bg="#87CEEB")
    result_label.pack(pady=10)

def open_discord_link():
    webbrowser.open("https://discord.gg/y3YZ6EtFPz")  

def check_key():
    login_window.destroy()  
    show_main_menu()       

# เริ่มต้นหน้าต่าง Login
login_window = tk.Tk()
login_window.title("HG - TEAM")
login_window.geometry("250x100")
login_window.config(bg="#87CEEB")
login_window.resizable(False, False)

# สร้างสไตล์ใหม่และกำหนดสไตล์ให้ ttk.Entry
style = ttk.Style()
style.configure('Modern.TEntry', padding=10)

tk.Button(login_window, text="Login", command=check_key, bg='#00a8e8', fg='white', font=("Arial", 10, "bold"), relief='flat', width=10, cursor='hand2').pack(pady=10)
discord_link = tk.Button(login_window, text="Discord", bg='#00a8e8', fg='white', font=("Arial", 10, "bold"), relief='flat', width=10, cursor='hand2')
discord_link.pack(pady=5)
discord_link.bind("<Button-1>", lambda e: open_discord_link())

login_window.mainloop()
