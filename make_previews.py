import os
import subprocess

# 1. Aapke screenshot ke hisab se sahi path
GS_PATH = r"C:\Program Files\gs\gs10.07.0\bin\gswin64c.exe"

# 2. Folder Paths
SOURCE_DIR = r"C:\Users\1234\Desktop\Glass_Project\CDR Data"
PREVIEW_DIR = r"C:\Users\1234\Desktop\Glass_Project\static\previews"

# Previews folder banayein agar nahi hai
if not os.path.exists(PREVIEW_DIR):
    os.makedirs(PREVIEW_DIR)

print("🚀 Processing shuru ho rahi hai... Sabar rakhein.")

count = 0
for root, dirs, files in os.walk(SOURCE_DIR):
    for file in files:
        if file.lower().endswith(".cdr"):
            in_file = os.path.join(root, file)
            out_file = os.path.join(PREVIEW_DIR, file.lower().replace(".cdr", ".jpg"))
            
            # Agar image pehle se bani hai toh skip karein
            if not os.path.exists(out_file):
                # Ghostscript command
                cmd = [
                    GS_PATH,
                    "-dNOPAUSE", "-dBATCH",
                    "-sDEVICE=jpeg",
                    "-dJPEGQ=90",    # Photo quality
                    "-r150",         # Resolution
                    f"-sOutputFile={out_file}",
                    in_file
                ]
                
                try:
                    # Result check karne ke liye capture_output use karein
                    result = subprocess.run(cmd, capture_output=True, text=True)
                    if result.returncode == 0:
                        print(f"✅ Success: {file}")
                        count += 1
                    else:
                        print(f"❌ Error in {file}: {result.stderr.strip()[:100]}")
                except Exception as e:
                    print(f"⚠️ Script error: {e}")

print(f"\n🎉 Kaam khatam! Total {count} nayi photos bani hain.")