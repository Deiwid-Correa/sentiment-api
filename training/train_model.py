import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# 1️⃣ Cargar dataset
df = pd.read_csv("training/dataset_es.csv")

# 2️⃣ Mapear etiquetas
label_map = {
    "negativo": 0,
    "neutro": 1,
    "positivo": 2
}
df["label"] = df["sentimiento"].map(label_map)

# 3️⃣ Separar datos
X_train, X_test, y_train, y_test = train_test_split(
    df["texto"],
    df["label"],
    test_size=0.2,
    random_state=42,
    stratify=df["label"]
)

# 4️⃣ Vectorizador TF-IDF
vectorizer = TfidfVectorizer(
    max_features=5000,
    ngram_range=(1, 2),
    stop_words=None
)

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# 5️⃣ Modelo
model = LogisticRegression(
    max_iter=1000,
    random_state=42
)
model.fit(X_train_vec, y_train)

# 6️⃣ Evaluación
y_pred = model.predict(X_test_vec)
print(classification_report(y_test, y_pred))

# 7️⃣ Guardar modelo
joblib.dump(model, "models/modelo_sentimiento.pkl")
joblib.dump(vectorizer, "models/vectorizador_tfidf.pkl")

print("✅ Modelo y vectorizador reentrenados y guardados")
