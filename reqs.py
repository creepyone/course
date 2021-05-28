from requests import request

q1 = request(url="http://127.0.0.1:5000/database/movies", method="get")
print(q1.content)
