import socket
import pickle

HOST = "172.29.83.101"  # Standard loopback interface address (localhost)
PORT = 65444  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            # Receive input data from the client
            data = conn.recv(1024)

            # Unpickle the received data
            input_data = pickle.loads(data)
            print('Input data received')

            # Process the input data and update the game state
            print(input_data['keyboard_inputs'])

            # Send game state data back to the client
            # game_state = {'position': [x, y], 'health': health, 'score': score}
            # game_state_data = pickle.dumps(game_state)
            # client_socket.sendall(game_state_data)