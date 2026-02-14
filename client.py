import socket
import threading
import tkinter as tk
from tkinter import messagebox

def connect_to_server():
    host = host_entry.get()
    port = int(port_entry.get())
    try:
        client_socket.connect((host, port))
        add_message(f"Connected to server {host}:{port}", "system")
        threading.Thread(target=receive_messages, daemon=True).start()
    except Exception as e:
        messagebox.showerror("Connection Error", str(e))


def receive_messages():
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if msg:
                add_message(msg, "server")
            else:
                break
        except:
            break


def send_message():
    msg = message_entry.get()
    if msg.strip() != "":
        add_message(msg, "client")
        client_socket.send(msg.encode())
        message_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty Message", "Please type something!")


def add_message(msg, sender="system"):
    frame = tk.Frame(scroll_frame, bg="#f5f5f5")

    if sender == "client":
        bg_color = "#dcf8c6"  
        anchor = "e"
        padx = (50, 10)
    elif sender == "server":
        bg_color = "#ebebeb" 
        anchor = "w"
        padx = (10, 50)
    else:
        bg_color = "#cce5ff" 
        anchor = "center"
        padx = (100, 100)

    msg_label = tk.Label(frame, text=msg, bg=bg_color, wraplength=300, justify="left",
                         font=("Arial", 12), padx=10, pady=5)
    msg_label.pack(anchor=anchor)

    frame.pack(fill=tk.X, padx=padx, pady=5, anchor=anchor)

    canvas.update_idletasks()
    canvas.yview_moveto(1.0)

root = tk.Tk()
root.title("Client Chat")
root.geometry("500x600")
root.config(bg="#f5f5f5")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

top_frame = tk.Frame(root, bg="#c2185b")
top_frame.pack(fill=tk.X)

tk.Label(top_frame, text="Server Host:", bg="#c2185b", fg="white", font=("Arial", 10, "bold")).pack(side=tk.LEFT,
                                                                                                    padx=5, pady=5)
host_entry = tk.Entry(top_frame, width=12)
host_entry.pack(side=tk.LEFT, padx=5)
host_entry.insert(0, "127.0.0.1")

tk.Label(top_frame, text="Port:", bg="#c2185b", fg="white", font=("Arial", 10, "bold")).pack(side=tk.LEFT)
port_entry = tk.Entry(top_frame, width=5)
port_entry.pack(side=tk.LEFT, padx=5)
port_entry.insert(0, "12345")

tk.Button(top_frame, text="Connect", command=connect_to_server, bg="green", fg="white",
          font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=10)

canvas_frame = tk.Frame(root, bg="#f5f5f5")
canvas_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

canvas = tk.Canvas(canvas_frame, bg="#f5f5f5")
scrollbar = tk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

scroll_frame = tk.Frame(canvas, bg="#f5f5f5")
canvas.create_window((0, 0), window=scroll_frame, anchor='nw')


def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))


scroll_frame.bind("<Configure>", on_frame_configure)

input_frame = tk.Frame(root, bg="#f5f5f5")
input_frame.pack(fill=tk.X, padx=10, pady=10)

message_entry = tk.Entry(input_frame, font=("Arial", 12))
message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10), ipady=8)
message_entry.bind("<Return>", lambda e: send_message())

send_button = tk.Button(input_frame, text="Send", command=send_message, bg="#c2185b", fg="white",
                        font=("Arial", 12, "bold"))
send_button.pack(side=tk.RIGHT)

root.mainloop()

