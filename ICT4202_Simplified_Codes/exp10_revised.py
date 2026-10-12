
# Experiment 10: Unsupervised Learning - K-means Clustering

# Import Matplotlib to visualize the clusters.
import matplotlib.pyplot as plt

# Load the Iris dataset.
from sklearn.datasets import load_iris

# Import the K-means clustering algorithm.
from sklearn.cluster import KMeans

# Import a metric to evaluate cluster separation.
from sklearn.metrics import silhouette_score


# Load the Iris features and select the first two columns.
# Column 0 = sepal length; column 1 = sepal width.
# Only these two features are used for clustering and plotting.
X = load_iris().data[:, :2]


# Create a K-means model with three clusters.
# random_state=42 makes initialization reproducible.
# n_init=10 runs the algorithm with 10 initializations
# and retains the best result according to the objective.
model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

# Fit the model to the data and return a cluster label for each sample.
# Each label identifies which of the three clusters the sample belongs to.
labels = model.fit_predict(X)


# Print the coordinates of the three cluster centers.
print("Centers:\n", model.cluster_centers_)

# Print inertia, the sum of squared distances from points to their
# assigned cluster centers. Lower is better for the same dataset
# and number of clusters, but it usually decreases as k increases.
print("Inertia:", model.inertia_)

# Calculate the silhouette score.
# It measures how well samples fit within their clusters compared
# with other clusters. Higher values generally indicate better separation.
print("Silhouette:", silhouette_score(X, labels))


# Plot the data points, coloring each point by its cluster label.
plt.scatter(X[:, 0], X[:, 1], c=labels)

# Plot the cluster centers using large X-shaped markers.
plt.scatter(
    model.cluster_centers_[:, 0],  # Center sepal lengths
    model.cluster_centers_[:, 1],  # Center sepal widths
    marker="X",                    # Use X-shaped markers
    s=180,                         # Set marker size
    edgecolors="black"             # Draw a black border
)

# Label both axes using the selected flower measurements.
plt.xlabel("Sepal length (cm)")
plt.ylabel("Sepal width (cm)")

# Add a title to the graph.
plt.title("K-means clustering, k=3")

# Display the cluster plot.
plt.show()
