import random
import math
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


# Set up the grid with reduced dimensions
grid_size = 450
center = grid_size // 2
grid = np.zeros((grid_size, grid_size), dtype=int)
grid[center, center] = 1
center1 = center
radius = 200
count = 0
frame_count = 0

def is_within_bounds(x, y, size):
    """Check if (x, y) is within the grid bounds."""
    return 0 <= x < size and 0 <= y < size

def is_next_to_aggregated_particle(x, y, grid):
    """Check if (x, y) is next to an aggregated particle."""
    neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in neighbors:
        nx, ny = x + dx, y + dy
        if is_within_bounds(nx, ny, len(grid)) and grid[nx, ny] == 1:
            return True
    return False

# Simulate the particle aggregation
frames = []
while True:
    # Initialize the particle
    theta = random.uniform(0, 2 * math.pi)
    x = round(center1 + radius * math.cos(theta))
    y = round(center1 + radius * math.sin(theta))

    # Run the random walk until the particle sticks or leaves the grid
    while True:
        # Move the particle
        dx, dy = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        x_new, y_new = x + dx, y + dy

        # Check if the particle is inside the grid
        if not is_within_bounds(x_new, y_new, grid_size):
            break

        # Check if the particle is next to an aggregated particle
        if is_next_to_aggregated_particle(x_new, y_new, grid):
            if (x_new - center1)**2 + (y_new - center1)**2 >= radius**2:
                count += 1
            grid[x_new, y_new] = 1
            break

        # Update the particle position
        x, y = x_new, y_new

    # Check if the particle reached the circle
    if count >= 1:
        break

    # Create a PIL image from the grid and add it to the list of frames
    frame_count += 1
    if frame_count % 200 == 0:
        im = Image.fromarray((grid * 255).astype(np.uint8))
        frames.append(im)

# Save the animation as a GIF
duration = 10  # milliseconds per frame
if frames:
    frames[0].save('fractal1.gif', format='GIF', append_images=frames[1:], save_all=True, duration=duration, loop=0)

# Save and visualize the results
np.savetxt("fractal_output.txt", grid, fmt='%d')
print(grid)

plt.imshow(grid, cmap='gray')
plt.show()
