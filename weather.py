# узнаем погода в местности
from pyowm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'  # your language
owm = OWM("98d685508325f6f34bbe349238921b94",config_dict)
mgr = owm.weather_manager()
observation = mgr.weather_at_place('Владикавказ, RU')
w = observation.weather
temp = w.temperature('celsius')['temp'] # температура сейчас
wind = w.wind()['speed'] # скорость ветра
pres = w.pressure['press']//1.333 # давление в мм
hum = w.humidity # влажность
statys = w.detailed_status
print(f'В Владикавказ сейчас  {temp} градусов по цельсию')
print(f'Скорость ветра - {wind} метра в секунду')
print(f'Атмосферное давление - {int(pres)} миллиметров ртутного столба')
print(f'Влажность - {hum} %')
print(f'Статус - {statys}')
