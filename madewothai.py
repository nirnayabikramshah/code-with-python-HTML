import numpy as np
import matplotlib.pyplot as plt

# 1. Generate data (NumPy)
x = np.linspace(0, 10, 100)  # 100 points from 0 to 10
y = np.sin(x)                # Vectorized sine calculation

# 2. Plot data (Matplotlib)
plt.figure(figsize=(8, 4))
plt.plot(x, y, label='Sine Wave', color='blue', linewidth=2)
plt.title('NumPy Data Visualization')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()   