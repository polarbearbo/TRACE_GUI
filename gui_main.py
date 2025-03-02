from gui import ExoGUI
import os
import csv
import random

def load_random_csv(data_folder="Data"):
    csv_files = [f for f in os.listdir(data_folder) if f.endswith('.csv')]
    if not csv_files:
        raise FileNotFoundError("No CSV files found")

    selected_file = random.choice(csv_files)
    file_path = os.path.join(data_folder, selected_file)

    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)  # Use DictReader to access columns by name
        for row in reader:
            locomotion = int(row['locomotion_mode'])
            terrain = int(row['terrain_info'])
            gait_phase = int(row['gait_phase'])
            data.append((locomotion, terrain, gait_phase))
    return data

if __name__ == "__main__":
    gui = ExoGUI()
    data = load_random_csv()

    def update_gui(index=0):
        if index < len(data):
            locomotion, terrain, gait_phase = data[index]
            print(locomotion, terrain, gait_phase)
            gui.update(locomotion, terrain, gait_phase)
            gui.root.after(2000, update_gui, index + 1)

    update_gui(0)
    gui.run()