# GitHub Actions Practice

## About This Project

This repository is created for learning and practicing **GitHub Actions** and basic **CI/CD concepts**.

Today I learned:

* What CI/CD means
* What GitHub Actions is
* How workflows work
* How automation works in DevOps
* YAML workflow structure
* How GitHub automatically runs tasks
* Difference between manual and automatic workflow trigger
* Basic linting automation

This is part of my DevOps learning journey.

---

# What is CI/CD?

CI/CD is a modern DevOps practice used to automate software development processes.

## CI → Continuous Integration

Continuous Integration means developers regularly push code changes to GitHub, and automated workflows verify the code automatically.

### Purpose of CI

* Detect coding issues early
* Improve code quality
* Reduce manual checking
* Run automated validation
* Keep project stable

### Example

Whenever code is pushed:

1. GitHub detects the change
2. Workflow starts automatically
3. Lint/test commands run
4. Result is shown in Actions tab

---

## CD → Continuous Deployment / Delivery

CD means automatically deploying the application after successful checks.

### Purpose of CD

* Faster deployment
* Less manual work
* Reduce deployment mistakes
* Improve release process

---

# What is GitHub Actions?

GitHub Actions is GitHub’s built-in automation platform.

It helps automate:

* Testing
* Linting
* Building applications
* Running scripts
* Deployments
* CI/CD pipelines

---

# Workflow Folder Structure

GitHub Actions workflows must be stored inside:

```bash id="s9m1qz"
.github/workflows/
```

Example:

```bash id="v2u2ow"
.github/workflows/hello.yml
```

---

# Important Workflow Concepts

## 1. Workflow

A workflow is an automated process.

Example:

* Run Python file
* Run linter
* Build Docker image
* Deploy application

---

## 2. Event

Events trigger workflows.

Common events:

* push
* pull_request
* workflow_dispatch
* schedule

Example:

```yaml id="v0n2mt"
on:
  push:
```

This means workflow starts whenever code is pushed.

---

## 3. Jobs

Jobs are groups of tasks inside a workflow.

Example:

* Build Job
* Test Job
* Deploy Job

---

## 4. Runner

Runner is the virtual machine that executes workflow steps.

Example:

```yaml id="r2u7nl"
runs-on: ubuntu-latest
```

GitHub provides:

* Ubuntu
* Windows
* macOS runners

---

## 5. Steps

Each job contains steps.

Example:

* Checkout code
* Install dependencies
* Run commands

---

# Basic Workflow Example

```yaml id="6p3mja"
name: Hello Workflow

on:
  push:

jobs:
  hello-job:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Print Message
        run: echo "Hello Asma"
```

---

# Understanding Each Section

## name

```yaml id="gx8txk"
name: Hello Workflow
```

This is the workflow name visible in GitHub Actions tab.

---

## on

```yaml id="6fxh4o"
on:
  push:
```

Defines when workflow should start.

---

## jobs

```yaml id="bo0scl"
jobs:
```

Container that holds all jobs.

---

## runs-on

```yaml id="sztmbw"
runs-on: ubuntu-latest
```

Defines operating system used by GitHub runner.

---

## steps

```yaml id="o3w7x0"
steps:
```

List of tasks to execute.

---

## uses

```yaml id="g5by0x"
uses: actions/checkout@v4
```

Downloads repository code into runner machine.

---

## run

```yaml id="pwvaf7"
run: echo "Hello"
```

Executes shell command.

---

# What I Understood About workflow_dispatch

```yaml id="qu7q5r"
on:
  workflow_dispatch:
```

This allows manual workflow execution.

Without this:

* workflow runs automatically only on push

With this:

* workflow can also be triggered manually from GitHub Actions tab

---

# Difference Between push and workflow_dispatch

| push                 | workflow_dispatch                        |
| -------------------- | ---------------------------------------- |
| Automatic trigger    | Manual trigger                           |
| Runs after code push | Runs when user clicks Run Workflow       |
| Mostly used in CI    | Mostly used for testing/manual execution |

---

# What is Linting?

Linting means checking code quality automatically.

Linting helps:

* Detect syntax mistakes
* Maintain coding standards
* Improve readability
* Find small bugs early

Example:

```yaml id="mtnuh3"
- name: Run Linter
  run: flake8 .
```

---

# Purpose of lint.yml File

The purpose of `lint.yml` is automation.

Instead of manually checking code every time:

* GitHub automatically runs linting
* Checks code quality
* Shows success or failure
* Saves developer time

So yes, my understanding is:

* Workflow runs automatically after push
* No need to manually execute commands every time
* GitHub Actions automates the process

---

# Basic CI/CD Flow

```text id="9d2d1j"
Developer Pushes Code
        ↓
GitHub Detects Change
        ↓
Workflow Starts
        ↓
Runner Machine Created
        ↓
Steps Execute
        ↓
Lint/Test Runs
        ↓
Success or Failure Status Shown
```

---

# Git Commands Used

```bash id="50jkmb"
git status
git add .
git commit -m "Added GitHub Actions workflow"
git push
```

---

# What I Learned Today

Today I learned:

* GitHub Actions basics
* CI/CD concepts
* Workflow automation
* YAML syntax
* Workflow triggers
* Jobs and steps
* Runner machines
* Linting process
* workflow_dispatch concept
* Automation in DevOps

---

# Future Learning Goals

Next I want to learn:

* Docker CI/CD pipeline
* Deploying applications automatically
* AWS deployment using GitHub Actions
* Secrets management
* Multi-job workflows
* Matrix strategy
* Kubernetes deployment automation

---

# Conclusion

GitHub Actions is a powerful automation tool for DevOps and CI/CD.

This practice helped me understand:

* Automation concepts
* Workflow execution
* CI/CD pipeline basics
* YAML workflow structure
* GitHub automation process

This is an important step in my DevOps journey.
