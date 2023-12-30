# Latsami Luanglaj
# Lab 6 Challenge 3
# COP 2500
# 10/15/23

def temperature_convertion(temperature, modifier):
    temp_fahrenhiet = (temperature * 9/5) + 32
    if(modifier < 2 and modifier > -2):
        return temp_fahrenhiet
    else:
        return((temp_fahrenhiet)+(modifier // 2))

def to_cold(temperature, vacation):
    if(temperature < 70 and vacation == False):
        return True
    elif(temperature < 50 and vacation == True):
        return True
    else:
        return False

def main():
    a = temperature_convertion(0, 1)
    b = temperature_convertion(0, 5)
    c = temperature_convertion(0, -8)
    d = temperature_convertion(0 ,10)
    e = temperature_convertion(28, -1)
    f = temperature_convertion(12, 10)
    g = temperature_convertion(27, -2)
    h = temperature_convertion(25, 75)
    print("\ntemperature_convertion tests")
    print("temperature_convertion(0,1) -> 32.0 \tResult: %.1f"% a)
    print("temperature_convertion(0,5) -> 34.0 \tResult: %.1f"% b)
    print("temperature_convertion(0, -8) -> 28.0 \tResult: %.1f"% c)
    print("temperature_convertion(0 ,10) -> 37.0 \tResult: %.1f"% d)
    print("temperature_convertion(28, -1) -> 82.4 \tResult: %.1f"% e)
    print("temperature_convertion(12, 10) -> 58.6 \tResult: %.1f"% f)
    print("temperature_convertion(27, -2) -> 79.6 \tResult: %.1f"% g)
    print("temperature_convertion(25, 75) -> 114.0 \tResult: %.1f"% h)

    print("\nto_cold tests\nOnly work once temperature_convertion tests are correct")

    print("to_cold(a, True) -> True \tResult: ", to_cold(a, True))
    print("to_cold(a, False) -> True \tResult: ", to_cold(a, False))
    print("to_cold(e, True) -> False \tResult: ", to_cold(e, True))
    print("to_cold(e, False) -> False \tResult: ", to_cold(e, False))
    print("to_cold(f, True) -> False \tResult: ", to_cold(f, True))
    print("to_cold(f, False) -> True \tResult: ", to_cold(f, False))
main()
