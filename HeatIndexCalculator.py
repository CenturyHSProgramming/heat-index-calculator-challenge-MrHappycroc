# HeatIndexCalculator.py
# Your job is to write a function in HeatIndexCalculator.py (call
# it **calculateHeatIndex()** that calculates the heat index
# factor based on the Heat Index Calculator from
# Calculator.net (http://www.calculator.net/heat-index-calculator.html)

# Define Function below
# be sure to return an integer

def calculateHeatIndex(humidity, tempature):
    h = humidity
    t = tempature
    c1 = -42.379
    c2 = 2.04901523
    c3 = 10.14333127
    c4 = -0.22475541
    c5 = -0.00683783
    c6 = -0.05481717
    c7 = 0.00122874
    c8 = 0.00085282
    c9 = -0.00000199
    index = c1 + (c2 * t) + (c3 * h) + (c4 * t * h) + (c5 * (t**2)) + (c6 * (h**2)) + (c7 * (t**2)*h)
    index = index + (c8 * t * (h**2))+(c9 * (t**2) * (h**2))


    return round(index)


if __name__ == '__main__':
    # Call the function in here if you want to test it
    # Make sure it's indented
    pass # remove or comment out this line if you wish to test the function



