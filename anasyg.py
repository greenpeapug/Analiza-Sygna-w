#y(t)=A∗sin(2∗π∗f∗t+φ)
# import numpy as np
# import matplotlib.pyplot as plt
#
# f = 5
# A = 1
# t = np.linspace(0, 1, 256)
# sygnal = A*np.sin(2*np.pi*f*t+13)
#
# plt.xlabel("s (czas)")
# plt.ylabel("Wartość funkcji")
#
#
# plt.title("f = 5")
# plt.plot(t, sygnal)
# plt.show()

### próbkowanie ###
# import numpy as np
# import matplotlib.pyplot as plt
#
# f1 = 5
# f2 = 7
# f3 = 3
# t = np.linspace(0, 1, 256)
# sygnal = np.sin(2*np.pi*f1*t)+np.sin(2*np.pi*f2*t)+np.sin(2*np.pi*f3*t)
# plt.plot(t, sygnal)
#
# t = np.linspace(0, 1, 10)
# sygnal = np.sin(2*np.pi*f1*t)+np.sin(2*np.pi*f2*t)+np.sin(2*np.pi*f3*t)
# plt.plot(t, sygnal)
#
# plt.show()

### Próbkowanie moje ###
import numpy as np
import matplotlib.pyplot as plt

f = 5
t = np.linspace(0, 1, 50)
sygnal = np.sin(2*np.pi*f*t)
plt.plot(t, sygnal,"o")

t = np.linspace(0, 1, 10)
sygnal = np.sin(2*np.pi*f*t)
plt.xlabel("s (czas)")
plt.ylabel("Wartość funkcji")

plt.title("Próbkowanie 50/s")

plt.plot(t, sygnal)

plt.show()
