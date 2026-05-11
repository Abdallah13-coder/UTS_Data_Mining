inventory = {
    "laptop": {"stok": 10, "harga": 15000000},
    "mouse": {"stok": 50, "harga": 250000},
    "monitor": {"stok": 20, "harga": 3000000}
}

# Menambahkan produk baru
inventory["keyboard"] = {"stok": 30, "harga": 500000}

# Update harga laptop
inventory["laptop"]["harga"] = 14500000

# Menghitung total aset
total_aset = sum(item["stok"] * item["harga"] for item in inventory.values())

print("Data Inventory:")
print(inventory)

print("Total aset gudang:", total_aset)