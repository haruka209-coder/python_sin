import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

n = 1000
x = np.linspace(0, 10, n)
y = np.sin(x)
df = pd.DataFrame({'x': x, 'y': y})

plt.figure(figsize=(10, 5))
plt.plot(df['x'], df['y'])

plt.title('Sine Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')    

plt.grid()
plt.show()