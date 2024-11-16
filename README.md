# Ovel

Ovel is a Python CLI app that lets you calculate the minimum and maximum orbital velocity around a planet, using the given orbital altitude (in kilometers).

## Run the Application

### Linux
```sh
pip install -r requirements.txt && python3 main.py
```

### Windows
```sh
pip install -r requirements.txt && python main.py
```

## Building/Compiling the Application

### Windows
To build the application to an executable, run:
```sh
./build.ps1
```
This uses PyInstaller to create an executable file that bundles the Python runtime and any dependencies.

You can find the standalone executable in the `dist` folder.

## Usage

Run the application and follow the prompts to input the necessary data for calculating orbital velocities.