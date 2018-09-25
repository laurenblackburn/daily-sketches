# 9/24/18

# inspired from matplotlib docs example:
#     Blend transparency with color in 2-D images
import matplotlib.pyplot as plt
import numpy as np

def gaussian(x, mean, var):
    return np.exp(-(x-mean)**2 / (2*var))
def poisson(x, mean):
    return

# grid to plot blobs
xmin, xmax, ymin, ymax = (0, 100, 0, 100)
n_bins = 350
xx = np.linspace(xmin, xmax, n_bins)
yy = np.linspace(ymin, ymax, n_bins)

# blob parameters
means_high = [90, 40]
means_hmed = [50, 50]
means_lmed = [50, 10]
means_low = [25, 75]
var = [120, 300, 200, 250]

gauss_x_high = gaussian(xx, means_high[0], var[0])
gauss_y_high = gaussian(yy, means_high[1], var[0])

gauss_x_hmed = gaussian(xx, means_hmed[0], var[1])
gauss_y_hmed = gaussian(yy, means_hmed[1], var[1])

gauss_x_lmed = gaussian(xx, means_lmed[0], var[2])
gauss_y_lmed = gaussian(yy, means_lmed[1], var[2])

gauss_x_low = gaussian(xx, means_low[0], var[3])
gauss_y_low = gaussian(yy, means_low[1], var[3])

# weight values to plot
weights_high = np.array(np.meshgrid(gauss_x_high, gauss_y_high)).prod(0)
#print("weight high: ", np.array(np.meshgrid(gauss_x_high, gauss_y_high)).prod(0))
weights_hmed = np.array(np.meshgrid(gauss_x_hmed, gauss_y_hmed)).prod(0)
weights_lmed = -1 * np.array(np.meshgrid(gauss_x_lmed, gauss_y_lmed)).prod(0)
weights_low = -1 * np.array(np.meshgrid(gauss_x_low, gauss_y_low)).prod(0)
#print("weight low: ", weights_low)
weights = weights_high + weights_hmed + weights_lmed + weights_low
#print("weights: ", weights)

greys = np.empty(weights.shape + (3,), dtype=np.uint8)
print("weight shape ", weights.shape)
print(" set greys ", (weights.shape + (3,)))
print("grey shape ", greys.shape)
greys.fill(70)

fig, ax = plt.subplots()
#ax.imshow(greys)
ax.imshow(weights, extent=(xmin, xmax, ymin, ymax), cmap= plt.cm.seismic)
plt.axis("off")
plt.show()
