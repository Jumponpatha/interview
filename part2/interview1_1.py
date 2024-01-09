# Import requests library
import requests

# Using get data from API link
x = requests.get('https://randomuser.me/api')

# print(x.status_code)
# print(x.text)

# Using if/else for checking status code equal 200
if x.status_code == 200:
    data = x.json()

    users = data['results']

    # Input data from API link to result
    for user in users:
        first_name = user['name']['first']
        last_name = user['name']['last']
        gender = user['gender']

    # Print the result firstname, lastname and gender
    print(f'First Name: {first_name} Last Name: {last_name} Gender: {gender}')
else:
    # Print the error
    print('ERROR API')