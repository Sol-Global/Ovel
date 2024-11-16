import numpy as np

def orbital_velocity(altitude_km):
    gravity = 6.67430e-11  # gravitational constant
    mass = 5.972e24  # mass of earth (kg)
    earth_radius = 6.371e6  # earth's radius (m)
    
    R = earth_radius + altitude_km * 1000  # convert altitude to meters
    v = np.sqrt(gravity * mass / R)
    return v

def escape_velocity(altitude_km):
    gravity = 6.67430e-11  # gravitational constant
    mass = 5.972e24  # mass of earth (kg)
    earth_radius = 6.371e6  # earth's radius (m)
    
    R = earth_radius + altitude_km * 1000  # convert altitude to meters
    v_escape = np.sqrt(2 * gravity * mass / R)
    return v_escape

# Ask user for the orbital altitude in kilometers
altitude_km = float(input("Enter the orbital altitude in kilometers: "))
velocity = orbital_velocity(altitude_km)
max_velocity = escape_velocity(altitude_km)

print(f"MINIMUM orbital velocity at {altitude_km} km altitude is {velocity:.2f} m/s")
print(f"MAXIMUM orbital velocity at {altitude_km} km altitude before reaching escape velocity is {max_velocity:.2f} m/s")