# building-material-cost-estimator

# Building Material Cost Estimator

A Python script to estimate the cost of flooring for rooms based on dimensions and chosen materials. It supports calculations for single or multiple rooms and allows saving project details to a file.

## Features

- **Calculate room area:** Computes the area of a room based on length and width.
- **Material cost estimation:** Supports flooring materials like Wood, Marble, and Tile, with predefined costs per square meter.
- **Multi-room calculations:** Allows users to calculate the total cost for multiple rooms.
- **Save project details:** Saves the calculated details to a user-specified file.

## Installation

1. Ensure Python 3.x is installed on your machine.
2. Download or clone the repository.
3. Place the script (`building_material_cost_estimator.py`) in your desired directory.

## Usage

1. Run the script:
   ```bash
   python building_material_cost_estimator.py

2. Follow the prompts to:
- Input room dimensions.
- Select a flooring material.
- Choose whether to calculate for multiple rooms.
- Save project details if desired.

## Example Output

```Welcome to Eli's Flooring Cost Calculator!
Enter the length of the room (in meters): 5
Enter the width of the room (in meters): 4
The area of the room is: 20.00 square meters.
Available materials: Wood, Marble, Tile
Please choose a material: Wood
The total cost for Wood flooring is: $300.00
Do you want to calculate for multiple rooms? (yes/no)
yes
Enter room dimensions. Type 'done' to finish.
Enter the length of the room (or 'done' to stop): 3
Enter the width of the room: 3
Enter the length of the room (or 'done' to stop): done
Total area of all rooms: 29.00 square meters.
Do you want to save the project details? (yes/no): yes
Enter the file name to save the details (e.g., project.txt): project.txt
Project details saved to project.txt.
