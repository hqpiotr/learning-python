import numpy as np
import matplotlib.pyplot as plt
import webbrowser

x = np.arange(0, 5, 0.1);
y = np.sin(x)
plt.plot(x, y)
webbrowser.open("www.google.com")
