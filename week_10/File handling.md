# 📁 File Handling in Python

File handling in Python allows us to **create**, **read**, **write**, and **delete** files. It’s used to manage data stored in files (like `.txt`, `.csv`, etc.).

---

## 📝 Types of Files

There are mainly **two types** of files:

1. **Text Files** – contain readable characters (e.g., `.txt`, `.csv`, `.py`)
2. **Binary Files** – contain non-readable (binary) data (e.g., images, videos, `.exe`, `.dat`)

---

## ⚙️ File Handling Modes

| Mode | Description |
|------|-------------|
| `'r'` | Read (default) – error if file doesn’t exist |
| `'w'` | Write – creates new file or overwrites existing |
| `'a'` | Append – adds content to end of file |
| `'x'` | Create – error if file already exists |
| `'b'` | Binary mode (e.g., `rb`, `wb`) |
| `'t'` | Text mode (default, e.g., `rt`, `wt`) |

---

## ✅ Basic Operations

### 1. **Open a File**

```python
file = open("example.txt", "r")  # Open for reading

#Or using with (recommended – auto closes file):
with open("example.txt", "r") as file:
    data = file.read()

```

### 🔧 Common File Operations

Below are the most commonly used file operations in Python, including reading, writing, closing, and deleting a file:

```python
# 📖 Read from a file
with open("example.txt", "r") as file:
    content = file.read()       # Reads the full content
    # line = file.readline()    # Reads the first line
    # lines = file.readlines()  # Reads all lines into a list

# ✍️ Write to a file
with open("example.txt", "w") as file:
    file.write("Hello, world!")  # Overwrites the file if it exists

# ❌ Close the file (only needed if not using 'with' statement)
file = open("example.txt", "r")
# ... some operations ...
file.close()

# 🗑️ Delete a file
import os

if os.path.exists("example.txt"):
    os.remove("example.txt")
else:
    print("File does not exist.")



