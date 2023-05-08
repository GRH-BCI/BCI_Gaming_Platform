import socket
import pickle
from pynput import keyboard

HOST = "172.29.83.101"  # The server's hostname or IP address
PORT = 65444  # The port used by the server

key_name = None

def on_press(key):
    global key_name
    try:
        key_name = key.char
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        key_name = key.name
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == key:
        # Stop listener
        return False

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        # Get keyboard and controller inputs from the player
        # Collect events until released
        with keyboard.Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()

        print(key_name)
        if key_name is not None:
            print("getting ready to send")
            # Pack input data into a Python object
            input_data = {'keyboard_inputs': key_name}

            # Serialize the input data using pickle
            input_data_serialized = pickle.dumps(input_data)

            # Send the input data to the server
            s.sendall(input_data_serialized)

            # Reset key_name
            key_name = None

