# ⚙️ SOC-Aid Installation & Setup

> Setup instructions for the SOC-Aid MVP.

## 1. Overview

SOC-Aid was developed and tested primarily in **Google Colab**.

The project uses Python-based security-analysis components together with an LLM-powered analysis layer and a Gradio interface for the working demonstration.

This guide explains how to prepare the environment and run the project.

---

## 2. Requirements

Before starting, make sure you have:

- 🐍 Python 3.x
- 📓 Google Colab or a compatible Python environment
- 🔑 A valid Groq API key
- 📦 Internet access for installing dependencies
- 📁 The SOC-Aid repository

Project dependencies are defined in:

```text id="qg9y0x"
requirements.txt
```

---

## 3. Recommended Environment: Google Colab

Google Colab is the recommended environment for the current MVP because the working prototype was developed and tested there.

### Basic Setup

Open the SOC-Aid notebook in Google Colab and connect the runtime.

Then run the dependency-installation/setup cells provided by the notebook.

---

## 4. Repository Structure

The repository follows this structure:

```text id="f1z0pv"
SOC-Aid/
│
├── src/
│   └── soc_aid/
│       ├── __init__.py
│       ├── agent.py
│       ├── models.py
│       ├── report.py
│       └── tools.py
│
├── tests/
│   └── test_soc_aid.py
│
├── README.md
├── ARCHITECTURE.md
├── ANALYST_GUIDE.md
├── INSTALLATION.md
├── USAGE.md
├── TESTING.md
├── SECURITY.md
├── PROBLEM_RESEARCH.md
├── ROADMAP.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── LICENSE
└── requirements.txt
```

---

## 5. Install Dependencies

From the project root, dependencies can be installed with:

```bash id="e4v8dg"
pip install -r requirements.txt
```

If using the original Google Colab prototype, use the package-installation cell already provided in the notebook.

---

## 6. API Key Configuration

SOC-Aid uses a Groq API key for LLM-powered analysis.

### 🔐 Google Colab Secret

The recommended configuration is to store the API key in **Google Colab Secrets**.

Use the exact secret name:

```text id="0v4fkn"
GROQ_API_KEY
```

The notebook retrieves the key at runtime.

### Do Not Hard-Code the Key

Do **not** write:

```python
GROQ_API_KEY = "your-real-api-key"
```

inside the notebook or source code.

Instead, retrieve the secret through the Colab secret mechanism used by the project.

---

## 7. Why Secrets Are Used

Keeping the API key outside the source code helps prevent accidental exposure through:

- Git commits
- GitHub repositories
- Screenshots
- Notebook sharing
- Copy/paste
- Public documentation

🔒 **Never commit a real API key to GitHub.**

---

## 8. Environment Configuration

The working prototype initializes the LLM using the configured API key.

The current project uses a Groq-backed LLM through the LangChain integration.

The LLM temperature is configured for deterministic-style analysis:

```text id="6e4k9x"
temperature = 0
```

The exact model configuration should remain consistent with the working notebook unless the model is intentionally changed and re-tested.

---

## 9. Running the Project

After configuring the environment:

### Step 1

Open the SOC-Aid Google Colab notebook.

### Step 2

Connect the runtime.

### Step 3

Make sure `GROQ_API_KEY` is available through Colab Secrets.

### Step 4

Run the setup/dependency cells.

### Step 5

Run the SOC-Aid workflow cells in order.

### Step 6

Run the testing/verification cells as required.

### Step 7

Start the Gradio interface.

### Step 8

Open the generated Gradio URL.

---

## 10. Starting the Demo Interface

The working MVP includes a Gradio-based user interface.

When the interface starts successfully, a runtime-generated URL is displayed.

Example format:

```text id="u8q5u1"
https://xxxxxxxx.gradio.live
```

The exact URL will change depending on the active runtime.

### ⚠️ Important

The Gradio URL is not a permanent deployment address.

It depends on the active Google Colab runtime.

If the runtime is stopped, reset, or disconnected, the previous demo endpoint may become unavailable.

---

## 11. Verifying the Installation

After setup, verify that the project can:

- Load required dependencies
- Access the configured API secret
- Initialize the SOC-Aid workflow
- Process a valid alert
- Handle invalid input
- Generate a triage result
- Start the Gradio interface

A successful setup should allow the complete workflow to run without configuration errors.

---

## 12. Running Automated Tests

From the repository root:

```bash id="q2z3sn"
pytest
```

The final MVP verification reported:

```text id="4t8p8f"
7 passed in 0.02s
```

The exact execution time can vary depending on the environment.

---

## 13. Evidence Verification

After setup, the authentication evidence workflow can also be verified.

The final verification produced:

```text id="1a8f7z"
Failed Logins : 50
First Failure : 2026-08-19 10:20:00
Last Failure  : 2026-08-19 10:28:10
Time Window   : 8.17 minutes
Pattern       : True
```

This confirms that the relevant authentication evidence was integrated into the workflow.

---

## 14. Expected Risk Verification

The final verification also confirmed:

```text id="y9j0kp"
Risk Level : CRITICAL
Risk Score : 100
```

The risk result is produced by the deterministic risk-assessment layer.

It should be interpreted together with the underlying evidence.

---

## 15. Troubleshooting

### 🔴 `GROQ_API_KEY` Not Found

Check:

1. The Colab runtime is connected.
2. The secret exists in Google Colab.
3. The secret is named exactly:

```text id="7s1c4x"
GROQ_API_KEY
```

4. The notebook is using the correct secret-retrieval code.

---

### 🔴 Dependency Error

Run:

```bash id="x1c0v8"
pip install -r requirements.txt
```

Then restart the runtime if required by the dependency installation and rerun the setup cells.

---

### 🔴 Gradio URL Does Not Appear

Check:

- The Gradio cell is running.
- Required dependencies are installed.
- The runtime is connected.
- The application did not raise an exception.
- The required API configuration is available.

---

### 🔴 Notebook Shows "Executing"

A Gradio server cell can remain active while the web interface is running.

If the Gradio URL is available and the interface works, the active cell can be normal behavior.

The server process is what keeps the demo interface available.

---

### 🔴 Tests Fail

Run:

```bash id="w4j7k9"
pytest
```

Read the failure output before modifying project code.

Do not assume a test failure is an installation problem; it may indicate a project or environment issue that needs investigation.

---

## 16. Clean Environment Principle

The GitHub repository contains the **source-code project structure and documentation**.

The working Google Colab notebook is used as the project development/demo environment.

Runtime-specific files, temporary files, credentials, and generated artifacts should not be committed to the repository.

---

## 17. Security Checklist

Before pushing changes to GitHub, verify:

- [ ] No API key is present in source files.
- [ ] No password or access token is committed.
- [ ] No `.env` file containing secrets is committed.
- [ ] No private credentials are included.
- [ ] Temporary runtime files are excluded.
- [ ] Tests pass after relevant changes.

---

## 18. Recommended Setup Flow

```text id="8h1m7b"
Open Google Colab
       ↓
Connect Runtime
       ↓
Configure GROQ_API_KEY Secret
       ↓
Install Dependencies
       ↓
Run SOC-Aid Cells
       ↓
Run Tests / Verification
       ↓
Start Gradio
       ↓
Open Demo URL
       ↓
Review Triage Result
```

---

## 19. Installation Status

The current SOC-Aid MVP has been successfully configured and tested in the intended Google Colab environment.

Final verification:

```text id="3g5y6m"
Environment Setup      ✓
Dependencies           ✓
API Secret Handling    ✓
Alert Processing       ✓
Evidence Integration   ✓
Risk Assessment        ✓
Testing                ✓
Gradio Interface       ✓
Human Oversight        ✓
```

---

## 20. Important Note

SOC-Aid is currently an **MVP prototype** rather than a production deployment.

For production use, additional controls would be required around:

- Authentication
- Authorization
- Secrets management
- Data privacy
- Logging
- Monitoring
- Dependency management
- Deployment security
- Incident-response integration

The current installation is intended for development, testing, demonstration, and evaluation.
