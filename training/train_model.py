import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.calibration import CalibratedClassifierCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# =========================
# 1️⃣ Cargar dataset
# =========================
DATASET_PATH = "training/dataset_sentiment_v3.csv"

df = pd.read_csv(
    DATASET_PATH,
    sep=";",
    encoding="utf-8"
)

print("\n📄 Columnas detectadas:")
print(df.columns.tolist())

expected_columns = {"texto", "sentimiento"}
if not expected_columns.issubset(df.columns):
    raise ValueError(f"❌ El CSV debe contener las columnas {expected_columns}")

# =========================
# 2️⃣ Normalizar etiquetas
# =========================
df["sentimiento"] = df["sentimiento"].str.lower().str.strip()

label_map = {
    "negativo": 0,
    "neutral": 1,
    "positivo": 2
}

df["label"] = df["sentimiento"].map(label_map)

if df["label"].isnull().any():
    raise ValueError("❌ Existen etiquetas no válidas en el CSV")

print("\n📊 Distribución de clases:")
print(df["sentimiento"].value_counts())

# =========================
# 3️⃣ Split estratificado
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    df["texto"],
    df["label"],
    test_size=0.2,
    random_state=42,
    stratify=df["label"]
)

# =========================
# 4️⃣ Vectorización TF-IDF
# =========================
vectorizer = TfidfVectorizer(
    max_features=5000,
    ngram_range=(1, 2),
    min_df=1,
    max_df=0.95
)

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# =========================
# 5️⃣ Modelo base
# =========================
base_model = LogisticRegression(
    max_iter=2000,
    class_weight="balanced",
    random_state=42
)

# =========================
# 6️⃣ Calibración (PASO A)
# =========================
model = CalibratedClassifierCV(
    estimator=base_model,
    method="sigmoid",
    cv=5
)

model.fit(X_train_vec, y_train)

# =========================
# 7️⃣ Evaluación
# =========================
y_pred = model.predict(X_test_vec)

print("\n📈 Reporte de clasificación:\n")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=["negativo", "neutral", "positivo"],
        zero_division=0
    )
)

# =========================
# 8️⃣ Guardar versión FINAL v3 (PASO B)
# =========================
joblib.dump(model, "models/modelo_sentimiento_v3.pkl")
joblib.dump(vectorizer, "models/vectorizador_tfidf_v3.pkl")

print("\n✅ Modelo sentiment-es-v3 entrenado, calibrado y guardado correctamente")
