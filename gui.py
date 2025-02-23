# display GUI
import tkinter as tk

class ExoGUI:
    def __init__(self):
        self.root = tk.TK()
        self.root.title("Exoskeleton Monitor GUI")
        self.sensor_label = tk.Label(self.root, text="Sensor: Unknown", font=("Arial", 14))
        self.sensor_label.pack(pady=10)
        self.torque_label = tk.Label(self.root, text="Torque: 0.0 Nm", font=("Arial", 14))
        self.torque_label.pack(pady=10)
        self.gait_phase_label = tk.Label(self.root, text="Gait Phase: Unknown", font=("Arial", 14))
        self.gait_phase_label.pack(pady=10)
    
    #update GUI based on torque and gait phase
    def update(self, sensor_active, torque, gait_phase):
        if sensor_active:
            sensor_status = "Activated"
        else:
            sensor_status = "Inactive"
        
        self.sensor_label.config(text=f"Sensor: {sensor_status}")
        self.torque_label.config(text=f"Torque: {torque:.1f} Nm")
        self.gait_phase_label.config(text=f"Gait Phase: {gait_phase}")

    def run(self):
        self.root.mainloop()