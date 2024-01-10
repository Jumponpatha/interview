# Import requests library
import requests
import pandas as pd

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
    first_name = user['name']['first']
    last_name = user['name']['last']
    gender_actual = user['gender']

    df1 = pd.DataFrame(columns=['first_name', 'last_name', 'gender_actual'])
print(df1)