import socket
import threading
import openai


openai.api_key = 'sk-proj-7lzK0BVDXd2fyTK7Zu6zT3BlbkFJRQ6WWWWpFuu11paSz13a'

clients = []
scores = {}
users = {"user1": "password1"}  # Simple user authentication (username: password)

def broadcast(message):
    for client in clients:
        client.send(message.encode('utf-8'))

def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")
    client_socket.send("Enter username: ".encode('utf-8'))
    username = client_socket.recv(1024).decode('utf-8').strip()
    client_socket.send("Enter password: ".encode('utf-8'))
    password = client_socket.recv(1024).decode('utf-8').strip()

    if users.get(username) == password:
        client_socket.send("Login successful!\n".encode('utf-8'))
        clients.append(client_socket)
        scores[client_socket] = 0
    else:
        client_socket.send("Login failed!\n".encode('utf-8'))
        client_socket.close()
        return

    try:
        for _ in range(3):  # Number of questions
            question, answer = generate_question()
            client_socket.send(question.encode('utf-8'))
            response = client_socket.recv(1024).decode('utf-8').strip()
            if response.lower() == answer.lower():
                scores[client_socket] += 1
            client_socket.send(f"Your score: {scores[client_socket]}\n".encode('utf-8'))
        
        client_socket.send("Quiz over!\n".encode('utf-8'))
        final_score = scores[client_socket]
        client_socket.send(f"Your final score: {final_score}\n".encode('utf-8'))

        # Update leaderboard
        leaderboard = "Leaderboard:\n"
        sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)
        for idx, (sock, score) in enumerate(sorted_scores):
            leaderboard += f"{idx+1}. Score: {score}\n"
        client_socket.send(leaderboard.encode('utf-8'))
    except Exception as e:
        print(f"Error: {e}")

    clients.remove(client_socket)
    client_socket.close()

def generate_question():
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Generate a trivia question with a clear answer.",
        max_tokens=100
    )
    question_text = response.choices[0].text.strip()
    question, answer = question_text.split("?")
    question += "?"
    return question.strip(), answer.strip()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 12345))
    server.listen(5)
    print("Server listening on port 12345")

    while True:
        client_socket, client_address = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

if __name__ == "__main__":
    start_server()
