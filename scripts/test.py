<<<<<<< HEAD
import numpy as np
import matplotlib.pyplot as plt

p_start = 3
p_end = 5


t = np.linspace(0, 1, 100)
a = -2
b = 3
x = a * t**3 + b * t**2
dx = 3 * a * t**2 + 2 * b * t
P = p_start + (p_end - p_start) * x
dP = (p_end - p_start) * (dx / 2)

plt.figure(1)
plt.grid()
plt.subplot(2, 2, 1)
plt.grid()
plt.plot(t, x, "k")
plt.ylabel("x")

plt.subplot(2, 2, 2)
plt.grid()
plt.plot(t, dx, "k")
plt.ylabel("dx")

plt.subplot(2, 2, 3)
plt.grid()
plt.plot(t, P, "k")
plt.ylabel("p")

plt.subplot(2, 2, 4)
plt.grid()
plt.plot(t, dP, "k")
plt.ylabel("dP")


plt.show()
=======
import g4f

g4f.debug.logging = True  # Enable logging
g4f.check_version = False  # Disable automatic version checking
print(g4f.version)  # Check version
print(g4f.Provider.Ails.params)  # Supported args

# Automatic selection of provider

# Streamed completion
# response = g4f.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[{"role": "user", "content": "Hello"}],
#     stream=True,
# )

# for message in response:
#     print(message, flush=True, end="")

# Normal response
response = g4f.ChatCompletion.create(
    model=g4f.models.gpt_4,
    messages=[{"role": "user", "content": "你好"}],
)  # Alternative model setting

print(response)
>>>>>>> 872288d (Added opencv library)
