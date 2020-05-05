import socket
import pyaudio
HOST = "localhost"
PORT = 10000

p = pyaudio.PyAudio()
WIDTH = 2
CHANNELS = 1
RATE = 44100
stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                output=True)

with socket.socket() as conn_speaker:
    conn_speaker.bind((HOST, PORT))
    conn_speaker.listen(1)
    try:
        conn, address = conn_speaker.accept()
        data = conn.recv(512)
        while data != '':
            print("working")
            try:
                print("working1")
                data = conn.recv(512)
                print("working2")
                while True:
                    stream.write(data)
                print("working3")
            except Exception as e:
                print(str(e))
    except Exception as e:
        print(str(e))
