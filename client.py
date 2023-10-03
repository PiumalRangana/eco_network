#client.py
import socket
port = 1234
address = '127.0.0.1'
BUF_SIZE = 15

# create a socket object name 'con'
con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
con.connect((address, port))



# prepaire the massage
header_size = 10
while True:
    message = input("enter the message: ")
    message_length = len(message.encode("utf-8"))

    prepaired_message = f"{message_length:{header_size}d}{message}"  #Add the length of the message in the hearder of the message

    con.send(bytes(prepaired_message , "utf-8"))
    receved_message = ''
    new_msg = True
    while True:   
        data = con.recv(BUF_SIZE)
        if new_msg:
            message_length =int( data[:header_size].decode("utf-8"))
            receved_message += data[header_size:].decode("utf-8")
            new_msg = False
        else:
            receved_message += data.decode("utf-8")

        if len(receved_message) >= message_length:
            print(receved_message)
            break
    if receved_message == "exit":
        con.close()
        break

