import numpy as np
import sys
import os
import subprocess
from colorama import Fore, Style, Back, init as coloramaInit
import pyfiglet
# local imports
from planets import planets, altitude_limits

coloramaInit()
warning_newline_printed = False

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

def restart_program():
    global warning_newline_printed
    warning_newline_printed = False
    main()

def display_warning(message):
    global warning_newline_printed
    if not warning_newline_printed:
        print("")
        warning_newline_printed = True
    print(Fore.WHITE + Back.YELLOW + Style.BRIGHT + "Warning: " + message + Style.RESET_ALL)

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

def main():
    clearConsole()
    planet = input(Fore.YELLOW + "Enter the planet name: " + Style.RESET_ALL).capitalize()
    if planet not in planets:
        print(Fore.RED + "Invalid planet name" + Style.RESET_ALL)
        sys.exit(1)
    apoapsis_input = input(Fore.YELLOW + "Enter the apoapsis in kilometers: " + Style.RESET_ALL)
    periapsis_input = input(Fore.YELLOW + "Enter the periapsis in kilometers: " + Style.RESET_ALL)
    apoapsis_km = float(apoapsis_input.replace("km", "").replace(" ", ""))
    periapsis_km = float(periapsis_input.replace("km", "").replace(" ", ""))

    # swap if periapsis is greater than apoapsis
    if periapsis_km > apoapsis_km:
        apoapsis_km, periapsis_km = periapsis_km, apoapsis_km
        display_warning("Periapsis was greater than apoapsis. Values have been swapped.")

    # check for unrealistic altitude
    min_altitude = altitude_limits[planet]['min_altitude']
    max_altitude = altitude_limits[planet]['max_altitude']
    if apoapsis_km < min_altitude or apoapsis_km > max_altitude or periapsis_km < min_altitude or periapsis_km > max_altitude:
        display_warning(f"The entered altitudes may be unrealistic for {planet}. They should be between {min_altitude} km and {max_altitude} km.")

    print("")
    print(Fore.GREEN + f"Calculating for {planet}..." + Style.RESET_ALL)
    print("")

    # call calculation functions
    velocity_apoapsis = orbital_velocity(apoapsis_km, planet)
    velocity_periapsis = orbital_velocity(periapsis_km, planet)
    max_velocity_apoapsis = escape_velocity(apoapsis_km, planet)
    max_velocity_periapsis = escape_velocity(periapsis_km, planet)

    # results
    if apoapsis_km == periapsis_km:
        print(Fore.BLUE + f"\033[1mOrbital velocity\033[0m for circular orbit at {apoapsis_km} km on {planet} is {velocity_apoapsis:.6f} m/s" + Style.RESET_ALL)
        print(Fore.MAGENTA + f"\033[1mEscape velocity\033[0m for circular orbit at {apoapsis_km} km on {planet} is {max_velocity_apoapsis:.6f} m/s" + Style.RESET_ALL)
    else:
        print(Fore.BLUE + f"\033[1mMinimum\033[0m orbital velocity at apoapsis ({apoapsis_km} km) on {planet} is {velocity_apoapsis:.6f} m/s" + Style.RESET_ALL)
        print(Fore.BLUE + f"\033[1mMinimum\033[0m orbital velocity at periapsis ({periapsis_km} km) on {planet} is {velocity_periapsis:.6f} m/s" + Style.RESET_ALL)
        print(Fore.MAGENTA + f"\033[1mEscape velocity\033[0m at apoapsis ({apoapsis_km} km) on {planet} is {max_velocity_apoapsis:.6f} m/s" + Style.RESET_ALL)
        print(Fore.MAGENTA + f"\033[1mEscape velocity\033[0m at periapsis ({periapsis_km} km) on {planet} is {max_velocity_periapsis:.6f} m/s" + Style.RESET_ALL)

    print("")
    input(Fore.YELLOW + "Press Enter to start over..." + Style.RESET_ALL)
    restart_program()

if __name__ == "__main__":
    main()