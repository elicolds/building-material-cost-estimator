def calculate_area(length, width):
    """Calculate the area of the room."""
    return length * width

def get_material_cost(material):
    """Return the cost per square meter of the chosen material."""
    materials = {
        'wood': 15.0,  # Cost per square meter in dollars
        'marble': 20.0,
        'tile': 30.0,
    }
    return materials.get(material.lower(), None)

def save_project_details(file_name, details):
    """Save project details to a file."""
    with open(file_name, 'w') as file:
        file.write(details)
def calculate_total_cost_for_rooms():
    """Calculate the total cost for multiple rooms."""
    total_area = 0
    print("Enter room dimensions. Type 'done' to finish.")
    while True:
        try:
            length = input("Enter the length of the room (or 'done' to stop): ")
            if length.lower() == 'done':
                break
            length = float(length)
            width = float(input("Enter the width of the room: "))
            total_area += calculate_area(length, width)
        except ValueError:
            print("Invalid input. Please enter numbers only.")
    
    print(f"Total area of all rooms: {total_area:.2f} square meters.")
    return total_area

def main():
    print("Welcome to Eli's Flooring Cost Calculator!")
    
    # Get room dimensions
    try:
        length = float(input("Enter the length of the room (in meters): "))
        width = float(input("Enter the width of the room (in meters): "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return

    # Calculate the area
    area = calculate_area(length, width)
    print(f"The area of the room is: {area:.2f} square meters.")
    
    # Step 2: Choose material
    print("Available materials: Wood, Marble, Tile")
    material = input("Please choose a material: ").strip()
    material_cost = get_material_cost(material)

    if material_cost is None:
        print("Invalid material! Please choose Wood, Carpet, or Tile.")
        return

    # Calculate total cost
    total_cost = area * material_cost
    print(f"The total cost for {material} flooring is: ${total_cost:.2f}")

    #Calculate for multiple rooms
    print("Do you want to calculate for multiple rooms? (yes/no)")
    multi_room = input().strip().lower()
    if multi_room == 'yes':
        area = calculate_total_cost_for_rooms()
    else:
        area = calculate_area(length, width)
    
    # Step 3: Save project details
    save = input("Do you want to save the project details? (yes/no): ").strip().lower()
    if save == 'yes':
        file_name = input("Enter the file name to save the details (e.g., project.txt): ").strip()
        project_details = (
            f"Room Dimensions: {length:.2f}m x {width:.2f}m\n"
            f"Room Area: {area:.2f} square meters\n"
            f"Material: {material}\n"
            f"Material Cost per square meter: ${material_cost:.2f}\n"
            f"Total Cost: ${total_cost:.2f}\n"
        )
        save_project_details(file_name, project_details)
        print(f"Project details saved to {file_name}.")

if __name__ == "__main__":
    main()