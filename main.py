import eel
import pyowm

owm = pyowm.OWM("91953f5e93d65c4e7d7c5ddce18c437f")

@eel.expose
def get_weather(place):
	mgr = owm.weather_manager()

	observstion = mgr.weather_at_place(place)
	w = observstion.weather

	temp = w.temperature('celsius')['temp']

	return "In " + place + ", it's " + str(temp) + " degrees right now"


eel.init("web")
eel.start("main.html", size=(700, 700))