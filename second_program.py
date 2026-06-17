HEIGHT_IN_CM = 165

def cm_to_inches(cm):
    """Convert centimeters to inches."""
    inches = cm / 2.54
    inches = round(inches, 2) # Round to 2 decimal places
    return inches

my_height_in_inches = cm_to_inches(165)

print(f"I'm {HEIGHT_IN_CM} centimeters tall.")
print(f"That's {my_height_in_inches} inches tall.")

