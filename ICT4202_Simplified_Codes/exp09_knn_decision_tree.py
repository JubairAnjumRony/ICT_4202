# Experiment 9: k-NN and Decision Tree Classification
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify=y
)

models = [
    ("k-NN", KNeighborsClassifier(n_neighbors=5)),
    ("Decision Tree", DecisionTreeClassifier(max_depth=3, random_state=42))
]

for name, model in models:
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print(name, "accuracy:", accuracy_score(y_test, pred))
    print(confusion_matrix(y_test, pred))
