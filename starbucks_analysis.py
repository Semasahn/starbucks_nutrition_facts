import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# 1. Veri Yükleme
file_path = "starbucks.csv"
df = pd.read_csv(file_path)

# 2. Veri Keşfi ve Genel Bilgiler
print(df.head())  
print(df.info())  
print(df.describe())  
print(df['type'].value_counts())  
print(df.isnull().sum())  

# 3. Eksik Veri Doldurma
df.fillna(df.select_dtypes(include=['number']).mean(), inplace=True)

# 4. Kategorik Verileri Sayısal Hale Getirme (Label Encoding)
encoder = LabelEncoder()
df['type'] = encoder.fit_transform(df['type'])

# Kategori isimlerinin saklanması
category_names = dict(enumerate(encoder.classes_))

# 5. Veri Görselleştirme

# Renklerin Kategorilere Göre Tanımlanması
category_colors = {
    "bakery": "#1f77b4",
    "petite": "#ff7f0e",
    "bistro box": "#d62728",
    "hot breakfast": "#8c564b",
    "sandwich": "#e377c2",
    "parfait": "#bcbd22",
    "salad": "#17becf"
}

# Pasta Grafiği
labels = category_names.values()
sizes = df['type'].value_counts().values
colors = [category_colors[label] for label in labels]

plt.figure(figsize=(10, 6))
wedges, texts, autotexts = plt.pie(
    sizes, labels=None, autopct="%1.1f%%", colors=colors, startangle=140
)
plt.title("Starbucks Ürün Dağılımı", pad=15)  # Başlık yukarı alındı
plt.legend(wedges, labels, title="Ürün Kategorileri", loc="center left", bbox_to_anchor=(1, 0.5))
plt.show()

# Sütun Grafiği (Aynı renk eşleşmesi kullanılarak)
plt.figure(figsize=(10, 5))
ax = sns.countplot(
    x=df["type"].map(category_names),
    palette=[category_colors[label] for label in category_names.values()]
)

ax.set_xticks(range(len(category_names)))
ax.set_xticklabels(category_names.values(), rotation=0)

plt.xlabel("Ürün Kategorileri", labelpad=10)
plt.ylabel("Ürün Sayısı", labelpad=15)
plt.title("Ürün Türlerine Göre Dağılım", pad=20)  # Başlık yukarı alındı
plt.show()

# Kalori Dağılımı Histogramı
plt.figure(figsize=(10, 5))
sns.histplot(df["calories"], bins=20, kde=True, color="red")
plt.xlabel("Kalori", labelpad=10)  # İngilizce terimler değiştirildi
plt.ylabel("Frekans", labelpad=10)
plt.title("Kalori Dağılımı", pad=20)  # Başlık yukarı alındı
plt.show()

# Kalori ve Karbonhidrat İlişkisi
plt.figure(figsize=(10, 5))
sns.scatterplot(x=df["calories"], y=df["carb"], color="green")
plt.xlabel("Kalori", labelpad=10)  # Çeviri yapıldı
plt.ylabel("Karbonhidrat", labelpad=10)
plt.title("Kalori ve Karbonhidrat İlişkisi", pad=20)  # Başlık yukarı alındı
plt.show()

# 6. Korelasyon Matrisi
numeric_df = df.select_dtypes(include=[np.number])
plt.figure(figsize=(10, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Değişkenler Arasındaki Korelasyon", pad=20)  # Başlık yukarı alındı
plt.show()

# 7. Karar Ağacı Modeli Oluşturma ve Eğitme
# Bağımsız ve bağımlı değişkenlerin belirlenmesi
X = df[['calories', 'fat', 'carb', 'fiber', 'protein']]
y = df['type']

# Eğitim ve test veri setlerinin oluşturulması
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Karar ağacı modelinin oluşturulması ve eğitilmesi
model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X_train, y_train)

# Modelin doğruluk oranının hesaplanması
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Karar Ağacı Modeli Doğruluk Skoru: {accuracy:.2f}")

# 8. Karar Ağacının Görselleştirilmesi
plt.figure(figsize=(15, 10))
plot_tree(model, feature_names=["Kalori", "Yağ", "Karbonhidrat", "Lif", "Protein"], 
          class_names=encoder.classes_, filled=True)
plt.title("Karar Ağacı Modeli", pad=25)  # Başlık yukarı alındı
plt.show()
