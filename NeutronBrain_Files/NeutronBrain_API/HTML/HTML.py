import re
Text = """

<html>
<head>
<title>Login to ForTHelL</title>
<link rel="stylesheet" href="loginnet.css">
</head>
<body>
<br>
<header>
<h1 class="title">Login to FortHell.net</h1>
<h4 class="subtitle">This page is for user of FortHell Firewall</h4> 
</header>

<article id="login">
<form method="post">
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<input  class="pass" type="password" placeholder="say the magic word " name   ="sandi"/><br><br>
<input class="submit" type  ="submit" formmethod="post" value="Login" name="name">
</form>
</article>
</body>
</html>
"""

request_file = b'GET /image.jpg HTTP/1.1\r\nHost: 127.0.0.1\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'
request = b'GET / HTTP/1.1\r\nHost: 127.0.0.1\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'
post = b'POST / HTTP/1.1\r\nHost: 192.168.43.171\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nReferer: http://192.168.43.171/\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 49\r\n\r\nusername=nivek&password=kevin&tombol=Submit+Query'
post_with_addr = b'POST /APA_YA HTTP/1.1\r\nHost: 127.0.0.1\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nReferer: http://127.0.0.1/APA_YA\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 49\r\n\r\nusername=kevin&password=nivek&tombol=Submit+Query'
post_with_addr1 = b'POST /APA_YA/mantap.jpg HTTP/1.1\r\nHost: 127.0.0.1\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nReferer: http://127.0.0.1/APA_YA\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 49\r\n\r\nusername=kevin&password=nivek&tombol=Submit+Query'
post_with_addr2 = b'POST /APA_YA/mantap.jpg|Proses1 HTTP/1.1\r\nHost: 127.0.0.1\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nReferer: http://127.0.0.1/APA_YA\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 49\r\n\r\nusername=kevin&password=nivek&tombol=Submit+Query'
polos = b'GET / HTTP/1.1\r\nHost: 192.168.43.171\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'
multiget = b'GET /?kwowowooww=kkkkkk&okeoke=jmolvqml HTTP/1.1\r\nHost: 127.0.0.1\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'
multiget1 = b'GET /?kwowowooww=kkkkkk&okeoke=jmolvqml&kevinagusto HTTP/1.1\r\nHost: 127.0.0.1\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'
get1 = b'GET /?kwowowooww=kkkkkk HTTP/1.1\r\nHost: 127.0.0.1\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'
get2 = b'GET /loginnet/index.html?test=mantap&oop=bagus&testdoangk HTTP/1.1\r\nHost: 127.0.0.1\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'
get3 = b'GET /loginnet/index.html?test=mantap&oop=bagus&testdoangk|/loginnet/test.js HTTP/1.1\r\nHost: 127.0.0.1\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'

getgoogle = b'HTTP/1.1 301 Moved Permanently\r\nLocation: http://www.google.com/\r\nContent-Type: text/html; charset=UTF-8\r\nDate: Mon, 21 May 2018 12:24:16 GMT\r\nExpires: Wed, 20 Jun 2018 12:24:16 GMT\r\nCache-Control: public, max-age=2592000\r\nServer: gws\r\nContent-Length: 219\r\nX-XSS-Protection: 1; mode=block\r\nX-Frame-Options: SAMEORIGIN\r\n\r\n<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">\n<TITLE>301 Moved</TITLE></HEAD><BODY>\n<H1>301 Moved</H1>\nThe document has moved\n<A HREF="http://www.google.com/">here</A>.\r\n</BODY></HTML>\r\n'
http_code = [
 ["Code 100", "100", "Informational Responses", "Continue"],
    ["Code 101", "101", "Informational Responses", "Switching Protocols"],
    ["Code 102", "102", "Informational Responses", "Processing"],
    ["Code 103", "103", "Informational Responses", "Early_Hints"],   

    ["Code 200", "200", "Success", "OK"],
    ["Code 201", "201", "Success", "Created"],
    ["Code 202", "202", "Success", "Accepted"],
    ["Code 203", "203", "Success", "Non-Authoritative Information"],
    ["Code 204", "204", "Success", "No Content"],
    ["Code 205", "205", "Success", "Reset Content"],
    ["Code 206", "206", "Success", "Partial Content"],
    ["Code 207", "207", "Success", "Multi-Status"],
    ["Code 208", "208", "Success", "Already Reported"],
    ["Code 226", "226", "Success", "IM Used"],


    ["Code 300", "300", "Redirection", "Multiple Choices"],
    ["Code 301", "301", "Redirection", "Moved Permanently"],
    ["Code 302", "302", "Redirection", "Found"],
    ["Code 303", "303", "Redirection", "See Other"],
    ["Code 304", "304", "Redirection", "Not Modified"],
    ["Code 305", "305", "Redirection", "Use Proxy"],
    ["Code 306", "306", "Redirection", "Switching Proxy"],
    ["Code 307", "307", "Redirection", "Temporary Redirect"],
    ["Code 308", "308", "Redirection", "Permanent Redirect"],

    ["Code 400", "400", "Client Error", "Bad Request"],
    ["Code 401", "401", "Client Error", "Unauthorized"],
    ["Code 402", "402", "Client Error", "Payment Required"],
    ["Code 403", "403", "Client Error", "Forbidden"],
    ["Code 404", "404", "Client Error", "Not Found"],
    ["Code 405", "405", "Client Error", "Method Not Allowed"],
    ["Code 406", "406", "Client Error", "Not Acceptable"],
    ["Code 407", "407", "Client Error", "Proxy Authentication Required"],
    ["Code 408", "408", "Client Error", "Request Timeout"],
    ["Code 409", "409", "Client Error", "Conflict"],
    ["Code 410", "410", "Client Error", "Gone"],
    ["Code 411", "411", "Client Error", "Length Required"],
    ["Code 412", "412", "Client Error", "Precondition Failed"],
    ["Code 413", "413", "Client Error", "Payload Too Large"],
    ["Code 414", "414", "Client Error", "URI Too Long"],
    ["Code 415", "415", "Client Error", "Unsupported Media Type"],
    ["Code 416", "416", "Client Error", "Range Not Satisfied"],
    ["Code 417", "417", "Client Error", "Exception Failed"],
    ["Code 418", "418", "Client Error", "I'm a teapot"],
    ["Code 421", "421", "Client Error", "Misdirected Request"],
    ["Code 422", "422", "Client Error", "Unprocessable Entity"],
    ["Code 423", "423", "Client Error", "Locked"],
    ["Code 424", "424", "Client Error", "Failed Depency"],
    ["Code 426", "426", "Client Error", "Upgrade Required"],
    ["Code 428", "428", "Client Error", "Precondition Required"],
    ["Code 429", "429", "Client Error", "Too Many Requests"],
    ["Code 431", "431", "Client Error", "Request Header Fields Too Lage"],
    ["Code 451", "451", "Client Error", "Unavailable For Legal Reasons"],

    ["Code 500", "500", "Server Error", "Internal Server Errors"],
    ["Code 501", "501", "Server Error", "Not Implentable"],
    ["Code 502", "502", "Server Error", "Bad Gateway"],
    ["Code 503", "503", "Server Error", "Service Unavailble"],
    ["Code 504", "504", "Server Error", "Gateway Timeout"],
    ["Code 505", "505", "Server Error", "HTTP Version Not Supported"],
    ["Code 506", "506", "Server Error", "Variant Also Negotiates"],
    ["Code 507", "507", "Server Error", "Insufficient Storage"],
    ["Code 508", "508", "Server Error", "Loop Detected"],
    ["Code 509", "509", "Server Error", "Not Extended"],
    ["Code 510", "510", "Server Error", ""],
    ["Code 511", "511", "Server Error", "Network  Authentication Required"],
    ["Code 512", "512", "Server Error", ""]

]
def Generate_HTTP(code, header={}, data=b""):
 header_default = {b"Content-Length": str(len(data)).encode("utf-8")} 
 message = ""
 for i in http_code:
  if (i[1]==code.decode("utf-8")):
   message = i[3]
   
 http = b"HTTP/1.1 %s %s\r\n" %(code, message.encode("utf-8"))
 
 for i in header:
  http+=i+b": "+header[i]+b"\r\n"

 for i in header_default:
  http+=i+b": "+header_default[i]+b"\r\n"
  
 http+=b"\r\n\r\n"+data
 return http

def Remove_Empty(arg):
 to_return = []
 for i in arg:
  if i==b"":
   continue
  to_return.append(i)
 return to_return
def POST(data):
 to_return = {} 
 pemisah = [":", "="]
 #header
 header = data.split(b"\r\n")[0];
 header = header.split(b" ")
 header_name = [b"method",  b"action", b"protocol"]
 for i in range(len(header)):
  to_return[header_name[i]] = header[i].strip(b"/")
 
 #handling multiple action
 to_return[b"action"] = to_return[b"action"].split(b"|")
 

 #content body
 inputt = {}
 
 body = data.replace(b"&", b"\r\n").split(b"\r\n")[1:]
 for i in body:
  pemisahh = b""
  for a in pemisah:
   if (a.encode("utf-8") in i):
    pemisahh = a.encode("utf-8")
    break
  if (pemisahh==b""):
   to_return[i.strip(b" ").rstrip(b" ")] = b""
  else:
   if (pemisahh==b"="):
    temp = i.split(pemisahh)
    inputt[temp[0].strip(b" ").strip(b"/").rstrip(b" ")] = temp[1].strip(b" ").rstrip(b" ")
   else:
    temp = i.split(pemisahh)
    to_return[temp[0].strip(b" ").rstrip(b" ")] = temp[1].strip(b" ").rstrip(b" ")
  pemisahh = b""
 to_return[b"input"] = inputt
 
 return to_return


def GET(data):
 to_return = {} 
 pemisah = [":", "="]
 #header
 header = data.split(b"\r\n")[0];
 header = header.split(b" ")
 header_name = [b"method",  b"action", b"protocol"]
 for i in range(len(header)):
  to_return[header_name[i]] = header[i]

 #content body
 body = data.split(b"\r\n")[1:]
 for i in body:
  pemisahh = b""
  for a in pemisah:
   if (a.encode("utf-8") in i):
    pemisahh = a.encode("utf-8")
    break
  if (pemisahh==b""):
   to_return[i.strip(b" ").rstrip(b" ")] = b""
  else:
   temp = i.split(pemisahh)
   to_return[temp[0].strip(b" ").rstrip(b" ")] = temp[1].strip(b" ").rstrip(b" ")
   pemisahh = b""
 
 
 #processing action and input
 temp0 = to_return[b"action"].split(b"|")
 temp1 = {}
 for i in temp0:
  i = i.strip(b"/")
  
  if (b"?" in i):
   a = i.split(b"?")
   head = a[0]
   args=a[1:]
   for b in range(len(args)):
    args[b] = args[b].split(b"&")
   args = args[0]
   argss = {}
   
   for c in range(len(args)):
    pemisahh = b""
    for d in pemisah:
     symb = d.encode("utf-8")
     if (symb in args[c]):
      pemisahh = symb
      break
    if (pemisahh==b"") :
     argss[args[c]] = b""
    else:
     pisahkan = args[c].split(pemisahh)
     argss[pisahkan[0]] = pisahkan[1]
    
   temp1[head]  = argss
  else:
   temp1[i] = b""
 del to_return[b"action"];
 to_return[b"input"] = temp1
 return to_return

def Get_Method(data):
 return data.split(b"\r\n")[0].split(b" ")[0]
def Get_Data(data):
 if (Get_Method(data)==b"GET"):
  return GET(data)
 if (Get_Method(data)==b"POST"):
  return POST(data)
 else:
  return (Generate_HTTP(b"404", header={b"Location": b"https://www.google.com"})) 
 
if __name__=="__main__":
 print(Generate_HTTP(b"404", header={b"Location": b"https://www.google.com"}))