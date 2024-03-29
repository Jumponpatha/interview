# Import requests library
import requests
import pandas as pd

# Function get data from API link with numbers
def get_random_users(numbers):
    response = requests.get(f'https://randomuser.me/api/?results={numbers}')

    data = response.json()

    return data['results']

# print(response.status_code)
# print(response.text)

# Set number 20 users
users = get_random_users(20)

# Create DataFrame with columns 'first_name', 'last_name', and 'gender(actual)'.
df = pd.DataFrame(columns=['first_name', 'last_name', 'gender(actual)'])

# For-loop to loop first_name, last_name and gender_actual
for user in users:
    first_name = user['name']['first']
    last_name = user['name']['last']
    gender_actual = user['gender']

    user_df = {'first_name': first_name, 'last_name': last_name, 'gender(actual)': gender_actual}
    df = pd.concat([df, pd.DataFrame([user_df])], ignore_index=True)

prediction = []

# For loop get probability response from API link
for index, row in df.iterrows():
    name = row['first_name']
    response = requests.get(f'https://api.genderize.io/?name={name}')
    prediction_data = response.json()

    gender_predict = prediction_data.get('gender')
    probability = prediction_data.get('probability')

    # Append function to add data in row gender_predict and probability
    prediction.append({'gender(predict)': gender_predict, 'probability': probability})

# Create dataframe with columns gender(actual) and probability, then add to df.
predict_df = pd.DataFrame(prediction)
df = pd.concat([df, predict_df], axis=1)

# Testing the prediction and actual gender (Boolean)
df['same_gender'] = df['gender(actual)'] == df['gender(predict)']

# Print the DataFrame
display(df)
