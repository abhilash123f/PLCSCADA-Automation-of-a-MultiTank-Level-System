import matplotlib.pyplot as plt

# Initial conditions
tank1_level = 50.0
tank2_level = 50.0
pump1_on = False
pump2_on = False

# Simulation parameters
time_step = 1  # seconds
total_time = 300
fill_rate = 0.8  # % per second when pump is on
drain_rate = 0.3  # % per second (natural drainage)

# Storage for plotting
time_data = []
tank1_data = []
tank2_data = []
pump1_data = []
pump2_data = []
alarm_hh_data = []
alarm_ll_data = []

# Run simulation
for t in range(0, total_time, time_step):
    # Auto mode logic for Pump1
    if tank1_level < 30:
        pump1_on = True
    elif tank1_level > 80:
        pump1_on = False
    
    # Auto mode logic for Pump2 (interlock: only if Pump1 is running)
    if pump1_on:
        if tank2_level < 25:
            pump2_on = True
        elif tank2_level > 75:
            pump2_on = False
    else:
        pump2_on = False
    
    # Update tank levels
    if pump1_on:
        tank1_level += fill_rate * time_step
    tank1_level -= drain_rate * time_step
    
    if pump2_on:
        tank2_level += fill_rate * time_step
    tank2_level -= drain_rate * time_step
    
    # Keep levels in bounds
    tank1_level = max(0, min(100, tank1_level))
    tank2_level = max(0, min(100, tank2_level))
    
    # Check alarms
    alarm_hh = tank1_level >= 95
    alarm_ll = tank1_level <= 10
    
    # Store data
    time_data.append(t)
    tank1_data.append(tank1_level)
    tank2_data.append(tank2_level)
    pump1_data.append(1 if pump1_on else 0)
    pump2_data.append(1 if pump2_on else 0)
    alarm_hh_data.append(1 if alarm_hh else 0)
    alarm_ll_data.append(1 if alarm_ll else 0)

# Plot results
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))

# Tank levels
ax1.plot(time_data, tank1_data, label='Tank1', color='blue')
ax1.plot(time_data, tank2_data, label='Tank2', color='green')
ax1.axhline(y=30, color='gray', linestyle='--', linewidth=0.8)
ax1.axhline(y=80, color='gray', linestyle='--', linewidth=0.8)
ax1.set_ylabel('Level (%)')
ax1.set_title('Tank Levels Over Time')
ax1.legend()
ax1.grid(True)

# Pump states
ax2.plot(time_data, pump1_data, label='Pump1', color='orange', linewidth=2)
ax2.plot(time_data, pump2_data, label='Pump2', color='red', linewidth=2)
ax2.set_ylabel('Pump State')
ax2.set_title('Pump Status (1=ON, 0=OFF)')
ax2.legend()
ax2.grid(True)

# Alarms
ax3.plot(time_data, alarm_hh_data, label='High-High Alarm', color='red', linewidth=2)
ax3.plot(time_data, alarm_ll_data, label='Low-Low Alarm', color='yellow', linewidth=2)
ax3.set_xlabel('Time (seconds)')
ax3.set_ylabel('Alarm State')
ax3.set_title('Alarm Status (1=Active, 0=Inactive)')
ax3.legend()
ax3.grid(True)

plt.tight_layout()
plt.savefig('simulation_results.png')
print("Simulation complete. Results saved to simulation_results.png")
plt.show()
