import requests
from tkinter import * 

# API key and URL
api_key = "9282b2f841257ebe05e6f62c986fb306"
url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

# Seach button executes here
def Search():
    city_search = city.get() 
    getWeather(city_search)

# Add button executes here    
def Add():
    city_add = city.get()   
    addList(city_add)  

# Function to get the weather for the visited weather list
def getWeather(city):
    Queue = []
    visited = []
    links = []
    #API request
    result = requests.get(url.format(city, api_key))

    if result:
        json = result.json()
        city = json['name']
        country = json['sys']['country']
        tempuratureK = json['main']['temp']
        tempurature = (tempuratureK - 273.15) * 9 / 5 + 32
        intTemp = '{:.1f}°F'.format(tempurature)
        weather = json['weather'][0]['main']
        final = (city, country, intTemp, weather)
    else:
        return None
    # Linked List that puts the searched city into the visited list
    for weather in final:
        links.append(weather)
        if weather not in visited and weather not in Queue:
            Queue.append(weather)
        else:
            visited.append(weather)

    while len(Queue):
        visited.append(Queue.pop(0))

    searchedCity.insert(END, str(visited) + '\n')
# Function to add the city to a personalized list        
def addList(city):
    weatherList = []
    result = requests.get(url.format(city, api_key))

    if result:
        json = result.json()
        city = json['name']
        country = json['sys']['country']
        tempuratureK = json['main']['temp']
        tempurature = (tempuratureK - 273.15) * 9 / 5 + 32
        formatedTemp = '{:.1f}°F'.format(tempurature)
        weather = json['weather'][0]['main']
        final = (city, country, formatedTemp, weather)
    else:
        return None
    for x in final:
        weatherList.append(x)


    outputSearch.insert(END, str(weatherList) + '\n')

# Set up window
app = Tk()
app.title("Weather API")
app.geometry('700x450')

# City search
city = StringVar()
city = Entry(app, textvariable=city)
city.pack()

# Search button
search = Button(app, text='Search for City', width=12, command=Search)
search.pack()

# Search output
searchedCity = Listbox(app,height=10, width=60)
searchedCity.pack()
 
# Add button 
addCity = Button(app, width=12, text='Add city to list', command=Add)
addCity.pack()

# Added output 
outputSearch = Listbox(app, height=10, width=60)
outputSearch.pack()

app.mainloop()

