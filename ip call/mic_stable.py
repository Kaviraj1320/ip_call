import socket
import pyaudio
HOST = 'localhost'
PORT = 10000
WIDTH = 2
CHANNELS = 1
RATE = 44100
p=pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True)
print("start streaming")
with socket.socket() as conn_mic:
    conn_mic.connect((HOST, PORT))
    while True:
        data = stream.read(512)
        conn_mic.send(data)

