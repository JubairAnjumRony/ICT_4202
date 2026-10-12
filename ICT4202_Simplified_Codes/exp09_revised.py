
# Experiment 9: k-NN and Decision Tree Classification

# Load the built-in Iris flower dataset.
from sklearn.datasets import load_iris

# Split the dataset into training and testing portions.
from sklearn.model_selection import train_test_split

# Import the k-Nearest Neighbors classifier.
from sklearn.neighbors import KNeighborsClassifier

# Import the Decision Tree classifier.
from sklearn.tree import DecisionTreeClassifier

# Import evaluation functions.
from sklearn.metrics import accuracy_score, confusion_matrix


# Load the input features X and target labels y.
# X contains four flower measurements.
# y contains the flower class labels.
X, y = load_iris(return_X_y=True)


# Split the data into training and testing sets.
X_train, X_test, y_train, y_test = train_test_split(
    X,                  # All input features
    y,                  # Correct class labels
    test_size=0.30,     # Use 30% for testing and 70% for training
    random_state=42,    # Make the split reproducible
    stratify=y          # Preserve class proportions in both sets
)


# Create a list containing the two classification models.
models = [
    # k-NN classifies a sample using its 5 nearest training samples.
    ("k-NN", KNeighborsClassifier(n_neighbors=5)),

    # Decision Tree uses feature-based rules to classify samples.
    # max_depth=3 limits the tree depth to reduce complexity.
    ("Decision Tree",
     DecisionTreeClassifier(max_depth=3, random_state=42))
]


# Train and evaluate each model separately.
for name, model in models:

    # Learn patterns from the training data.
    model.fit(X_train, y_train)

    # Predict class labels for the unseen test data.
    pred = model.predict(X_test)

    # Calculate the proportion of correct predictions.
    print(name, "accuracy:", accuracy_score(y_test, pred))

    # Display correct and incorrect predictions by class.
    print(confusion_matrix(y_test, pred))
