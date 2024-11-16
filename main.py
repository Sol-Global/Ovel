import numpy as np
import sys
from colorama import Fore, Style, Back, init as coloramaInit
import pyfiglet

coloramaInit()

altitude_limits = {
    'Mercury': {'min_altitude': 0, 'max_altitude': 1000},
    'Venus': {'min_altitude': 0, 'max_altitude': 250},
    'Earth': {'min_altitude': 0, 'max_altitude': 1000},
    'Mars': {'min_altitude': 0, 'max_altitude': 250},
    'Jupiter': {'min_altitude': 0, 'max_altitude': 5000},
    'Saturn': {'min_altitude': 0, 'max_altitude': 5000},
    'Uranus': {'min_altitude': 0, 'max_altitude': 5000},
    'Neptune': {'min_altitude': 0, 'max_altitude': 5000}
}

planets = {
    'Mercury': {'mass': 3.3011e23, 'radius': 2.4397e6},
    'Venus': {'mass': 4.8675e24, 'radius': 6.0518e6},
    'Earth': {'mass': 5.972e24, 'radius': 6.371e6},
    'Mars': {'mass': 6.4171e23, 'radius': 3.3895e6},
    'Jupiter': {'mass': 1.8982e27, 'radius': 6.9911e7},
    'Saturn': {'mass': 5.6834e26, 'radius': 5.8232e7},
    'Uranus': {'mass': 8.6810e25, 'radius': 2.5362e7},
    'Neptune': {'mass': 1.02413e26, 'radius': 2.4622e7}
}

def orbital_velocity(altitude_km, planet):
    gravity = 6.67430e-11  # gravitational constant
    mass = planets[planet]['mass']
    radius = planets[planet]['radius']
    
    R = radius + altitude_km * 1000  # convert altitude to meters
    v = np.sqrt(gravity * mass / R)
    return v

def escape_velocity(altitude_km, planet):
    gravity = 6.67430e-11  # gravitational constant
    mass = planets[planet]['mass']
    radius = planets[planet]['radius']
    
    R = radius + altitude_km * 1000  # convert altitude to meters
    v_escape = np.sqrt(2 * gravity * mass / R)
    return v_escape

ascii_banner = pyfiglet.figlet_format("Orbital Calculator")
print(Fore.CYAN + ascii_banner + Style.RESET_ALL)

# main
planet = input(Fore.YELLOW + "Enter the planet name: " + Style.RESET_ALL).capitalize()
if planet not in planets:
    print(Fore.RED + "Invalid planet name" + Style.RESET_ALL)
    sys.exit(1)
altitude_km = float(input(Fore.YELLOW + "Enter the orbital altitude in kilometers: " + Style.RESET_ALL))

# check for unrealistic altitude
min_altitude = altitude_limits[planet]['min_altitude']
max_altitude = altitude_limits[planet]['max_altitude']
if altitude_km < min_altitude or altitude_km > max_altitude:
    print(Fore.WHITE + Back.YELLOW + Style.BRIGHT + f"Warning: The entered altitude is unrealistic for {planet}. It should be between {min_altitude} km and {max_altitude} km." + Style.RESET_ALL)

print(Fore.GREEN + f"Calculating for planet: {planet}" + Style.RESET_ALL)

# call calculation functions
velocity = orbital_velocity(altitude_km, planet)
max_velocity = escape_velocity(altitude_km, planet)

# results
print(Fore.BLUE + f"\033[1mMinimum\033[0m orbital velocity at {altitude_km} km altitude on {planet} is {velocity:.2f} m/s" + Style.RESET_ALL)
print(Fore.MAGENTA + f"\033[1mMaximum\033[0m orbital velocity at {altitude_km} km altitude on {planet} before reaching escape velocity is {max_velocity:.2f} m/s" + Style.RESET_ALL)