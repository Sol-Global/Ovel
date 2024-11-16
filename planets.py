altitude_limits = {
    'Mercury': {'min_altitude': 200, 'max_altitude': 1500},  # avoids surface impacts and extreme temperatures
    'Venus': {'min_altitude': 250, 'max_altitude': 2000},   # atmosphere ends around 250 km
    'Earth': {'min_altitude': 160, 'max_altitude': 36_000}, # LEO to geostationary altitudes
    'Mars': {'min_altitude': 250, 'max_altitude': 20_000},  # includes areostationary orbits
    'Jupiter': {'min_altitude': 1_000, 'max_altitude': 200_000},  # avoids intense radiation belts
    'Saturn': {'min_altitude': 3_000, 'max_altitude': 200_000},  # safe distance from rings and atmosphere
    'Uranus': {'min_altitude': 5_000, 'max_altitude': 100_000},  # stability far from dense atmosphere
    'Neptune': {'min_altitude': 5_000, 'max_altitude': 100_000}  # stability due to extreme winds

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