# Import requests library
import requests

def get_random_users(numbers):
    response = requests.get(f'https://randomuser.me/api/?results={numbers}')

    data = response.json()

    return data['results']

# print(response.status_code)
# print(response.text)

# Set number 20
users = get_random_users(20)

#probability = requests.get('https://api.genderize.io/?name=')
#for user in users:
    #f
for user in users:
    print(f"Name: {user['name']['first']} {user['name']['last']}, Gender: {user['gender']}")