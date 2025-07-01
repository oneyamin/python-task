# ask user for temperature 
temperature = int(input('entert the current temperature in celsius'))
#check the temperature and give alert 
if temperature >= 30:
    print('its a hot day .stay hydrated')
elif 20 <= temperature <= 29:
    print('its a warm day . enjoy the weather ')
elif 10 <= temperature <= 19:
    print('itsa cool day. wear a jacket ')
else:
    print('its a cold day . stay warm')