# 💬 Chat Application (Tkinter GUI)

A simple GUI-based Client-Server Chat Application built using Python Tkinter.  
This application allows real-time messaging between a server and a client over a network.

---

## 🚀 Features

- Real-time messaging between server and client
- Color-coded messages for server, client, and system
- Scrollable chat history
- Enter key support for sending messages
- Simple and clean Tkinter interface

---

## 🛠️ Technologies Used

- Python 3
- Tkinter (GUI Library)
- Socket programming
- Threading module

---

## 📂 Project Structure

ChatApp/
│
├── server.py
├── client.py
└── README.md

---

## ⚙️ Installation & Running

### 1️⃣ Clone the Repository
bash git clone https://github.com/your-username/ChatApp.git cd ChatApp
`

### 2️⃣ Run the Server
bash python server.py
### 3️⃣ Run the Client
bash python client.py
---

## 🔑 How It Works

1. Start the server by entering **Host** and **Port**, then click **Start Server**.
2. Start the client, enter the server **Host** and **Port**, then click **Connect**.
3. Type messages in the input field and press **Send** or **Enter**.
4. Messages appear in the chat window for both server and client.

---

## 📌 Message Rules

* Server messages → Light green bubbles
* Client messages → Gray/light green bubbles
* System messages → Light blue bubbles
* Messages wrap automatically and scroll when exceeding window height

---

## 🖥️ Interface Overview

* Host & Port input fields
* Connect / Start Server button
* Scrollable chat display
* Message input field
* Send button

---

## 🔮 Future Enhancements

* Support for multiple clients with broadcasting
* Private messaging between clients
* Emoji and rich text support
* File transfer support
* Dark mode interface

---

## 👩‍💻 Author

Harshitha V

---

## 📜 License

This project is licensed under the MIT License
