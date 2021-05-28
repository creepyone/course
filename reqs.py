from requests import request

q1 = request("get", "http://127.0.0.1:5000/database/movies")
print(q1.content)