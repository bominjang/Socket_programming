# Socket_programming
Python Socket Programming

socket programming이란, 네트워크상에서 통신을 위해 두개의 노드가 연결되는 방법이다.
한 소켓(노드)가 또다른 커넥션을 생성하는 동안, 하나의 소켓은 어떤 IP의 특정 port에서 listen하고 있는다. 클라이언트가 서버에 접근하는 동안 서버는 리스너 소켓을 형성한다. 이 통신은 웹 브라우징에서 가장 중요한 역할을 하고, 우리는 보통 서버-클라이언트 통신이라고 부른다.

소켓 프로그래밍은 socket library를 import하고 simple socket을 만들면서 시작된다. 

### Connecting to a server

socket을 이용하여 server와 통신해보자.
먼저, 소켓을 만드는 동안 오류가 발생하면 socket.error가 발생함.
일단 서버를 알고있어야 서버에 연결할 수 있는데 다음을 사용하여 서버의 ip를 찾을 수 있음.

```
    ping www.google.com
```
*ping 명령어는 해당 도메인에 IP를 확인할 때 많이 사용함*

```
    import socket

    ip = socket.gethostbyname('www.google.com')
    print(ip)
```
위 코드를 사용해도 해당 서버의 ip를 찾을 수 있다.

```
    import socket
    import sys

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket successfully created")
    except socket.error as err:
        print("socket creation failed with error %s" %(err))

    # default port for socket
    port = 80

    try:
        host_ip = socket.gethostbyname('www.google.com')
    except socket.gaierror:
        # this means could not resolve the host
        print("there was an error resolving the host")
        sys.exit()

    # connecting to the server
    s.connect((host_ip, port))

    print ("the socket has successfully connected to google \non port == %s" %(host_ip))
```

- 먼저, 소켓을 만들었다.
- 그리고 구글의 ip를 받고 s.connect((host_ip,port)) 를 통해 서버에 연결했다.
- 이제 소켓을 통해 데이터를 어떻게 보낼 수 있는지 알아야 함.
- 데이터를 보내기 위해 소켓 라이브러리에는 sendall 함수가 있다. 이 함수를 사용하면 소켓이 연결된 서버로 데이터 전송이 가능하고 
서버 또한 이 기능을 사용하여 클라이언트로 데이터를 보낼 수도 있음.

### A simple server-client program : 
**Server** : 
서버에는 특정 IP 및 포트에 바인드하여 해당 IP 및 포트에서 들어오는 요청을 들을 수 있는 bind() 메소드가 있음.
서버에는 서버를 listen 모드로 만드는 listen() 메소드가 있음. 이를 통해 서버는 들어오는 연결을 listen할 수 있음.
마지막으로 서버에는 accept() 및 close() 메소드가 있음. accept 메소드는 클라이언트와의 연결을 시작하고 close 메소드는 클라이언트와의 연결을 끊음. 

```
    #first of all import the socket library
    import socket

    #next create a socket object
    s = socket.socket()
    print("Socket successfully created")

    #reserve a port on your computer in our case
    #it is 12345 but it can be anything
    port = 12345

    #Next bind to the port
    #we have not typed any ip in the ip field
    #instead we have inputted an empty string
    #this makes the server listen to requests coming from other computers on the network

    s.bind(('',port))
    print ("socket binded to %s" %(port))

    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")

    # a forever loop unitl we interrupt it or an error occurs
    while True:
        #Establish connection with client
        c, addr = s.accept()
        print("Got connection from", addr)

        #send a thank you message to the client.
        c.send("Thank you for connecting")

        #Close the connection with the client
        c.close()
```

- 필수적으로 처음에 socket을 import 함
- 그리고 socket을 만들고, 우리 pc의 port로 받도록 함.
- 그런 다음 서버를 지정된 포트에 바인딩함. (bind 함수를 통해!)
- 빈 문자열을 전달하면 서버가 다른 컴퓨터에서도 들어오는 연결을 수신할 수 있음.
- 만약 우리가 127.0.0.1을 pass했다면, 그건 로컬 컴퓨터 내에서 이루어진 호출들만 들을 수 있었을 것.
- 그리고 우리는 서버를 listen 모드로 전환했음.
- 여기서 '5'는 서버가 사용 중일 때, 5개의 연결까지는 계속 기다리고, 6번째 소켓이 연결을 시도하면 연결이 거부됨을 의미.
- 마지막으로 while 루프를 만들고 들어오는 모든 연결을 받아들이고, 연결된 모든 소켓에 감사메시지를 보낸 후 해당 연결을 close

**Client**
이제 서버와 상호작용할 수 있는 무언가가 필요함. 
서버가 작동한다는 것을 알 수 있는 방법으로는 terminal에 다음 명령어를 입력하는 방법이 있다.
일단 서버를 작동시키고,
```
    #start the server
    python server.py
```

#keep the above terminal open
#now open another terminal and type:
```
    telnet localhost 12345
```
**Output:**

```
    #in the server.py terminal you will see
    #this output:
    ocket successfully created
    socket binded to 12345
    socket is listening
    Got connection from ('127.0.0.1', 58933)
```

```
    #In the telnet terminal you will get this:
    Trying ::1...
    telnet: connect to address ::1: Connection refused
    Trying 127.0.0.1...
    Connected to localhost.
    Escape character is '^]'.
    Connection closed by foreign host.
```

위 결과가 나오면 server가 잘 작동하고 있는 것.

**Now for the client side**
```
    #import socket module
    import socket

    #Create a socket object
    s = socket.socket()

    #Define the port on which you to connect
    port = 12345

    #connect to the server on local computer
    s.connect(('127.0.0.1',port))

    #receive data from the server
    print (s.recv(1024)) # byte를 정해준 것. string을 받겠다! 이렇게.
    #close the connection
    s.close()
```

- 먼저 socket 모듈 import하고
- localhost의 12345 port에 연결. (우리 서버가 작동중인 ip,port에) 그리고 lastly server에서 데이터 얻고, close
- 이제는 서버 스크립트 실행 후, 클라이언트스크립틀르 실행시켜보자.

**Output**
#reference
https://www.geeksforgeeks.org/socket-programming-python/