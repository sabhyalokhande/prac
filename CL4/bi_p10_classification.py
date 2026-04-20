import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# STEP 1 & 2: Import Libraries and Load Dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target_names[iris.target]
print("Dataset:")
print(df.head())

# STEP 3: Prepare Data
X = df[iris.feature_names]

# STEP 4: Convert Labels
le = LabelEncoder()
y = le.fit_transform(df['species'])

# STEP 5: Split Data and Apply Classification Algorithm
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# STEP 6: Prediction
y_pred = model.predict(X_test)
print("\nPredictions:", le.inverse_transform(y_pred))

# STEP 7: Evaluation
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=le.classes_))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
