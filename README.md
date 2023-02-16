# web-server

This README.md file was generated on 2023-02-15 by Shion M. 

This web server lab was an assignment from the ECE303 course at The Cooper Union. The lab implements creating a socket, binding it to a specific address and port, as well as sending and receiving a HTTP packet.
- The file **webserver.py** is the web server that handles one HTTP request at a time. The web server accepts and parses the HTTP request, gets the requested file from the server’s file system, creates an HTTP response message consisting of the requested file preceded by header lines, and then sends the response directly to the client. If the requested file is not present in the server, the server sends an HTTP “404 Not Found” message back to the client.
- The **hello.html** file is a simple HTML file that is used for testing the **webserver.py**. It is used as the requested file.
- **ip.py** is a simple program that returns the local host name / IP address with various methods. This was implemented primarily for testing purposes for **webserver.py**.


## CONTENTS OF THIS FILE
 
- [Contained Files](#contained-files)
- [Usage](#usage)
- [Author](#author)
- [File Creation Date](#file-creation-date)


## CONTAINED FILES

- webserver.py
- hello.html
- ip.py


# Usage

- Run **ip.py** to determine the IP address of the host that will run the server.
```
python3 ip.py
```
- Put **hello.html** or any other similar HTML file in the same directory that the server is in. Run the server program:
```
python3 webserver.py
```
- From another host, open a browser and provide the corresponding URL. For example, **http://127.0.0.1:6789/hello.html**, where we use the port number **6789** after the colon following the IP address, matching the port number specified in **webserver.py**.


## EXAMPLE OUTPUT

- A successful run of **webserver.py**, where the browser displays the contents of **hello.html**.

[An image displaying the demonstration of a successful run of the web server](./success.png?raw=true "successful run")

- A successful demonstration of an attempt to get a file that is not present at the server, where the browser displays a "404 Not Found" message.

[An image displaying the demonstration of "404 Not Found" using the web server](./404.png?raw=true "404 demonstration")


![An image displaying the demonstration of a successful run of the web server](https://github.com/shioncm/web-server/blob/dda8421c72e27f990706f790192737403231eea6/success.png?sanitize=true)
<img src="https://github.com/shioncm/web-server/blob/dda8421c72e27f990706f790192737403231eea6/success.png?sanitize=true">


## AUTHOR

- Name: Shion M 


## FILE CREATION DATE 

2023-02-15
