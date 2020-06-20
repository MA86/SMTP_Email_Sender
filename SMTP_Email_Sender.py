from socket import *

msg = "From: BE <tixapo2186@vewku.com>\r\nTo: BE <tixapo2186@vewku.com>\r\nSubject: Test message\r\nNetworking student testing SMTP protocol"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'gmail-smtp-in.l.google.com'

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.bind(('xxx.xxx.xxx.xxx', 12345))
clientSocket.connect((mailserver, 25))

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
clientSocket.send('MAIL FROM: <tixapo2186@vewku.com>\r\n'.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)

# Send RCPT TO command and print server response.
clientSocket.send('RCPT TO: <tixapo2186@vewku.com>\r\n'.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)

# Send DATA command and print server response.
clientSocket.send('DATA\r\n'.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)

# Send message data.
clientSocket.send(msg.encode())

# Message ends with a single period.
clientSocket.send(endmsg.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)

# Send QUIT command and get server response.
clientSocket.send('QUIT\r\n'.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)
