import tkinter as tk
from tkinter import ttk

class ExoGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Exoskeleton Monitor GUI")

        # Main container using grid layout
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Left panel for status information
        self.left_frame = ttk.Frame(self.main_frame)
        self.left_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        # Information labels
        self.locomotion_label = ttk.Label(self.left_frame,
                                          text="Locomotion: Unknown",
                                          font=("Arial", 14))
        self.locomotion_label.pack(pady=10, anchor=tk.W)

        self.terrain_label = ttk.Label(self.left_frame,
                                       text="Terrain: Unknown",
                                       font=("Arial", 14))
        self.terrain_label.pack(pady=10, anchor=tk.W)

        self.gait_phase_label = ttk.Label(self.left_frame,
                                          text="Gait Phase: Unknown",
                                          font=("Arial", 14))
        self.gait_phase_label.pack(pady=10, anchor=tk.W)

        # Right panel for torque display
        self.right_frame = ttk.Frame(self.main_frame, padding="20")
        self.right_frame.pack(side=tk.RIGHT, fill=tk.Y)

        # Torque display components
        self.torque_label = ttk.Label(self.right_frame,
                                      text="Torque",
                                      font=("Arial", 14, "bold"))
        self.torque_label.pack(pady=5)

        # Canvas for torque bar
        self.canvas_height = 200
        self.canvas_width = 80
        self.torque_canvas = tk.Canvas(self.right_frame,
                                       width=self.canvas_width,
                                       height=self.canvas_height,
                                       bg="#f0f0f0",
                                       highlightthickness=0)
        self.torque_canvas.pack(pady=10)

        # Create initial torque bar
        self.bar_width = 40
        self.torque_bar = self.torque_canvas.create_rectangle(
            (self.canvas_width - self.bar_width) // 2, self.canvas_height,  # x1, y1
            (self.canvas_width + self.bar_width) // 2, self.canvas_height,  # x2, y2
            fill="green",
            outline=""
        )

        # Numerical torque value display
        self.torque_value_label = ttk.Label(self.right_frame,
                                            text="0 Nm",
                                            font=("Arial", 12))
        self.torque_value_label.pack(pady=5)

    def calculate_color(self, torque):
        """Calculate color based on torque value (0-100)"""
        torque = max(0, min(100, torque))
        if torque <= 50:
            red = int(255 * (torque / 50))
            green = 255
        else:
            red = 255
            green = int(255 * (1 - (torque - 50) / 50))
        return f"#{red:02x}{green:02x}00"

    def update(self, locomotion, terrain_info, gait_phase):
        self.locomotion_label.config(text=f"Locomotion: {locomotion}")
        self.terrain_label.config(text=f"Terrain: {terrain_info}")
        self.gait_phase_label.config(text=f"Gait Phase: {gait_phase}")

    def update_torque(self, torque):
        """Update torque display with color-changing bar"""
        torque = max(0, min(100, torque))
        bar_height = (torque / 100) * self.canvas_height

        # Update bar position and color
        self.torque_canvas.coords(self.torque_bar,
                                  (self.canvas_width - self.bar_width) // 2,
                                  self.canvas_height - bar_height,
                                  (self.canvas_width + self.bar_width) // 2,
                                  self.canvas_height)

        color = self.calculate_color(torque)
        self.torque_canvas.itemconfig(self.torque_bar, fill=color)

        # Update numerical value
        self.torque_value_label.config(text=f"{torque} Nm")

    def run(self):
        self.root.mainloop()

    def on_close(self):
        self.root.quit()
        self.root.destroy()
if __name__ == "__main__":
    gui = ExoGUI()


    # Example simulation (remove in actual implementation)
    def simulate_torque():
        torque = 0
        # while True:
        #     gui.update_torque(torque)
        #     torque = (torque + 1) % 101
        #     gui.root.update()
        #     gui.root.after(50)


    gui.root.after(100, simulate_torque)
    gui.run()