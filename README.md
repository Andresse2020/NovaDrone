# NovaDrone

Copyright © 2025 Andresse Brisel BASSINGA
Licensed under CERN Open Hardware Licence v2 – Weakly Reciprocal (CERN-OHL-W)

This project provides a complete hardware design for a professional UAV Quadcopter.
Firmware is proprietary and not covered by this licence.


## Project Overview
NovaDrone is a full hardware–firmware engineering project aiming to develop the **entire embedded electronics** of a quadcopter UAV **from scratch**.  
Rather than relying on off-the-shelf components, the project focuses on designing all critical subsystems: propulsion electronics, real-time motor control, power supervision, communication, diagnostics, and later, a fully custom flight controller.

The objective is to create a **professional-grade, reliable, and modular UAV platform** suitable for demanding embedded applications in robotics and aerospace.

---

## Key Features

- **Custom 1.5 kW Propulsion Board**  
  Single PCB integrating four 300–400 W ESCs and a dedicated supervisor MCU.

- **High-Performance ESC Subsystems**  
  STM32G4-based motor controllers using sensorless FOC, 48 kHz PWM, synchronized ADC sampling, and real-time telemetry.

- **Supervisor MCU**  
  Active precharge, power sequencing, battery monitoring, ARM/DISARM logic, watchdog, kill-line, USB monitoring, and DroneCAN communication.

- **Integrated Power Management**  
  LC filtering, TVS protection, OVP/UVLO/OCP/OTP, reinforced copper, and regulated 12 V / 5 V / 3.3 V rails.

- **Communication Architecture**  
  DroneCAN (CAN-FD) for propulsion telemetry and commands, UART CLI for debugging, USB streaming during development.

- **Custom Flight Controller (Next Stage)**  
  IMU fusion, stabilization, navigation logic, modular firmware architecture.

---

## Starting Point

NovaDrone uses a robust quadcopter frame as a mechanical platform for integration and testing:

- **Frame:** ZD550 carbon fiber  
- **Motors:** QM4208 brushless motors  
- **Propellers:** 1455 carbon fiber  

All electronics, power systems, and firmware are entirely custom-designed.

---

## Project Goals

NovaDrone aims to develop a **complete UAV electronics and firmware stack**, with emphasis on:

- High-efficiency propulsion and motor control  
- Intelligent and safe power management  
- Clean and maintainable firmware architecture  
- Robust diagnostics and system telemetry  
- Modular and scalable embedded design  
- Full control over every subsystem (no black boxes)

This is not a drone assembly project—**every subsystem is engineered from the ground up**.

---

## Architecture

### 1. Propulsion Board (1.5 kW)
A single PCB containing all propulsion-related electronics.

**Includes:**
- 4 × ESC (STM32G4)  
- 1 × Supervisor MCU  
- PSU: 12 V / 5 V / 3.3 V  
- Active precharge circuit  
- LC filtering, TVS, fuses  
- CAN-FD transceivers  
- USB and UART  
- XT60 (battery), XT30PW (motors), JST PH/SH, Tag-Connect SWD

---

### 2. ESC Subsystems (300–400 W each)

Each ESC is a fully independent motor controller.

**Features:**
- STM32G4 ARM Cortex-M4  
- Sensorless FOC  
- 48 kHz PWM  
- 24 kHz current loop  
- 1 kHz speed loop  
- Synchronized ADC sampling  
- Low-noise current sensing  
- Telemetry (current, voltage, RPM, temperature)  
- Bare-metal firmware (no HAL)

---

### 3. Supervisor MCU

Handles global power management and safety.

**Functions:**
- Active precharge (anti-inrush)  
- Battery voltage/current/temperature monitoring  
- Power sequencing  
- ARM/DISARM logic  
- Watchdog and kill-line  
- DroneCAN (CAN-FD) communication  
- **USB interface for development-time monitoring**  
- UART CLI  
- Planned: CAN bootloader

---

### 4. Integrated Power Management

Built directly into the propulsion board.

**Includes:**
- Input: LiPo 6S (18–25 V)  
- LC input filtering (PI filter)  
- TVS surge protection  
- OVP, UVLO, OCP, OTP protections  
- Reinforced copper planes  
- Regulated power rails (12 V / 5 V / 3.3 V)

---

### 5. Flight Control Unit (Upcoming)

The FCU will be developed after propulsion system validation.

**Planned capabilities:**
- STM32-based processing  
- IMU, barometer, magnetometer, GPS fusion  
- Kalman-based estimation  
- Stabilization loops  
- Trajectory and navigation control  

---

### 6. Communication System

| Interface | Purpose |
|-----------|---------|
| **DroneCAN (CAN-FD)** | ESC commands, propulsion telemetry, supervisor data |
| **USB** | High-rate logging and real-time monitoring during development |
| **UART CLI** | Debugging, tuning, calibration |
| **SWD** | Low-level flashing and debugging |

---

## Development Environment

NovaDrone firmware uses a custom modular embedded development environment built with **CMake**.





## Licence

Hardware design files are licensed under the CERN Open Hardware Licence v2 – Weakly Reciprocal (CERN-OHL-W).

The firmware is proprietary and not covered by this licence.
Commercial licences are available on request.
