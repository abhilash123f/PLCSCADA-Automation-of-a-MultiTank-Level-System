# Multi-Tank Level Control System

A simple PLC-SCADA project for automated level control of two tanks using Siemens TIA Portal and WinCC.

## Project Overview
This system monitors and controls water levels in two tanks using two pumps. The PLC handles pump sequencing, alarm management, and supports both manual and automatic operation modes.

## Folder Structure
- `/logic` - Ladder logic pseudocode and sequence descriptions
- `/hmi` - HMI screen descriptions for WinCC
- `/docs` - Process description and system overview

## System Features
- Automatic pump sequencing based on tank levels
- High-high and low-low alarm monitoring
- Manual/Auto mode switching
- Pump interlock protection
- Emergency stop functionality

## Hardware
- Siemens S7-1200/1500 PLC
- Level sensors (analog 4-20mA)
- Two pumps with motor starters
- WinCC HMI for visualization

## Optional Simulation
A small Python script (`simulate_tank_levels.py`) is included to simulate how Tank1 and Tank2 behave using the same auto-mode sequencing logic defined in `ladder_logic.txt`. This is only for visualization and does not replace an actual PLC program. Run it with `python simulate_tank_levels.py` to see tank levels, pump states, and alarms over time.

## Author
Student project for PLC programming course
