# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# LESSON 1: BASIC COMANDS
# Modifying the head text

# %% [markdown]
# Normal text
#
# Title 
# %% [markdown]
# Text with format
#
# *Title* **Title**

# %% [markdown]
# Heading text 1
#
# # Title

# %% [markdown]
# Heading text 2
#
# ## Title
# %% [markdown]
# Formula text
#
# $e^{i\pi} + 1 = 0$
# %%
# Adding a plot
import matplotlib
import matplotlib.pyplot as plt 
import numpy as np 

# Data plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2*np.pi*t)

fig, ax=plt.subplots()
ax.plot(t,s)
ax.set(xlabel='time (s)', ylabel='voltage (mV)', 
    title='Voltage-Time plot')
ax.grid()
fig.savefig("test.png")

# %%