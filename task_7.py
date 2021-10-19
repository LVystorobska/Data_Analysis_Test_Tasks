import numpy as np
import matplotlib.pyplot as plt

months = np.arange(1, 11)
turnover = np.array([1, 4, 6, 7, 15, 18, 20, 25, 35, 40])*1000
refunds = np.array([15, 18, 35, 40, 75, 80, 85, 90, 95, 110])*10

plt.figure(figsize=(7,5), dpi=100)

plt.plot(turnover, refunds, 'g.-', label='refunds by turnover')
plt.xlabel('Turnover per month')
plt.ylabel('Refund per month')

m, b = np.polyfit(turnover, refunds, 1)
plt.plot(turnover, m*turnover + b)
plt.show()



