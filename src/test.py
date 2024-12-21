from pathlib import Path

# Locate the "My Documents" folder
documents_path = Path.home() / "Documents"

print(f"My Documents folder is located at: {documents_path}")