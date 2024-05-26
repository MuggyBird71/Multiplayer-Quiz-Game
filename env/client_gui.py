import socket
import threading
import tkinter as tk
from tkinter import simpledialog

class QuizClient:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Game Client")

        self.chat_log = tk.Text(master, state='disabled')
        self.chat_log.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()
        self.entry.bind("<Return>", self.send_message)

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(('localhost', 12345))

        threading.Thread(target=self.receive_messages).start()

    def receive_messages(self):
        try:
            while True:
                message = self.client.recv(1024).decode('utf-8')
                self.chat_log.config(state='normal')
                self.chat_log.insert(tk.END, message + '\n')
                self.chat_log.config(state='disabled')
                if "Quiz over!" in message or "Leaderboard:" in message:
                    break
        except Exception as e:
            print(f"Error: {e}")

    def send_message(self, event):
        message = self.entry.get()
        self.client.send(message.encode('utf-8'))
        self.entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    QuizClient(root)
    root.mainloop()

if __name__ == "__main__":
    main()
