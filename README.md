![ignoreme logo](static/ignoreme.png)

> 🛡️ A simple CLI to generate `.gitignore` files using [donotcommit.com](https://donotcommit.com)  
> 🔥 Stop committing files you shouldn't. Ever again.

---

### ✨ Features

- List all available `.gitignore` templates
- Generate `.gitignore` for one or more technologies
- Output to terminal or directly to a file
- Powered by [donotcommit.com](https://donotcommit.com)

---

### Installation
Using uv:

```bash
uv tool install ignoreme
```

### 🚀 Usage
List available templates
```bash
ignoreme list
```

Generate a .gitignore for Python and Zig
```bash
ignoreme generate python zig
```

Save output to a file
```bash
ignoreme generate python zig --output .gitignore
```

### 🧠 How it works
This CLI is a simple wrapper for the [donotcommit.com](https://donotcommit.com) API. It fetches .gitignore templates by name and combines them for use in your project.

### 📄 License
MIT © Dêvid de Souza Teófilo

### 🛠️ Contributing
Clone the repository.

Install dependencies:

```bash
uv sync
```

Run tests:
```bash
task test
```

Pull requests are welcome.