# Suchak by Protomate AI

Backend for Suchak, the AI Assistant for the IISER Bhopal Community.

> **NOTE**
> This repo contains the backend for Suchak. This can be cloned and used as a template for other similar projects.
> However, Protomate AI does not yet accept contributions to the backend code.

## Installation

### Clone the Repository

```bash
git clone git remote https://github.com/sattwik-protomate/suchak-backend.git
```

## Setup Environment

Create the virtual environment and install the necessary packages.

```bash
python -m pip install poetry
# OR
conda install poetry

python -m venv .venv
poetry shell
poetry install
```

## Usage

### Start the Server

```bash
python -m suchak server start
```

### Check server health

```bash
python -m suchak server health
```

### Parse Documents

```bash
python -m suchak parser docs --output=<OUTPUT_FORMAT> <PATH>
```

---

> Created with ❤️ by Protomate AI
