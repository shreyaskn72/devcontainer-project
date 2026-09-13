 **Lets learn Dev Containers practically with VS Code + GitHub Copilot**, I’d recommend learning it as a **single progressive project**, rather than studying Dev Container concepts independently.

The goal can be: **take a normal application → containerize the development environment → configure VS Code → add services → use Copilot effectively → make the setup reproducible for the team → use it in CI/CD.**

# Dev Containers + VS Code + GitHub Copilot — Learning TOC

## Module 0 — What Problem Does Dev Container Solve?

### 0.1 Development Environment Problems

* "Works on my machine"
* Different Python/Node/Java versions
* OS differences
* Dependency conflicts
* Local tool installation
* Onboarding a new developer

### 0.2 What is a Dev Container?

* Container vs Dev Container
* Development container vs production container
* Why Docker alone isn't enough
* Reproducible development environments

[0.2 What is a Dev Container?](theory/module_0/0.2_what_is_dev_container.md)

### 0.3 Dev Container Architecture

```text
Developer
   │
   ▼
VS Code
   │
   ▼
Dev Containers Extension
   │
   ▼
Docker
   │
   ▼
Development Container
   │
   ├── Source Code
   ├── Runtime
   ├── Tools
   ├── Dependencies
   └── VS Code Extensions
```
[0.3 Dev Container Architecture](theory/module_0/0.3_dev_container_architecture.md)


### 0.4 Dev Container Lifecycle

```text
Open Repository
      ↓
Read devcontainer.json
      ↓
Build Image
      ↓
Create Container
      ↓
Mount Source Code
      ↓
Install Tools / Extensions
      ↓
VS Code attaches
      ↓
Start Development
```

[0.4 Dev Container Lifecycle](theory/module_0/0.4_dev_container_lifecycle.md)
---

# Module 1 — Prerequisites

### 1.1 Docker Fundamentals

* Images
* Containers
* Volumes
* Networks
* Dockerfile
* Docker Compose


[1.1 Docker Fundamentals](theory/module_1/1.1_docker_fundamentals.md)

### 1.2 VS Code Fundamentals

* Extensions
* Integrated Terminal
* Workspace
* Settings
* Remote Development

### 1.3 Git Fundamentals

* Repository
* Branch
* `.gitignore`
* GitHub repository structure

### 1.4 GitHub Copilot Fundamentals

* Copilot Chat
* Inline suggestions
* Agent-style development
* Repository context

---

# Module 2 — Your First Dev Container

**Lab 1 — Create a Python project**

```text
devcontainer-demo/
├── .devcontainer/
│   └── devcontainer.json
├── app/
│   └── main.py
├── requirements.txt
└── README.md
```

Learn:

* `.devcontainer/`
* `devcontainer.json`
* `image`
* `features`
* `customizations`
* `forwardPorts`
* `postCreateCommand`

### Lab

Start with:

```text
Mac
 │
 ├── VS Code
 │
 └── Docker Desktop
        │
        ▼
   Python Dev Container
```

Verify:

```bash
python --version
pip --version
```

Then run the application **inside the container**.

---

# Module 3 — Understanding `devcontainer.json`

This is the most important module.

### 3.1 Basic Configuration

```json
{
  "name": "Python Dev Container",
  "image": "mcr.microsoft.com/devcontainers/python:3.12"
}
```

### 3.2 Container Configuration

* `image`
* `dockerFile`
* `context`
* `build`
* `containerEnv`
* `remoteEnv`

### 3.3 VS Code Configuration

* Extensions
* Settings
* Themes
* Formatters
* Linters

Example:

```json
"customizations": {
  "vscode": {
    "extensions": [
      "ms-python.python"
    ]
  }
}
```

### 3.4 Lifecycle Commands

* `initializeCommand`
* `onCreateCommand`
* `updateContentCommand`
* `postCreateCommand`
* `postStartCommand`

Understand **when each command executes**.

---

# Module 4 — Dev Container Features

### 4.1 What are Features?

Instead of building everything yourself:

```text
Base Image
    +
Python Feature
    +
Node Feature
    +
Azure CLI Feature
    +
Terraform Feature
```

### 4.2 Add Features

Learn:

* Feature registry
* Feature configuration
* Version selection
* Multiple features

### Lab

Create a development environment containing:

```text
Python
Node.js
Azure CLI
Terraform
kubectl
```

---

# Module 5 — Custom Dev Container Image

Now move beyond prebuilt images.

### 5.1 Dockerfile + Dev Container

```text
.devcontainer/
├── devcontainer.json
└── Dockerfile
```

### 5.2 Build Arguments

* `ARG`
* environment variables
* version pinning

### 5.3 Installing Development Tools

* OS packages
* Python packages
* CLI tools
* npm packages

### 5.4 Image Optimization

* Layer caching
* Smaller images
* Multi-stage builds
* Reproducibility

### Lab

Build your own:

```text
Python + Node + Terraform + kubectl
```

development image.

---

# Module 6 — Source Code & Workspace

Understand where your code actually lives.

### 6.1 Workspace Mounting

```text
Mac filesystem
      │
      ▼
Docker volume / bind mount
      │
      ▼
/workspaces/project
```

### 6.2 Workspace Folder

* `workspaceFolder`
* `workspaceMount`

### 6.3 Git Inside Container

* Git installation
* Git credentials
* SSH
* GitHub authentication

### 6.4 File Permissions

Especially important on:

```text
Linux
Mac
Windows
```

---

# Module 7 — Environment Variables & Secrets

### 7.1 Environment Variables

```json
"containerEnv": {
  "APP_ENV": "development"
}
```

### 7.2 `containerEnv` vs `remoteEnv`

Understand the difference.

### 7.3 `.env` Files

### 7.4 Secrets

What **should NOT** go into:

```text
devcontainer.json
Dockerfile
.env committed to Git
```

### 7.5 Development Secrets Strategy

Learn:

```text
Developer
   ↓
Local Secret
   ↓
Dev Container
```

and later:

```text
GitHub Codespaces / CI
        ↓
GitHub Secrets
```

---

# Module 8 — Dev Container + Docker Compose

This is where Dev Containers become really powerful.

### 8.1 Why Compose?

Instead of:

```text
App Container
```

you can create:

```text
App
 │
 ├── PostgreSQL
 ├── Redis
 └── RabbitMQ
```

### 8.2 Dev Container with Compose

```text
.devcontainer/
├── devcontainer.json
└── docker-compose.yml
```

### 8.3 Service Configuration

* `service`
* `runServices`
* `shutdownAction`

### Lab

Build:

```text
                ┌──────────────┐
                │ VS Code      │
                │ Dev Container│
                └──────┬───────┘
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       Flask         Redis       PostgreSQL
```

---

# Module 9 — Networking Inside Dev Containers

Learn how containers communicate.

### 9.1 Container Network

### 9.2 Service Discovery

Why this works:

```text
postgres:5432
```

instead of:

```text
localhost:5432
```

### 9.3 Port Forwarding

```json
"forwardPorts": [8000, 5432]
```

### 9.4 `localhost` — Host vs Container

This is a **very important concept**.

### Lab

Run:

```text
FastAPI
PostgreSQL
Redis
```

and make them communicate.

---

# Module 10 — VS Code Extensions Inside Dev Containers

Understand:

```text
Host VS Code
      │
      ├── Local Extensions
      │
      └── Container Extensions
```

Learn:

* Extension installation
* `customizations.vscode.extensions`
* Settings
* Language servers
* Debuggers
* Linters
* Formatters

### Lab

Configure:

```text
Python
Pylance
Black
Ruff
Docker
GitHub Copilot
Kubernetes
```

---

# Module 11 — GitHub Copilot + Dev Containers

This should be a dedicated module because this is part of your goal.

### 11.1 Copilot Inside the Development Environment

Understand:

```text
VS Code
   │
   ├── Dev Container
   │      ├── Source Code
   │      ├── Runtime
   │      └── Tools
   │
   └── GitHub Copilot
```

### 11.2 Ask Copilot to Create a Dev Container

For example:

> Create a Dev Container configuration for this Python project.

### 11.3 Ask Copilot to Analyze Existing Configuration

Examples:

> Explain this devcontainer.json.

> Why is this container failing to start?

> Add PostgreSQL to this development environment.

### 11.4 Copilot + Dockerfile

Use Copilot to:

* Generate Dockerfiles
* Optimize Dockerfiles
* Explain layers
* Debug build failures

### 11.5 Copilot + Compose

Ask Copilot to:

* Add Redis
* Add PostgreSQL
* Configure networking
* Add health checks

---

# Module 12 — Copilot as a Dev Container Learning Assistant

This is where I'd make the learning **lab-based**.

For every lab:

```text
You
 │
 ▼
Define requirement
 │
 ▼
Ask Copilot
 │
 ▼
Review generated configuration
 │
 ▼
Run it
 │
 ▼
Break something intentionally
 │
 ▼
Ask Copilot to diagnose
 │
 ▼
Understand the solution
```

Important principle:

> **Don't blindly accept Copilot-generated Dev Container configuration.**

Learn to review:

* Security
* Image versions
* Permissions
* Ports
* Secrets
* Dependencies
* Reproducibility

---

# Module 13 — Debugging Dev Containers

### 13.1 Container Won't Build

### 13.2 Container Starts but VS Code Cannot Attach

### 13.3 Extension Problems

### 13.4 Permission Problems

### 13.5 Port Problems

### 13.6 Network Problems

### 13.7 `postCreateCommand` Failure

### 13.8 Docker Build Cache Problems

### Lab

Intentionally introduce:

```text
Wrong image
Wrong port
Missing dependency
Bad command
Permission issue
Broken extension
```

Then troubleshoot them.

---

# Module 14 — Advanced Dev Container Configuration

### 14.1 Multiple Development Containers

### 14.2 Non-root User

### 14.3 `remoteUser`

### 14.4 `containerUser`

### 14.5 Mounts

### 14.6 Volumes

### 14.7 GPU / Hardware Access

### 14.8 Resource Limits

### 14.9 Lifecycle Optimization

---

# Module 15 — Dev Container Security

Very important for production-quality development environments.

### 15.1 Don't Put Secrets in Images

### 15.2 Don't Commit Credentials

### 15.3 Image Trust

### 15.4 Dependency Security

### 15.5 Running as Non-root

### 15.6 Container Capabilities

### 15.7 Supply Chain Security

### 15.8 Pinning Image Versions

---

# Module 16 — Team Development

Now think like an architect.

### 16.1 Shared Development Environment

```text
Git Repository
      │
      ▼
.devcontainer/
      │
      ▼
Every Developer
      │
      ▼
Same Environment
```

### 16.2 Onboarding a New Developer

Target:

```text
git clone
     ↓
Open in VS Code
     ↓
Reopen in Container
     ↓
Start coding
```

### 16.3 Standardizing Developer Tooling

### 16.4 Versioning Dev Container Configuration

### 16.5 Dev Container Documentation

---

# Module 17 — Dev Containers + GitHub

### 17.1 Repository Integration

### 17.2 GitHub Codespaces

Understand the relationship:

```text
Dev Container
     │
     ├── Local VS Code
     │
     └── GitHub Codespaces
```

### 17.3 Local Dev Container vs Codespaces

| Feature          | Local Dev Container | Codespaces          |
| ---------------- | ------------------- | ------------------- |
| Docker           | Local               | Cloud               |
| VS Code          | Local               | Browser/desktop     |
| Compute          | Developer machine   | Cloud               |
| Environment      | `devcontainer.json` | `devcontainer.json` |
| Team consistency | Yes                 | Yes                 |

### 17.4 `.devcontainer` as the Development Contract

---

# Module 18 — Dev Containers + CI/CD

Understand an important distinction:

```text
Development Container
        ≠
Production Container
```

Then:

```text
Dev Container
      ↓
Developer Testing
      ↓
Git Push
      ↓
CI
      ↓
Production Image
      ↓
AKS
```

Learn:

* GitHub Actions
* Docker build
* Testing
* Image scanning
* Container registry
* Deployment

---

# Module 19 — Production-Style Project

Now combine everything.

## Project: Python Microservices Development Environment

Build:

```text
                         VS Code
                            │
                            ▼
                    Dev Container
                            │
              ┌─────────────┼─────────────┐
              │             │             │
            Flask         Celery        Tools
              │             │
              ▼             ▼
          PostgreSQL      RabbitMQ
              │
              ▼
            Redis
```

The Dev Container should contain:

* Python
* Node.js
* Git
* Docker CLI
* kubectl
* Helm
* Terraform
* Azure CLI
* VS Code extensions
* GitHub Copilot

---

# Module 20 — Capstone Project

### Build a Production-Like Development Environment

Repository:

```text
cloud-native-dev-environment/
│
├── .devcontainer/
│   ├── devcontainer.json
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── services/
│   ├── api/
│   └── worker/
│
├── infrastructure/
│   ├── terraform/
│   └── kubernetes/
│
├── tests/
│
├── .github/
│   └── workflows/
│
└── README.md
```

### Final Environment

```text
                   Developer
                       │
                       ▼
                    VS Code
                       │
              GitHub Copilot
                       │
                       ▼
              ┌─────────────────┐
              │  Dev Container  │
              │                 │
              │ Python          │
              │ Node            │
              │ Terraform       │
              │ kubectl         │
              │ Helm            │
              │ Azure CLI       │
              └────────┬────────┘
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       PostgreSQL    RabbitMQ      Redis
```

---

## Recommended Learning Path

Given your **Kubernetes → Helm → ArgoCD → Terraform → Azure/AKS** learning path, I would **not** spend too much time on generic Docker theory.

I'd structure your actual hands-on learning as:

```text
Module 0  → Why Dev Containers?
     ↓
Module 1  → Prerequisites
     ↓
Module 2  → First Dev Container
     ↓
Module 3  → devcontainer.json
     ↓
Module 4  → Features
     ↓
Module 5  → Custom Dockerfile
     ↓
Module 6  → Workspace & Git
     ↓
Module 7  → Environment & Secrets
     ↓
Module 8  → Docker Compose
     ↓
Module 9  → Networking
     ↓
Module 10 → VS Code Extensions
     ↓
Module 11 → GitHub Copilot + Dev Containers
     ↓
Module 12 → Copilot-assisted development
     ↓
Module 13 → Troubleshooting
     ↓
Module 14 → Advanced configuration
     ↓
Module 15 → Security
     ↓
Module 16 → Team development
     ↓
Module 17 → GitHub Codespaces
     ↓
Module 18 → CI/CD
     ↓
Module 19 → Production-style project
     ↓
Module 20 → Capstone
```

**One important recommendation:** make **Modules 2–19 one continuous project**. Each lab should modify the same repository rather than creating 15 unrelated examples. That way, by the end you'll have a real `.devcontainer` setup that looks like something you'd actually use for your Python/AKS/Kubernetes work.
