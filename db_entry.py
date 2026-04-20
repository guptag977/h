import os
import mysql.connector

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "Guptag@123*$",
    "database": "design_store"
}

PREVIEW_DIR = r"C:\Users\1234\Desktop\Glass_Project\static\previews"

def sync():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("TRUNCATE TABLE cdr_designs")
    
    files = [f for f in os.listdir(PREVIEW_DIR) if f.lower().endswith(('.png', '.jpg'))]
    for file in files:
        title = file.rsplit('.', 1)[0].upper()
        # Default category agar folder structure nahi hai
        category = "Glass Design" 
        cursor.execute("INSERT INTO cdr_designs (title, category, preview_path) VALUES (%s, %s, %s)", (title, category, file))
    
    conn.commit()
    conn.close()
    print(f"Done! {len(files)} designs synced.")

if __name__ == "__main__":
    sync()