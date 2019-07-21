from matplotlib import pyplot as plt
import pandas as pd

plt.style.use('seaborn')

data = pd.read_csv('scatter_plot_data.csv')

view_count = data['view_count']
likes = data['likes']
ratios = data['ratio']

colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]
sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174,
         538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539]

# x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
# y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]

plt.scatter(view_count, likes, c=ratios, cmap='Greens', edgecolors='k', linewidths=0.75, alpha=0.75)

cbar = plt.colorbar()
cbar.set_label('Likes & DisLikes ratio')

plt.xscale('log')
plt.yscale('log')

plt.title('Trending YouTube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')
plt.tight_layout(True)
plt.grid(True)
plt.savefig('scatter_plot.png')

plt.show()
