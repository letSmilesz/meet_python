from requests import *

# responce = get('https://www.google.com/')
# print(responce)
# print(responce.status_code)
# print(responce.text)

api_key = '4321a3d417b53045aa1b6617c529c910'
city_name = 'Moscow'

responce = get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric&lang=ru')
print(responce.json())
weather = responce.json()['weather']
print()
print(weather[0]['description'])
temp = responce.json()['main']
print()
print(temp)

result = []
result.append(weather[0]['description'])
result.append(temp['temp'])
print(f'In {city_name} now is {result[0]} and temerature is {result[1]}')