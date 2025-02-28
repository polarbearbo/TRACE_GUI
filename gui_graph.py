import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time

class ExoGUI:
    def __init__(self):
        # parameters
        self.window_seconds = 30 # windows second (s)
        self.update_interval = 500 # Interval (ms)

        #set up gui
        self.root = tk.Tk()
        self.root.title("Exoskeleton Monitor GUI")
        self.root.protocol("WM_DELETE_WINDOW", self.on_close) 
        
        # max data point
        self.max_data_points = int(self.window_seconds * 1000 / self.update_interval)

        # Storing
        self.time_data = []
        self.torque_data = []
        self.start_time = time.time()
        
        # GUI parts
        self.create_widgets()
        self.setup_plot()
        
        # Simulation
        self.simulate_data_update()

        # Data
        # self.data_log = open("torque_data.csv", "w")
        # self.data_log.write("timestamp,torque,gait_phase\n")

    def create_widgets(self):
        # GUI
        status_frame = tk.Frame(self.root)
        status_frame.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.Y)
        
        self.sensor_label = tk.Label(status_frame, text="Sensor: Unknown", font=("Arial", 12))
        self.sensor_label.pack(pady=10, anchor="w")
        
        self.torque_label = tk.Label(status_frame, text="Torque: 0.0 Nm", font=("Arial", 12))
        self.torque_label.pack(pady=10, anchor="w")
        
        self.gait_phase_label = tk.Label(status_frame, text="Gait Phase: Unknown", font=("Arial", 12))
        self.gait_phase_label.pack(pady=10, anchor="w")

    def setup_plot(self):
        # initalization
        self.fig = Figure(figsize=(6, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.line, = self.ax.plot([], [], 'b-')

        # self.ax.set_ylim(0, 40)  # Y region
        # self.line.set_color('red')  # curve color
        # self.ax.axhline(y=30, color='r', linestyle='--')  

        # graph setting
        self.ax.set_title("Real-time Torque Monitoring")
        self.ax.set_xlabel("Time (s)")
        self.ax.set_ylabel("Torque (Nm)")
        self.ax.grid(True)
        
        # Tkinter
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def update_data_buffer(self):
        current_size = len(self.time_data)

        # cut the edge
        if current_size > self.max_data_points:
            self.time_data = self.time_data[-self.max_data_points:]
            self.torque_data = self.torque_data[-self.max_data_points:]

    def update(self, sensor_active, torque, gait_phase):
        # update the graph
        sensor_status = "Activated" if sensor_active else "Inactive"
        self.sensor_label.config(text=f"Sensor: {sensor_status}")
        self.torque_label.config(text=f"Torque: {torque:.1f} Nm")
        self.gait_phase_label.config(text=f"Gait Phase: {gait_phase}")
        
        # update the graph
        current_time = time.time() - self.start_time
        self.time_data.append(current_time)
        self.torque_data.append(torque)

        # Cut the edge
        self.update_data_buffer()
        
        self.line.set_data(self.time_data, self.torque_data)
        self.ax.relim()
        self.ax.autoscale_view()
        self.canvas.draw()

        #writing data
        # self.data_log.write(f"{time.time()},{torque},{gait_phase}\n")
    def simulate_data_update(self):
        simulated_torque = 20 + 5 * (time.time() % 3)  
        gait_phases = ["Heel Strike", "Mid Stance", "Toe Off"]
        
        self.update(
            sensor_active=True,
            torque=simulated_torque,
            gait_phase=gait_phases[int(time.time()*2) % 3]
        )
        self.root.after(500, self.simulate_data_update)  # 500ms

    def on_close(self):
        self.root.quit()
        self.root.destroy()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = ExoGUI()
    gui.run()
    