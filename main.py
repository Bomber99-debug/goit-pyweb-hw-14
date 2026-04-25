import subprocess
import sys

def main():
    files = ["create_db.py", "insert_db.py", "select.py"]
    
    for file in files:
        print(f"--- Запуск {file} ---")
        subprocess.run([sys.executable, file])
        print(f"--- {file} завершено ---\n")

if __name__ == "__main__":
    main()