# Import requests library
import requests

# Using get data from API link
response = requests.get('https://randomuser.me/api')

# print(response.status_code)
# print(response.text)

data = response.json()

users = data['results']

# Input data from API link to result
for user in users:
    first_name = user['name']['first']
    last_name = user['name']['last']
    gender = user['gender']

probability = requests.get('https://api.genderize.io/?name=')
for user in users:
    f

# Print the result firstname, lastname and gender
print(f'First Name: {first_name} Last Name: {last_name} Gender: {gender}')