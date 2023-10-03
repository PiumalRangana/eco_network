#server.py
import socket
port = 1234
address = "127.0.0.1"
buff_size = 15
header_size = 10

# create a socket object name 'server'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((address, port))
server.listen(5)
print("Listening..")

con , adr = server.accept()
print(f"Connected addres is {adr}")


while True:
# This loop keeps the connection running untill the exit message reseve
    new_msg = True
    msg_length = 0
    reseved_message = ""
    while True:
        # This loop receves the buff sized massages and add to the reseved_message veriable untill the full message recives
        data = con.recv(buff_size)
        if new_msg: # Check if receved message a new message
            msg_length = int(data[:header_size].decode("utf-8")) #Extract the length of the massage from the new message
            reseved_message += data[header_size:].decode("utf-8")# Add rest of the message to reseved_message veriable
            new_msg = False
        else:
            reseved_message += data.decode("utf-8")

        if len(reseved_message) >= msg_length:
            print(reseved_message)
            con.send(bytes(f"{len(reseved_message):{header_size}d}{reseved_message}","utf-8"))
            if reseved_message == "exit":
                con.close() # If receves the massage "exit" program terminates the connection
            break
    if reseved_message == 'exit':
        print("----**Connection terminated.**----")
        break

