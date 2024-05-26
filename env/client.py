import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))

    try:
        while True:
            message = client.recv(1024).decode('utf-8')
            if "Quiz over!" in message or "Leaderboard:" in message:
                print(message)
                break
            print(message)
            response = input()
            client.send(response.encode('utf-8'))
    except Exception as e:
        print(f"Error: {e}")

    client.close()

if __name__ == "__main__":
    main()
