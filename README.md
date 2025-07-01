# Template: Python with Ruff and MyPy 

<img src="src/static/img/article-cover.png" alt="Project Cover" style="width:100%; max-width:800px;" />

A modern Python project template pre-configured with Ruff (for linting and formatting) and MyPy (for static type checking).
This setup uses pre-commit to ensure code quality before every commit.

You can find concepts and step-by-step instructions in the article in Medium:
* 🔗 [How to: Automate a clean code base with Ruff and Mypy.](https://medium.com/@fernando.peres/how-to-automate-a-clean-code-base-with-ruff-and-mypy-ff7d9fa51e86) 


🚀 Features:
- **Ruff**: Blazing-fast linter and formatter
- **MyPy**: Static type checking for Python
- **pre-commit**: Automated checks before every commit
- **Easy setup**: Fast environment provisioning with `uv`

---

## 1. Installation

Step 1: Install dependencies

```bash
uv sync --all-groups
```

Step 2: Activate the virtual environment

```bash
source .venv/bin/activate
```

Step 3: Set up pre-commit hooks

```bash
pre-commit install  
```

## 2. Usage

Check pre-commit hook status

```bash
pre-commit run --all-files
``` 

Whenever you run:

```bash
git commit -m "<message>"
```
the pre-commit hooks will run automatically.
If any checks fail, the commit will be aborted.


## 3. Customization

* Configure Ruff and MyPy via `pyproject.toml`.
* Add or remove `pre-commit` hooks in `.pre-commit-config.yaml`.

Happy coding! 🚀
