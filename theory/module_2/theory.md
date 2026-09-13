Absolutely. Now we're moving from **understanding Dev Containers** to actually creating one.

This lab is intentionally simple. The goal is **not to build a complex application**. The goal is to understand exactly what each Dev Container configuration option does.

# Module 2 — Your First Dev Container

## Lab 1 — Create a Python Project

We'll create:

```text
devcontainer-demo/
├── .devcontainer/
│   └── devcontainer.json
├── app/
│   └── main.py
├── requirements.txt
└── README.md
```

The final architecture will be:

```text
                    Your Mac
                       │
             ┌─────────┴─────────┐
             │                   │
          VS Code          Docker Desktop
             │                   │
             │                   ▼
             │          Python Dev Container
             │                   │
             └───────────────────┤
                                 │
                         /workspaces/
                         devcontainer-demo
                                 │
                         ┌───────┴───────┐
                         ▼               ▼
                      main.py       requirements.txt
```

---

# 1. Create the Project

Create a folder:

```bash
mkdir devcontainer-demo
cd devcontainer-demo
```

Then create the directories/files:

```bash
mkdir .devcontainer
mkdir app

touch .devcontainer/devcontainer.json
touch app/main.py
touch requirements.txt
touch README.md
```

You should now have:

```text
devcontainer-demo/
├── .devcontainer/
│   └── devcontainer.json
├── app/
│   └── main.py
├── requirements.txt
└── README.md
```

Open the project in VS Code:

```bash
code .
```

---

# 2. Create `main.py`

Put this inside:

```text
app/main.py
```

```python
print("Hello from the Dev Container!")
```

That's intentionally simple.

We want to prove that this Python code runs **inside the container**.

---

# 3. Create `requirements.txt`

For our first lab, we don't actually need any Python dependencies.

Leave it empty for now.

Later we'll add Flask/FastAPI and other dependencies.

---

# 4. The Most Important File — `devcontainer.json`

Now open:

```text
.devcontainer/devcontainer.json
```

Start with:

```json
{
  "name": "Python Dev Container",
  "image": "mcr.microsoft.com/devcontainers/python:3.12"
}
```

That's it!

This tiny file is already enough to create a Dev Container.

---

# 5. What Does `image` Mean?

This:

```json
"image": "mcr.microsoft.com/devcontainers/python:3.12"
```

means:

> Use this Docker image as the base for my development environment.

We're using Microsoft's official Dev Container Python image.

Conceptually:

```text
devcontainer.json
       │
       │ image
       ▼
Python 3.12 Dev Container Image
       │
       ▼
Development Container
```

The image already contains useful development tooling around Python.

So we don't have to write a Dockerfile yet.

---

# 6. Why Don't We Use a Dockerfile?

You could create:

```text
.devcontainer/
├── devcontainer.json
└── Dockerfile
```

and build everything yourself.

But for learning Dev Containers, it's better to start with:

```json
"image": "mcr.microsoft.com/devcontainers/python:3.12"
```

because you can focus on understanding:

```text
Dev Container
     ↓
VS Code
     ↓
Docker
```

rather than immediately dealing with Dockerfile syntax.

We'll learn custom Dockerfiles in **Module 5**.

---

# 7. Start the Dev Container

Now in VS Code:

1. Open the Command Palette.
2. Search for:

```text
Dev Containers: Reopen in Container
```

3. Select it.

VS Code will now start doing work.

Conceptually:

```text
VS Code
   │
   ▼
Read devcontainer.json
   │
   ▼
Find Python 3.12 image
   │
   ▼
Docker Desktop
   │
   ▼
Create container
   │
   ▼
Mount your project
   │
   ▼
VS Code attaches
```

The first time may take a little while because Docker may need to download the image.

---

# 8. What Has Actually Happened?

Before:

```text
Mac
│
└── VS Code
      │
      └── Python project
```

After:

```text
Mac
│
├── VS Code
│
└── Docker Desktop
       │
       ▼
  Python Dev Container
       │
       └── devcontainer-demo
```

Your source code is available inside the container.

VS Code is now connected to the container.

---

# 9. Verify Python

Open the **VS Code terminal**.

Run:

```bash
python --version
```

You should get something similar to:

```text
Python 3.12.x
```

Then:

```bash
pip --version
```

You should get something similar to:

```text
pip 25.x from ...
```

The important concept isn't the exact version.

It's:

> **Where is Python running?**

Answer:

```text
Inside the Dev Container
```

---

# 10. Prove That You're Inside the Container

This is a good learning exercise.

Run:

```bash
uname -a
```

You should see Linux-related information.

Remember:

```text
Your Mac
   ↓
macOS
```

but:

```text
Dev Container
   ↓
Linux environment
```

Even though you're using macOS, your development process is running inside the Linux container.

This is one of the major benefits of containers.

---

# 11. Run Your Python Application

Now run:

```bash
python app/main.py
```

You should see:

```text
Hello from the Dev Container!
```

So:

```text
VS Code terminal
      │
      ▼
Python
      │
      ▼
Dev Container
      │
      ▼
app/main.py
```

Congratulations — you've created your first Dev Container. 🎉

---

# 12. Now Let's Understand the Configuration

Our configuration currently is:

```json
{
  "name": "Python Dev Container",
  "image": "mcr.microsoft.com/devcontainers/python:3.12"
}
```

There are two properties:

### `name`

```json
"name": "Python Dev Container"
```

This is simply the name of the development environment.

You'll see it in VS Code.

It helps distinguish environments when you're working with multiple projects.

---

### `image`

```json
"image": "mcr.microsoft.com/devcontainers/python:3.12"
```

This tells Dev Containers:

> Use this image to create my development environment.

---

# 13. Now Add `features`

This is our next important concept.

Suppose we want Node.js in addition to Python.

We could manually install Node.js.

But Dev Containers provide **Features**.

A Feature is a reusable package/configuration that adds a capability or tool to your Dev Container.

For example:

```json
{
  "name": "Python Dev Container",

  "image": "mcr.microsoft.com/devcontainers/python:3.12",

  "features": {
    "ghcr.io/devcontainers/features/node:1": {
      "version": "22"
    }
  }
}
```

Now the environment conceptually becomes:

```text
Python Dev Container
       │
       ├── Python 3.12
       │
       └── Node.js 22
```

You didn't need to write a Dockerfile just to install Node.

---

# 14. What Is a Feature?

Think of it like a Lego block.

Base:

```text
Python Dev Container
```

Add:

```text
Node Feature
```

Result:

```text
Python
+
Node.js
```

Add another:

```text
Terraform Feature
```

Result:

```text
Python
+
Node.js
+
Terraform
```

Add:

```text
Azure CLI
```

Now:

```text
Python
Node.js
Terraform
Azure CLI
```

This becomes very useful for your eventual cloud-native development environment.

---

# 15. Add VS Code Extensions with `customizations`

Now suppose you want Python and Pylance extensions automatically installed.

Add:

```json
{
  "name": "Python Dev Container",

  "image": "mcr.microsoft.com/devcontainers/python:3.12",

  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance"
      ]
    }
  }
}
```

Now the architecture becomes:

```text
Dev Container
│
├── Python 3.12
│
└── VS Code Extensions
    ├── Python
    └── Pylance
```

This means another developer opening this repository gets the required VS Code extensions automatically.

That's one of the major ideas behind reproducible development environments.

---

# 16. `customizations` Is Not the Same as `features`

This distinction is important.

### `features`

Add **development tools/software to the container**.

For example:

```text
Node.js
Terraform
Azure CLI
kubectl
```

### `customizations`

Configure the **VS Code development experience**.

For example:

```text
Python extension
Pylance
Ruff
Docker extension
Kubernetes extension
```

Think:

```text
             Dev Container
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
     Features            Customizations
        │                     │
        ▼                     ▼
     Container              VS Code
       Tools              Experience
```

---

# 17. `forwardPorts`

Now suppose we turn our Python program into a web application.

For example, Flask:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Dev Container!"

app.run(host="0.0.0.0", port=8000)
```

The application listens inside the container on:

```text
8000
```

We can tell Dev Containers:

```json
"forwardPorts": [8000]
```

So:

```json
{
  "name": "Python Dev Container",

  "image": "mcr.microsoft.com/devcontainers/python:3.12",

  "forwardPorts": [
    8000
  ]
}
```

Conceptually:

```text
Mac
 │
 │ localhost:8000
 ▼
VS Code / Docker port forwarding
 │
 ▼
Container
 │
 │ :8000
 ▼
Flask
```

This allows you to access the application from your host machine.

---

# 18. Important: `forwardPorts` Is Not the Same as Docker `EXPOSE`

Don't worry about this distinction deeply yet, but remember:

```text
forwardPorts
```

is specifically about making a container port accessible through the Dev Container development experience.

We'll revisit port/network behavior when we learn Docker Compose.

---

# 19. `postCreateCommand`

Now suppose your project has dependencies:

```text
requirements.txt
```

For example:

```text
flask
requests
```

We could tell Dev Containers:

```json
"postCreateCommand": "pip install -r requirements.txt"
```

Full configuration:

```json
{
  "name": "Python Dev Container",

  "image": "mcr.microsoft.com/devcontainers/python:3.12",

  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance"
      ]
    }
  },

  "forwardPorts": [
    8000
  ],

  "postCreateCommand": "pip install -r requirements.txt"
}
```

Now after the container is created, Dev Containers can run:

```bash
pip install -r requirements.txt
```

inside the container.

---

# 20. Why Is `postCreateCommand` Useful?

Without it, you might have to manually run:

```bash
pip install -r requirements.txt
```

every time you create a fresh environment.

With:

```json
"postCreateCommand": "pip install -r requirements.txt"
```

the project can automatically prepare itself.

So the workflow becomes:

```text
Clone repository
      ↓
Open in VS Code
      ↓
Reopen in Container
      ↓
Container created
      ↓
pip install -r requirements.txt
      ↓
Ready to code
```

This is a major part of the **"clone → open → start coding"** experience.

---

# 21. Our Final `devcontainer.json`

For this first lab, I'd use:

```json
{
  "name": "Python Dev Container",

  "image": "mcr.microsoft.com/devcontainers/python:3.12",

  "features": {
    "ghcr.io/devcontainers/features/node:1": {
      "version": "22"
    }
  },

  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance"
      ]
    }
  },

  "forwardPorts": [
    8000
  ],

  "postCreateCommand": "pip install -r requirements.txt"
}
```

Even though our current Python program doesn't need Node or port 8000, **we're deliberately adding them to learn the configuration concepts**.

---

# 22. Verify Everything

After rebuilding/reopening the container, run:

```bash
python --version
```

Expected:

```text
Python 3.12.x
```

Then:

```bash
pip --version
```

Then:

```bash
node --version
```

Expected something around:

```text
v22.x.x
```

Then:

```bash
python app/main.py
```

Expected:

```text
Hello from the Dev Container!
```

---

# 23. One Important Experiment

Now close/delete the container and recreate it.

Don't worry—you can safely do this because your project source code is outside the container.

Reopen:

```text
Dev Containers: Reopen in Container
```

Watch what happens:

```text
.devcontainer/devcontainer.json
          │
          ▼
Docker image/container
          │
          ▼
Features installed
          │
          ▼
VS Code extensions configured
          │
          ▼
postCreateCommand
          │
          ▼
VS Code attaches
```

Then:

```bash
python --version
node --version
```

should still work.

**This experiment demonstrates the key Dev Container principle:**

> The environment is reproducible from the repository configuration.

---

# 24. What You Have Learned

At the end of this lab, you should understand:

| Configuration       | Purpose                             |
| ------------------- | ----------------------------------- |
| `.devcontainer/`    | Stores Dev Container configuration  |
| `devcontainer.json` | Defines the development environment |
| `image`             | Base container image                |
| `features`          | Adds reusable development tools     |
| `customizations`    | Configures VS Code                  |
| `forwardPorts`      | Makes container ports accessible    |
| `postCreateCommand` | Runs setup after container creation |

The overall architecture is now:

```text
                     Git Repository
                           │
                           ▼
                  .devcontainer/
                           │
                           ▼
                  devcontainer.json
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
        image           features      customizations
          │                │                │
          ▼                ▼                ▼
       Python            Node.js       VS Code Extensions
          │
          └────────────────┬────────────────┘
                           ▼
                   Development Container
                           │
                           ├── Source Code
                           ├── Python
                           ├── Node.js
                           └── Dependencies
                           │
                           ▼
                  postCreateCommand
                           │
                           ▼
                    Ready to Code
```

### The key mental model

Think of `devcontainer.json` as saying:

> **"When a developer opens this repository, this is the development environment I want VS Code to create for me."**

That's the foundation. From here, the next useful step is to take this exact lab and **inspect what Docker actually created**—using `docker images`, `docker ps`, `docker inspect`, and `docker exec`. That will connect your Docker Fundamentals directly to what you just built.
