def coll(data):
    weatherfile = open("weather.txt", "w")
    for dict in data:
        j = 0

        for category in dict.values():
            j += 1
            weatherfile.write(str(j) + ', ' + str(category) + ';\n')

    weatherfile.close()
    return 'Donezo! Take a look at weather.csv and see the results!'

def txt(data, name, mod):
    weatherfile = open(name, mod)
    for dict in data:
        j = 0
        for category in dict.values():
            j += 1
            weatherfile.write(str(category) + '\n')
            if j == 22:
                return

    weatherfile.close()
    return 'Donezo! Take a look at weather.txt!'

def txtarchive(data, name):
    for dict in data[1:]:
        txt(data, name, "a")
