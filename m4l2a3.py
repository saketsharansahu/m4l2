weather = (1,0,0,1,1,1,0,0,0,1)

sunny = weather.count(1)
rainy = weather.count(0)
if (sunny > rainy):
    print("good weather")
else:
    print("bad weather")
    
    