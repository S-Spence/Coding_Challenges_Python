# a string of lights starts off. Loop through n times toggling the nth light on and off

def string_lights(n: int)-> int:

    lights = [0 for i in range(n)]

    for i in range(1, n+1):
        for j in range(0, len(lights), i):
        
            if lights[j] == 0:
                lights[j] = 1
            else:
                lights[j] = 0

        print(lights)
    return sum(lights)


print(string_lights(5))



