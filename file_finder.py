import os

search = input("Wonach willst du suchen? ")
count = 0


for root, dirs, files in os.walk("Test Ordner"):
    for file in files:
        if search.lower() in file.lower():
            count += 1
            print("Gefunden:", os.path.join(root, file))

print("\nGefundene Dateien:", count)