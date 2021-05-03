from urllib import request, parse
import json
from datetime import datetime
import locale
import math
locale.setlocale(locale.LC_ALL, 'ru_RU')

API_KEY = '38d24964d88167b58e762e1d2aaeaaf0'

URL = 'http://api.openweathermap.org/data/2.5/weather?q=Penza&lang=ru&appid=' + API_KEY
resp = request.urlopen(URL)
data = json.loads(resp.read().decode('utf-8'))
json.dump(data, open('weather.json', 'w'), indent=2, ensure_ascii=False)


def celsius(temperature):
    return str(math.ceil((temperature - 273.15) * 100) / 100) + '°C'


"""
N - North - Север
S - South - Юг
E - East - Восток
W - West - Запад
"""


def in_range(deg, start, end):
    ACCURANCY = 100
    deg = deg * ACCURANCY
    if start > end:
        return deg in range(int(start * ACCURANCY), 360 * ACCURANCY) \
            or deg in range(0, int(end * ACCURANCY))
    return deg in range(int(start * ACCURANCY), int(end * ACCURANCY))


def wind_direction(deg):
    if in_range(deg, 348.75, 11.25):
        return 'Северное'

    if in_range(deg, 11.25, 33.75):
        return "Северо-северо-восточное"

    if in_range(deg, 33.75, 56.25):
        return "Северо-восточное"

    if in_range(deg, 56.25, 78.75):
        return "Восточно-северо-восточное"

    if in_range(deg, 78.75, 101.25):
        return "Восточное"

    if in_range(deg, 101.25, 123.75):
        return "Восточно-юго-восточное"

    if in_range(deg, 123.75, 146.25):
        return "Юго-восточное"

    if in_range(deg, 146.25, 168.75):
        return "Юго-юго-восточное"

    if in_range(deg, 168.75, 191.25):
        return "Южное"

    if in_range(deg, 191.25, 213.75):
        return "Юго-юго-западное"

    if in_range(deg, 213.75, 236.25):
        return "Юго-западное"

    if in_range(deg, 236.25, 258.75):
        return "Западно-юго-западное"

    if in_range(deg, 258.75, 281.25):
        return "Западное"

    if in_range(deg, 281.25, 303.75):
        return "Западно-северо-западое"

    if in_range(deg, 303.75, 326.25):
        return "Северо-западое"

    if in_range(deg, 326.25, 348.75):
        return "Северо-северо-западое"


temp = """
Погода в городе Пенза на 18:53:33 27 aпреля 2021 г.:
 - 10°C, ощущается как 8°C
 - Минимальная темература: 10°С
 - Максимальная температура: 10°С
 - Переменная облачность
 - Атмосферное давление: 990 ммрс
 - Влажность воздуха: 33%
 - Облачность: 44%
 - Видимость: 100%


 Ветер:
  - Скорость: 3.17 м/с
  - Направление: Северо-западное

Закат: 19:20:36
Рассвет: 04:34:22
"""

date = datetime.fromtimestamp(data['dt']).strftime('%X %d %B %Y')
sunrise = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%X')
sunset = datetime.fromtimestamp(data['sys']['sunset']).strftime('%X')

print("Погода в городе", data['name'], "на", date, "г.:")
main = data['main']
print(' -', celsius(main['temp']) +
      ', ощущается как', celsius(main['feels_like']))
print(' - Минимальная темература:', celsius(main['temp_min']))
print(' - Максимальная температура:', celsius(main['temp_max']))

for weather in data['weather']:
    print(' -', weather['description'].title())

print(' - Атмосферное давление:', main['pressure'], 'ммрс')
print(' - Влажность воздуха:', str(main['humidity']) + '%')
print(' - Облачность:', str(data['clouds']['all']) + '%')
print(' - Видимость: %d%%' % (data['visibility'] / 100))

wind = data['wind']
print('\n Ветер:')
print('  - Скорость:', wind['speed'], 'м/с')
print('  - Направление:', wind_direction(wind['deg']))
print()
print('Закат:', sunset)
print('Рассвет:', sunrise)
