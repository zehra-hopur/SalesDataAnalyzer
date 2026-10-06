import pandas as pd
import matplotlib.pyplot as plt

# CSV dosyasını oku
df = pd.read_csv("data/sales.csv")

# Toplam satış tutarını hesapla
df["Sales"] = df["Quantity"] * df["Unit_Price"]

# Kârı hesapla
df["Profit"] = df["Quantity"] * (df["Unit_Price"] - df["Unit_Cost"])

# Verileri ekrana yazdır
print(df)

# Toplam satış ve toplam kâr
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

print("Toplam Satış:", total_sales)
print("Toplam Kâr:", total_profit)

# En çok satan ürünü bul
product_sales = df.groupby("Product")["Quantity"].sum()
best_selling_product = product_sales.idxmax()
best_selling_quantity = product_sales.max()

print("En Çok Satan Ürün:", best_selling_product)
print("Satılan Adet:", best_selling_quantity)

# Kategorilere göre toplam geliri hesapla
category_sales = df.groupby("Category")["Sales"].sum()

# En yüksek gelir getiren kategoriyi bul
best_category = category_sales.idxmax()
best_category_sales = category_sales.max()

print("En Yüksek Gelir Getiren Kategori:", best_category)
print("Kategori Geliri:", best_category_sales)


# Tarih sütununu datetime formatına çevir
df["Date"] = pd.to_datetime(df["Date"])

# Aylık satışları hesapla
monthly_sales = df.groupby(df["Date"].dt.to_period("M"))["Sales"].sum()

print("\nAylık Satışlar:")
print(monthly_sales)

# Aylık satış grafiği
plt.figure(figsize=(10, 5))

monthly_sales.plot(kind="bar")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.xticks(rotation=45)

plt.tight_layout()

# Grafiği kaydet
plt.savefig("charts/monthly_sales.png")

plt.show()

# Ürün bazında toplam satış
product_revenue = df.groupby("Product")["Sales"].sum()

# Ürün satış grafiği
plt.figure(figsize=(10, 5))

product_revenue.plot(kind="bar")

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales ($)")
plt.xticks(rotation=45)

plt.tight_layout()

# Grafiği kaydet
plt.savefig("charts/product_sales.png")

plt.show()


# Ürün bazında toplam kâr
product_profit = df.groupby("Product")["Profit"].sum()

# Ürün kâr grafiği
plt.figure(figsize=(10, 5))

product_profit.plot(kind="bar")

plt.title("Profit by Product")
plt.xlabel("Product")
plt.ylabel("Profit ($)")
plt.xticks(rotation=45)

plt.tight_layout()

# Grafiği kaydet
plt.savefig("charts/product_profit.png")

plt.show()

# Kâr marjını hesapla
profit_margin = (total_profit / total_sales) * 100

print("\nKâr Marjı: %", round(profit_margin, 2))