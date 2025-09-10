# Import required libraries
def calculate_area_moment_inertia(b1, h1, b2, h2, h):
    
    effective_h2 = max(0, min(h2, h1 - h))  
    Ix1 = (1 / 12) * b1 * (h1 ** 3)

    # Step 2: Calculate the centroidal distance for the cutout rectangle
    if effective_h2 > 0:  # Only consider the cutout if it affects the larger rectangle
        d = (h + effective_h2 / 2) - (h1 / 2)

        # Step 3: Calculate the moment of inertia for the cutout rectangle about its centroidal axis
        Ix2_centroidal = (1 / 12) * b2 * (effective_h2 ** 3)

        # Step 4: Use the parallel axis theorem to shift the cutout moment of inertia
        A2 = b2 * effective_h2
        Ix2 = Ix2_centroidal + A2 * (d ** 2)
    else:
        Ix2 = 0

    # Step 5: Calculate the net moment of inertia by subtracting the cutout
    Ix_net = Ix1 - Ix2

    return Ix_net

# Example usage with user inputs
if __name__ == "__main__":
    # Input parameters
    b1 = float(input("Enter the breadth of the larger rectangle (b1, in mm): "))
    h1 = float(input("Enter the height of the larger rectangle (h1, in mm): "))
    b2 = float(input("Enter the breadth of the cutout rectangle (b2, in mm): "))
    h2 = float(input("Enter the height of the cutout rectangle (h2, in mm): "))
    h = float(input("Enter the vertical position of the bottom of the cutout rectangle (h, in mm): "))

    # Calculate net area moment of inertia
    Ix_net = calculate_area_moment_inertia(b1, h1, b2, h2, h)

    # Display results
    print(f"\nNet area moment of inertia about the x-axis: {Ix_net:.3f} mm^4")
