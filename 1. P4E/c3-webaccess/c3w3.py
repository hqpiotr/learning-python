# web communication
# sockets, urllib
import socket
import urllib.request, urllib.parse, urllib.error

def get_file_using_socket():
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))
    cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')

    mysock.close()

def get_file_using_urllib():
    # one option
    file = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
    for line in file:
        print(line.decode().strip())

    print('\n--- separator ---\n')

    # second option
    file2 = urllib.request.urlopen('http://data.pr4e.org/romeo.txt').read().decode()
    print(file2)


def call_main():
    # get_file_using_socket()
    get_file_using_urllib()

if __name__ == "__main__":
    call_main()
