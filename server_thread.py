import socket
import threading
import pickle

HOST ="0.0.0.0"  # Listen on all network interfaces
PORT = 5001

class ClientThread(threading.Thread):
    def __init__(self, conn, addr):
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        print(f"New connection from {addr}")

    def run(self):
        while True:
            # Receive input data from the client
            data = self.conn.recv(1024)
            if not data:
                print(f"Connection from {self.addr} closed")
                break

            # Unpickle the received data
            input_data = pickle.loads(data)
            print(f"Input data received from {self.addr}")

            # Process the input data and update the game state
            print(input_data['keyboard_inputs'])

            # Send game state data back to the client
            # game_state = {'position': [x, y], 'health': health, 'score': score}
            # game_state_data = pickle.dumps(game_state)
            # self.conn.sendall(game_state_data)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Listening on {HOST}:{PORT}")
    while True:
        # Wait for a new connection
        conn, addr = s.accept()

        # Start a new thread to handle the client connection
        client_thread = ClientThread(conn, addr)
        client_thread.start()
