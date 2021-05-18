from urllib import request, parse
import json
from datetime import datetime
import locale
import math
locale.setlocale(locale.LC_ALL, 'ru_RU')

API_KEY = '38d24964d88167b58e762e1d2aaeaaf0'

def get_data():
    URL = 'http://api.openweathermap.org/data/2.5/weather?q=Penza&lang=ru&appid=' + API_KEY
    resp = request.urlopen(URL)
    data = json.loads(resp.read().decode('utf-8'))
    json.dump(data, open('weather.json', 'w'), indent=2, ensure_ascii=False)
    return data


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


def get_weather():
    data = get_data()
    date = datetime.fromtimestamp(data['dt']).strftime('%X %d %B %Y')
    sunrise = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%X')
    sunset = datetime.fromtimestamp(data['sys']['sunset']).strftime('%X')
    main = data['main']
    wind = data['wind']

    res = ' '.join(("Погода в городе", data['name'], "на", date, "г.:")) + '\n'
    res += ' '.join((' -', celsius(main['temp']) +
        ', ощущается как', celsius(main['feels_like']))) + '\n'
    res += ' '.join((' - Минимальная темература:', celsius(main['temp_min']))) + '\n'
    res += ' '.join((' - Максимальная температура:', celsius(main['temp_max']))) + '\n'

    for weather in data['weather']:
        res += ' '.join((' -', weather['description'].title())) + '\n'

    res += ' '.join((' - Атмосферное давление:', str(main['pressure']), 'ммрс')) + '\n'
    res += ' '.join((' - Влажность воздуха:', str(main['humidity']) + '%')) + '\n'
    res += ' '.join((' - Облачность:', str(data['clouds']['all']) + '%')) + '\n'
    res += ' - Видимость: %d%%\n\n' % (data['visibility'] / 100)

    res += '  Ветер:\n' + '\n'
    res += ' '.join(('  - Скорость:', str(wind['speed']), 'м/с')) + '\n'
    res += ' '.join(('  - Направление:', wind_direction(wind['deg']))) + '\n\n'
    res += ' '.join(('Закат:', sunset)) + '\n'
    res += ' '.join(('Рассвет:', sunrise)) + '\n'

    return res


if __name__ == '__main__':
    print(get_weather())
