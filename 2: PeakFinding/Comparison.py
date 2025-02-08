import numpy as np
import matplotlib.pyplot as plt

# Generate n values from 1 to 1000
n = np.arange(1, 1001)

# Calculate the two functions
f1 = 4 * (n - 1)          # 4(n-1)
f2 = 5 * np.log(n)        # 5log(n), natural logarithm

# Plot the functions
plt.figure(figsize=(10, 6))
plt.plot(n, f1, label='Slow Peak Finding: 4(n-1)')
plt.plot(n, f2, label='Fast Peak Finding: 5log(n)')

# Add labels, title, and legend
plt.xlabel('n (size of the array)')
plt.ylabel('number of accesses to the array')
plt.title('Peak Finding: Runtime Comparison')
plt.legend()

# Show grid and plot
plt.grid(True)
plt.show()
