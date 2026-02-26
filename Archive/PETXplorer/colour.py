import matplotlib.pyplot as plt

# Define the key points in the gradient as RGB tuples
key_points = [
    (0, 0, 150),
    (0, 225, 255),
    (0, 255, 0),
    (255, 255, 0),
    (255, 0, 0)
]

# Function to interpolate between two colours
def interpolate(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))

# Generate 256 colours
colors = []
num_sections = len(key_points) - 1
steps_per_section = 256 // num_sections

for i in range(num_sections):
    for step in range(steps_per_section):
        t = step / steps_per_section
        colors.append(interpolate(key_points[i], key_points[i + 1], t))

# Ensure exactly 256 colours
while len(colors) < 256:
    colors.append(key_points[-1])

# Convert RGB values to hexadecimal
hex_colors = [f"#{r:02x}{g:02x}{b:02x}" for r, g, b in colors]

# Print the hexadecimal list
print(hex_colors)

# Optional: Display the gradient
plt.figure(figsize=(12, 2))
plt.imshow([colors], extent=[0, 256, 0, 1])
plt.axis("off")
plt.show()