import requests
from config import API_KEY
#from json import loads, dumps
def make_api_request(city_name = "Hartford"):
    resp = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=fahrenheit&appid={API_KEY}')
    #print(resp.json())
    print(resp.json())
    return resp.json()

def parse_json(resp_json):
    if(resp_json['cod'] == 200):
        print(f"You searched up {resp_json['name']}")
        #print(resp_json['main']['temp'])
        print(f"The Current Temperature is {k_to_f(resp_json['main']['temp'])} F")
        print(f"The Current Weather is {(resp_json['weather'][0]['description'])}")
        return [k_to_f(resp_json['main']['temp']), (resp_json['weather'][0]['description'])]
    else:
        print("Invalid city, please try again!")

def k_to_f(k):
    '''Converts Kelvin to Fahrenheit'''
    return round(((k - 273.15) * 9/5) + 32)

if __name__ == "__main__":
    user_input = ""
    while user_input.lower() != "exit":
        user_input = input("Type in your city name, or type exit to quit: ")
        resp_json = make_api_request(user_input)
        parse_json(resp_json)