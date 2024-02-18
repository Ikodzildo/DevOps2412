from math import pi

def radtodeg(rad):
    deg = rad*180/pi
    return deg

def degtorad(deg):
    rad = deg*pi/180
    return rad

print(f'from Radians to Degrees: {radtodeg(2)}')
print(f'from Degrees to Radians: {degtorad(180)}')


