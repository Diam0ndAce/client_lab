import socket
if '__main__'==__name__:
    s=socket.socket()
    #host=socket.gethostname()##185.57.29.217
    host='192.168.56.102'
    #host='kali'
    print('main host',host)
    port=50000
    s.connect((host,port))
    with open('C:\\Users\\User\\Desktop\\ServerAnswer.txt', 'wb') as f:
        while True:
            data = s.recv(1024)
            print('data=%s', (data))
            if not data:
                break
            # write data to a file
            f.write(data)
    s.close()
