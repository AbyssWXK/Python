from urllib.parse import urlunparse
data= ['http','www.baidu.com','index.html','user','a=6','comment']
result = urlunparse(data)
print(result)