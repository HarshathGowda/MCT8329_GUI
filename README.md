# MCT8329 Register Configuration GUI

## Overview

The **MCT8329 Register Configuration GUI** is a desktop application developed using **Python** and **PyQt5**. It provides a simple graphical interface for configuring the MCT8329 motor driver IC registers.

This GUI is intended as a **configuration and register calculation tool**. It allows users to modify register fields and view the corresponding register values.

> **Note:** This GUI does **not** communicate with the MCU or hardware directly. It is designed only for register configuration and visualization purposes.

---

## Features

- User-friendly graphical interface
- Register-wise configuration
- Bit-field level parameter editing
- Automatic register value calculation
- Register value display in Hexadecimal format
- Reset register values to default
- Copy generated register values
- Organized register categories for easy navigation

---

## Project Structure

```
HarshathGUI/
│
├── Main.py                 # Main application
├── registers_data.py       # Register definitions and field information
├── README.md
└── requirements.txt
```

---

## Requirements

- Python 3.10 or later
- PyQt5

Install the required package:

```bash
pip install PyQt5
```

or

```bash
pip install -r requirements.txt
```

---

## Running the Application

Navigate to the project directory and run:

```bash
python Main.py
```

---

## How It Works

1. Launch the application.
2. Select the required register.
3. Configure the available fields using the GUI.
4. The application automatically updates the corresponding register value.
5. Copy or record the generated register values for firmware development or manual programming.

---

## Important Note

This GUI is intended only for **register configuration**.

- ❌ No MCU communication
- ❌ No SPI communication
- ❌ No I2C communication
- ❌ No UART communication
- ❌ No live hardware register read/write

The displayed register values are generated based on the selected configuration options and are meant to assist firmware developers during implementation.

---

## Future Improvements

- SPI communication support
- USB/UART interface
- Live register read/write
- Import and export configuration files
- Register configuration profiles
- Device connection status

---

## Technologies Used

- Python
- PyQt5

---



## License

This project is provided for educational and development purposes.
