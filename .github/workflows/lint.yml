name: Auto Linter

on:
  push:
    paths:
      - "**.py"
  workflow_dispatch:

jobs:
  lint:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository Code
        uses: actions/checkout@v4

      - name: Setup Python Environment
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Check Python Version
        run: python --version

      - name: Install Flake8
        run: pip install flake8

      - name: List Repository Files
        run: ls -la

      - name: Run Python Linter
        run: flake8 .

      - name: Workflow Completed
        run: echo "Lint workflow completed successfully"
