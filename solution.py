# import socket module
import socket
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  hostName= "localhost"
  #Prepare a server socket
  serverSocket.bind((hostName, port))
  #Fill in start
  serverSocket.listen(1)
  #print('The server is ready to receive')
  #Fill in end

  while True:
    #Establish the connection
    #print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:

      try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        
        #Send one HTTP header line into socket.
        okMessage = "HTTP/1.1 200 OK\r\n"
        connectionSocket.send(okMessage.encode())


        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
          connectionSocket.send(outputdata[i].encode())

        connectionSocket.send(outputdata)
        connectionSocket.close()

      except IOError:
        # Send response message for file not found (404)
        #Fill in start
        NotFoundMessage= "HTTP/1.1 404 Not Found\r\n"
        connectionSocket.send(NotFoundMessage.encode())
        #Fill in end


        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end

    except (ConnectionResetError, BrokenPipeError):
      pass

  serverSocket.close()
  sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
