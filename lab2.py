import requests
city = "Moscow, RU"
appid = "4087cc283e710b1560b8766038138667"
res2Day = requests.get("http://api.openweathermap.org/data/2.5/weather",
    params={'q': city, 'units': 'metric', 'lang': 'ru','APPID': appid,})
data2day = res2Day.json()
print("Прогноз погоды на день")
print("Город:", city)
print("Погодные условия:", data2day['weather'][0]['description'])
print("Температура:", data2day['main']['temp'])
print("Минимальная температура:", data2day['main']['temp_min'])
print("Максимальная температура", data2day['main']['temp_max'])
print("-----------")
resWeek = requests.get("http://api.openweathermap.org/data/2.5/forecast",
    params={'q': city, 'units': 'metric', 'lang': 'ru','APPID': appid,})
dataWeek = resWeek.json()
print("Прогноз погоды на неделю:")
for i in dataWeek['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <",
'{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодные условия <",
i['weather'][0]['description'], ">")
print("-----------")
print("Прогноз ветра и видимости на сегодня:")
print('Cкорость ветра: ', data2day['wind']['speed'], ' м/с')
print("Видимость: ", (data2day['visibility'] / 10000)*100, '%')
print('-----------')
print("Прогноз ветра и видимости на неделю:")
for i in dataWeek["list"]:
    print("Дата: ", i['dt_txt'],
    "\r\n Скорость ветра: ", i['wind']['speed'], ' м/с',
    "\r\n Видимость: ", round((i['visibility'] / 10000)*100), '%')