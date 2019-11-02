import pandas as pd
import matplotlib.pyplot as plt
import math

db = pd.read_csv("LOG(5).csv")

AcX= db.iloc[:,0]
AcY= db.iloc[:,1]
AcZ= db.iloc[:,2]

time = db.iloc[:,3]     #time in milliseconds, give by arduino

tempo = [i/1000 for i in time]      #time in seconds
    



# Create plots with pre-defined labels.
fig, ax = plt.subplots()

ax.plot(tempo, AcX, '-', color="red", linewidth= 0.8, label='AcX')
ax.plot(tempo, AcY, '-', color="blue", linewidth= 0.8, label='AcY')
ax.plot(tempo, AcZ, '-', color="green", linewidth= 0.8, label='AcZ')

legend = fig.legend(loc='upper right', shadow=True, fontsize='medium')

# Put a nicer background color on the legend.
legend.get_frame().set_facecolor('white')





plt.show()


