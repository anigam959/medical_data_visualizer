import matplotlib.pyplot as plt
from medical_data_visualizer import draw_cat_plot, draw_heat_map

# Run and save the categorical plot
print("Generating Categorical Plot...")
fig1 = draw_cat_plot()
fig1.savefig("catplot.png")
plt.show()

# Run and save the heat map
print("Generating Heat Map...")
fig2 = draw_heat_map()
fig2.savefig("heatmap.png")
plt.show()

print("✅ All plots generated and saved as 'catplot.png' and 'heatmap.png'")
