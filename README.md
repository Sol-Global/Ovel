# Ovel

Ovel is a Python CLI app that calculates the minimum and maximum orbital velocity around a planet based on the given orbital altitude (in kilometers).

## Run the Application Directly

### Linux
```bash
python3 -m venv venv
venv/bin/pip install -r requirements.txt
venv/bin/python main.py
```

### Windows
```bash
python3 -m venv venv
.venv\Scripts\pip.exe install -r requirements.txt
.venv\Scripts\python.exe main.py
```

## Building the Application

### Windows
To build the application into an executable, run:
```sh
./build.ps1
```
This uses PyInstaller to create a standalone executable, which can be found in the `dist` folder.

## Usage

Run the application and follow the prompts to input the necessary data for calculating orbital velocities.