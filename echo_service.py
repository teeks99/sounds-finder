import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

listen_address = '0.0.0.0'
listen_port = 21011

listen_location = (listen_address, listen_port)
sock.bind(listen_location)
print("Listening on " + listen_address + ":" + str(listen_port))

while True:
    payload, client_address = sock.recvfrom(1)
    sent = sock.sendto(payload, client_address)
    
    print("Received and sent back to " + str(client_address))