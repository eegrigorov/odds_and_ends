from pyowm import OWM

owm = OWM('f24f64157f295b0305abe3a8b771f008')
mgr = owm.weather_manager()
place = input("Укажите населенный пункт: ")

observation = mgr.weather_at_place(place)
w = observation.weather
temp = w.temperature('celsius')["temp"]

print("В городе " + place + " сейчас " + w.detailed_status)
print("Температура: " + str(temp))