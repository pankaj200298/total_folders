import tkinter as tk
import psutil

def get_cpu_temperature():
    temp = psutil.sensors_temperatures()['coretemp'][0].current
    return f"CPU Temperature: {temp}°C"

def update_temperature_label(label):
    label.config(text=get_cpu_temperature())
    root.after(1000, lambda: update_temperature_label(label))

root = tk.Tk()
root.title("CPU Temperature")

label = tk.Label(root, font=('Helvetica', 24), fg='red')
label.pack()

update_temperature_label(label)

root.mainloop()