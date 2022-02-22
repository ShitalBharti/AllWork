from requests.auth import HTTPBasicAuth
import requests

# using Username and Password
basic = HTTPBasicAuth('123', 'abc')
response=requests.get('https://httpbin.org/basic-auth/123/abc', auth=basic)
print(response)
print(response.text)
print(response.json())
print()


# using API secret Key
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=da8d34a78c34c5764866b99d8baaaf4f'
city = 'Las Vegas'
status_code = requests.get(url.format(city))
print(status_code)
city_weather = requests.get(url.format(city)).json()
print(city_weather)
