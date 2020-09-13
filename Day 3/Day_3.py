altitude = int(input())
if altitude<1000:
    print("Safe to land")
elif altitude<5000:
    print("Come down to 5000ft")
else:
    print("Try again")
