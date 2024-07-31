import matplotlib.pyplot as plt

# Data
x = [0, 5, 9, 10, 15, 20, 25]
y = [0, 1, 2, 3, 4, 5, 6]

# Create the plot
plt.plot(x, y, marker='o', linestyle='-', color='b')

# Add titles and labels
plt.title('Line Plot of Given Data')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Show grid
plt.grid(True)

# Display the plot
plt.show()


