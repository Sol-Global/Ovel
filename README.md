# Ovel

Ovel is a Python CLI app that calculates the orbital velocity around a planet based on the given orbital altitude (in kilometers).

![image](https://github.com/user-attachments/assets/b1ce35b3-d298-4aac-82ae-e4e00aa1e564)

## Run the Application Directly

### Linux
```bash
python3 -m venv venv
venv/bin/pip install -r requirements.txt
venv/bin/python3 main.py
```

### Windows
```bash
python -m venv venv
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
