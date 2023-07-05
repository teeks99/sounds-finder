import time
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
destination_address = '10.53.1.49'
destination_port = 21011
client_socket.connect((destination_address, destination_port))

message = 'Hello World'
message_bytes = message.encode()

def test():
    start = time.perf_counter()
    client_socket.send(message_bytes)
    response_bytes = client_socket.recv(1024)
    end = time.perf_counter()
    return end - start

result = test()
print(f"Round trip echo completed in: {result:.6f} seconds")

results = []
for _ in range(1, 50):
    results.append(test())

print("Rapid fire")
sum = 0
for result in results:
    sum += result
    print(f"Individual: {result:.6f} seconds")

print(f"Average: {sum/len(results)} seconds")