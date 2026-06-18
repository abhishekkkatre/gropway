import requests

url = 'https://jsonplaceholder.typicode.com/users/1'

response = requests.get(url)
data = response.json()

# print(f"name:{data['name']}")
# print(f"email:{data['email']}")
# print(f"city:{data['address']['city']}")
for user in data:
    print(f"name: {user['name']}- Email:{user['email']}")

a = [i for i in range(1,6)]
print(a)
even = [i for i in range(1,20) if i%2==0  ]

print(even)

