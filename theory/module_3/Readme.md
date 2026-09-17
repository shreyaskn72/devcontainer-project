**Module 3 — Understanding `devcontainer.json`** is the most important part because this file is essentially the **instruction manual for your development environment**.

You already created a basic Dev Container in Module 2. Now we'll understand **what each configuration does and why you would use it**.

---

# Module 3 — Understanding `devcontainer.json`

Our current project:

```text
devcontainer-demo/
├── .devcontainer/
│   └── devcontainer.json
├── app/
│   └── main.py
├── requirements.txt
└── README.md
```

Think of `devcontainer.json` like this:

```text
                 devcontainer.json
                        │
        ┌───────────────┼────────────────┐
        ↓               ↓                ↓
 Container setup    VS Code setup    Lifecycle setup
        │               │                │
   image/features   extensions       commands
   environment      settings         installation
   ports             formatter        startup
```

So instead of manually telling every developer:

> "Install Python 3.12, install these extensions, configure this setting, run this command..."

you put those instructions into `devcontainer.json`.

---

# 3.1 Basic Configuration

Let's start with the simplest configuration:

```json
{
  "name": "Python Dev Container",
  "image": "mcr.microsoft.com/devcontainers/python:3.12"
}
```

There are two important properties here:

```text
name
image
```

---

## `name`

```json
"name": "Python Dev Container"
```

This is simply the **human-readable name** of your development container.

For example:

```json
"name": "Python Microservice Development"
```

When VS Code shows the Dev Container information, this name helps you identify it.

It doesn't determine how Docker works.

---

# `image`

```json
"image": "mcr.microsoft.com/devcontainers/python:3.12"
```

This tells Dev Containers:

> "Use this Docker image as the starting point for my development environment."

Conceptually:

```text
devcontainer.json
       │
       │ image
       ↓
Python 3.12 Dev Container Image
       │
       ↓
Development Container
```

You can think of the image as a **pre-built development machine template**.

It contains things needed for Python development.

---

## Why use an image?

Without Dev Containers, your Mac might have:

```text
Mac
 ├── Python
 ├── pip
 ├── Git
 ├── VS Code
 └── Python libraries
```

Another developer may have:

```text
Windows
 ├── Python 3.11
 ├── pip
 ├── Git
 └── different libraries
```

This can lead to:

> "It works on my machine."

With Dev Containers:

```text
Git Repository
      │
      ↓
devcontainer.json
      │
      ↓
Same development environment
      │
 ┌────┴─────┐
 ↓          ↓
Developer A Developer B
```

---

# 3.2 Container Configuration

This section is about **how the actual container is created**.

The major concepts are:

```text
image
dockerFile
context
build
containerEnv
remoteEnv
```

The first four are closely related, so let's understand them together.

---

# `image` vs `dockerFile`

This is one of the most important concepts.

There are two common approaches.

### Approach 1 — Use an existing image

```json
{
  "image": "mcr.microsoft.com/devcontainers/python:3.12"
}
```

You are basically saying:

> "Give me this ready-made development environment."

---

### Approach 2 — Build your own image

You can have:

```text
.devcontainer/
├── devcontainer.json
└── Dockerfile
```

Dockerfile:

```dockerfile
FROM mcr.microsoft.com/devcontainers/python:3.12

RUN pip install flask

RUN apt-get update && apt-get install -y \
    curl \
    vim
```

Then:

```json
{
  "name": "My Python Environment",
  "build": {
    "dockerfile": "Dockerfile"
  }
}
```

Now the flow becomes:

```text
Dockerfile
     │
     │ docker build
     ↓
Docker Image
     │
     │ docker run
     ↓
Dev Container
```

---

# Why would we need a Dockerfile?

Suppose your company wants this exact environment:

```text
Python 3.12
Flask
Terraform
kubectl
Helm
Azure CLI
some Linux packages
some custom configuration
```

A standard image may not contain everything.

So you create:

```text
Dockerfile
```

and define exactly what your development environment needs.

---

# `context`

You may see:

```json
{
  "build": {
    "dockerfile": "Dockerfile",
    "context": ".."
  }
}
```

`context` tells Docker:

> "What files/directories are available to the Docker build?"

Suppose:

```text
project/
├── Dockerfile
├── app/
│   └── main.py
├── requirements.txt
└── .devcontainer/
    └── devcontainer.json
```

If:

```json
"context": ".."
```

the context is the project directory.

This matters because Dockerfile instructions such as:

```dockerfile
COPY requirements.txt .
```

can only access files inside the build context.

A simple mental model:

```text
context
   │
   └── Files Docker is allowed to use
             during image build
```

---

# `build`

Instead of:

```json
"image": "some-image"
```

you can tell Dev Containers:

```json
"build": {
  "dockerfile": "Dockerfile"
}
```

This means:

> "Build the development image using this Dockerfile."

You can also specify:

```json
{
  "build": {
    "dockerfile": "Dockerfile",
    "context": ".."
  }
}
```

So:

```text
devcontainer.json
       │
       ↓
Dockerfile + context
       │
       ↓
Docker build
       │
       ↓
Development Image
       │
       ↓
Container
```

---

# `containerEnv`

Now suppose your application needs an environment variable:

```text
APP_ENV=development
```

You can configure:

```json
{
  "containerEnv": {
    "APP_ENV": "development"
  }
}
```

Inside the container:

```bash
echo $APP_ENV
```

would produce:

```text
development
```

Mental model:

```text
containerEnv
      ↓
Environment variable
      ↓
Available inside container
```

You might have:

```json
"containerEnv": {
  "APP_ENV": "development",
  "LOG_LEVEL": "debug"
}
```

---

# `remoteEnv`

This one is slightly different.

```json
"remoteEnv": {
  "MY_VARIABLE": "some-value"
}
```

`remoteEnv` controls environment variables for the **VS Code remote development environment/processes**.

For beginners, don't worry too much about the distinction yet.

Remember:

| Property       | Think of it as                                              |
| -------------- | ----------------------------------------------------------- |
| `containerEnv` | Environment variables for the container                     |
| `remoteEnv`    | Environment variables available to VS Code/remote processes |

For most simple projects, you'll encounter `containerEnv` more often.

---

# 3.3 VS Code Configuration

Now we move from:

> "What should be inside my container?"

to:

> "How should VS Code behave when connected to this container?"

This is where:

```json
customizations
```

comes in.

Example:

```json
{
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python"
      ]
    }
  }
}
```

---

# Extensions

You can automatically install extensions:

```json
"extensions": [
  "ms-python.python",
  "ms-python.vscode-pylance"
]
```

So a new developer does:

```text
git clone repository
        ↓
Open in VS Code
        ↓
Reopen in Container
        ↓
Python extensions automatically available
```

No manual:

> "Go install this extension."

---

## For your project

You might eventually have:

```json
"extensions": [
  "ms-python.python",
  "ms-python.vscode-pylance",
  "redhat.vscode-yaml",
  "ms-kubernetes-tools.vscode-kubernetes-tools",
  "hashicorp.terraform"
]
```

This becomes very useful for your Kubernetes/Terraform projects.

---

# VS Code Settings

You can also configure settings:

```json
"customizations": {
  "vscode": {
    "settings": {
      "python.defaultInterpreterPath": "/usr/local/bin/python",
      "editor.formatOnSave": true
    }
  }
}
```

Now everyone using the Dev Container gets those settings.

---

# Formatters

Suppose your Python project uses:

```text
Black
```

You can configure the development environment so formatting happens consistently.

For example:

```text
Developer A
    ↓
Save Python file
    ↓
Formatter
    ↓
Standard formatting

Developer B
    ↓
Save Python file
    ↓
Same formatter
    ↓
Same formatting
```

This is one of the advantages of putting development configuration in the repository.

---

# Linters

A linter checks code for potential problems.

For Python you might use:

```text
Ruff
```

or other Python tooling.

Conceptually:

```text
Developer writes code
        ↓
       Linter
        ↓
Potential problems highlighted
```

So your Dev Container can standardize:

```text
Python
 ├── Formatter
 ├── Linter
 ├── Language server
 └── Debugger
```

---

# Themes

You can also configure VS Code appearance, although this is generally less important for team reproducibility.

The more important things are:

```text
Extensions
Settings
Formatter
Linter
Debugger
```

---

# 3.4 Lifecycle Commands

This is probably the most confusing part of `devcontainer.json`.

You have commands such as:

```text
initializeCommand
onCreateCommand
updateContentCommand
postCreateCommand
postStartCommand
```

The key question is:

> **When does each command execute?**

Think about the container lifecycle.

```text
Repository opened
       │
       ↓
Initialize
       │
       ↓
Image built
       │
       ↓
Container created
       │
       ↓
Source/content updated
       │
       ↓
Container created/configured
       │
       ↓
Container started
       │
       ↓
Development
```

Let's go through them.

---

# `initializeCommand`

Runs **before the container is created**, on the host side.

Think:

```text
Host machine
     │
     ↓
initializeCommand
     │
     ↓
Create container
```

This is useful for host-side preparation.

Example conceptually:

```json
"initializeCommand": "echo Preparing environment"
```

Important:

**This command is not primarily for installing packages inside your container.**

---

# `onCreateCommand`

Runs when the container is **created**.

Think:

```text
Container creation
       ↓
onCreateCommand
```

It is useful for setup that should happen when the container is created.

---

# `updateContentCommand`

This is related to updating the container's content/workspace.

Think:

```text
Container/workspace content updated
             ↓
updateContentCommand
```

It can be useful when your development environment needs some action after workspace content is updated.

For your beginner project, you don't need this yet.

---

# `postCreateCommand`

This is one you'll use frequently.

It runs after the container has been created and configured.

For example:

```json
"postCreateCommand": "pip install -r requirements.txt"
```

Flow:

```text
Container created
       ↓
Environment configured
       ↓
postCreateCommand
       ↓
pip install -r requirements.txt
       ↓
Ready for development
```

This is perfect for project-specific setup.

For example:

```json
"postCreateCommand": "pip install -r requirements.txt"
```

or:

```json
"postCreateCommand": "npm install"
```

---

# `postStartCommand`

This runs when the container **starts**.

Think:

```text
Container starts
      ↓
postStartCommand
```

Unlike `postCreateCommand`, container startup can happen many times.

For example:

```text
Create container
   ↓
postCreateCommand
   ↓
Start container
   ↓
postStartCommand
```

Later:

```text
Stop container
   ↓
Start container
   ↓
postStartCommand
```

The container wasn't recreated, so `postCreateCommand` doesn't represent that startup event.

---

# Important Lifecycle Difference

This is the part I recommend memorizing:

| Command                | Simple mental model       |
| ---------------------- | ------------------------- |
| `initializeCommand`    | Before container creation |
| `onCreateCommand`      | Container creation        |
| `updateContentCommand` | Workspace/content update  |
| `postCreateCommand`    | After container creation  |
| `postStartCommand`     | After container starts    |

Don't worry about memorizing every edge case right now.

The important distinction is:

```text
CREATE
  ↓
postCreateCommand

START
  ↓
postStartCommand
```

---

# Let's Put Everything Together

Our `devcontainer.json` can now look like:

```json
{
  "name": "Python Dev Container",

  "image": "mcr.microsoft.com/devcontainers/python:3.12",

  "features": {
    "ghcr.io/devcontainers/features/node:1": {
      "version": "22"
    }
  },

  "containerEnv": {
    "APP_ENV": "development"
  },

  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance"
      ],
      "settings": {
        "editor.formatOnSave": true
      }
    }
  },

  "forwardPorts": [
    8000
  ],

  "postCreateCommand": "pip install -r requirements.txt"
}
```

Now look at what each section controls:

```text
                    devcontainer.json
                           │
        ┌──────────────────┼───────────────────┐
        ↓                  ↓                   ↓
    Container            VS Code            Lifecycle
    environment          experience           setup
        │                  │                   │
     image             extensions        postCreateCommand
     features          settings           postStartCommand
     env variables
     ports
```

---

# A Very Important Concept

There are actually **three different layers** involved.

### Layer 1 — Docker

Docker handles:

```text
Image
Container
Network
Volume
```

### Layer 2 — Dev Container

Dev Container configuration handles:

```text
Which image?
Which features?
Which environment variables?
Which ports?
Which lifecycle commands?
```

### Layer 3 — VS Code

VS Code customization handles:

```text
Extensions
Settings
Formatter
Linter
Debugger
```

So:

```text
                  VS Code
                     │
             Dev Containers
                     │
               devcontainer.json
                     │
          ┌──────────┴──────────┐
          ↓                     ↓
       Docker              VS Code setup
          │
    ┌─────┼─────┐
    ↓     ↓     ↓
  Image Container Network
```

This distinction will become **very important when you start using Docker Compose and Codespaces**.

---

# One More Important Example

Suppose later you build your cloud-native development environment:

```text
Enterprise Cloud-Native Project
│
├── Python
├── Flask
├── Celery
├── RabbitMQ
├── Redis
├── PostgreSQL
├── Docker
├── Kubernetes CLI
├── Helm
├── Terraform
└── Azure CLI
```

Your Dev Container could provide the **developer tooling**:

```text
Dev Container
│
├── Python
├── Terraform
├── kubectl
├── Helm
├── Azure CLI
└── VS Code extensions
```

While Docker Compose could provide application dependencies:

```text
Docker Compose
│
├── RabbitMQ
├── Redis
└── PostgreSQL
```

And your actual application:

```text
Flask API
Celery Worker
```

could run alongside them.

That leads naturally into the next important concept:

```text
devcontainer.json
       +
Dockerfile
       +
Docker Compose
       ↓
Complete Development Environment
```

---

# 🧠 What You Should Remember From Module 3

If you remember only these, you're good:

```text
image
    ↓
Which existing image should I use?

dockerFile / build
    ↓
How do I build my own development image?

context
    ↓
Which files are available during the Docker build?

containerEnv
    ↓
Environment variables inside the container

remoteEnv
    ↓
Environment variables for VS Code/remote processes

customizations
    ↓
How should VS Code behave?

extensions
    ↓
Which VS Code extensions should be installed?

postCreateCommand
    ↓
What should happen after creating the container?

postStartCommand
    ↓
What should happen when the container starts?
```

And the overall mental model:

```text
                Git Repository
                      │
                      ↓
             .devcontainer/
                      │
                      ↓
             devcontainer.json
                      │
       ┌──────────────┼──────────────┐
       ↓              ↓              ↓
   Container        VS Code       Lifecycle
   definition     customization    commands
       │              │              │
    image          extensions      postCreate
    features       settings        postStart
    env
    ports
       │
       ↓
 Development Container
       │
       ↓
 VS Code attached
       │
       ↓
 🚀 Ready to code
```

**For your learning path, the next useful step is to take this exact `devcontainer-demo` project and build a custom `Dockerfile` instead of using the pre-built Python image.** That will make the relationship between **Dockerfile → image → container → `devcontainer.json`** very clear.
