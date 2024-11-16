import numpy as np
import sys
from colorama import Fore, Style, Back, init as coloramaInit
import pyfiglet
# local imports
from planets import planets, altitude_limits

coloramaInit()

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
altitude_input = input(Fore.YELLOW + "Enter the orbital altitude in kilometers: " + Style.RESET_ALL)
altitude_km = float(altitude_input.replace("km", "").replace(" ", ""))

# check for unrealistic altitude
min_altitude = altitude_limits[planet]['min_altitude']
max_altitude = altitude_limits[planet]['max_altitude']
if altitude_km < min_altitude or altitude_km > max_altitude:
    print(Fore.WHITE + Back.YELLOW + Style.BRIGHT + f"Warning: The entered altitude may be unrealistic for {planet}. It should be between {min_altitude} km and {max_altitude} km." + Style.RESET_ALL)

print(Fore.GREEN + f"Calculating for planet: {planet}" + Style.RESET_ALL)

# call calculation functions
velocity = orbital_velocity(altitude_km, planet)
max_velocity = escape_velocity(altitude_km, planet)

# results
print(Fore.BLUE + f"\033[1mMinimum\033[0m orbital velocity at {altitude_km} km altitude on {planet} is {velocity:.2f} m/s" + Style.RESET_ALL)
print(Fore.MAGENTA + f"\033[1mMaximum\033[0m orbital velocity at {altitude_km} km altitude on {planet} before reaching escape velocity is {max_velocity:.2f} m/s" + Style.RESET_ALL)