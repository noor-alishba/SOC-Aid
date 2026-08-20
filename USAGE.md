# 🚀 SOC-Aid Usage Guide

> How to run, interact with, and evaluate the SOC-Aid MVP.

## 1. Overview

SOC-Aid is an AI-assisted security-alert triage system designed to help SOC analysts understand and prioritize security alerts.

The working MVP was developed and tested in **Google Colab** and includes a Gradio-based interface for interacting with the system.

The typical workflow is:

```text
Security Alert
      ↓
Alert Parsing
      ↓
Related Alert Correlation
      ↓
Evidence Extraction
      ↓
Risk Assessment
      ↓
Evidence-Aware AI Analysis
      ↓
Investigation Recommendation
      ↓
Human SOC Analyst Review
```

---

## 2. Requirements

Before running SOC-Aid, make sure the environment has:

- Python
- Required project dependencies
- A valid Groq API key
- Google Colab or another compatible Python environment

The project dependencies are listed in:

```text
requirements.txt
```

---

## 3. Google Colab Setup

The working MVP can be run directly in Google Colab.

### Step 1 — Open the Notebook

Open the working SOC-Aid notebook in Google Colab.

The notebook contains the project workflow, security-alert processing logic, testing, and the working user interface.

---

### Step 2 — Install Dependencies

Install the required packages from the project's dependency list.

```bash
pip install -r requirements.txt
```

If working directly with the original Colab prototype, use the package-installation cell provided in the notebook.

---

## 4. API Key Configuration

SOC-Aid uses a Groq API key for the LLM-powered analysis.

The working Colab prototype is designed to retrieve the API key from **Google Colab Secrets**.

### Expected Secret Name

```text
GROQ_API_KEY
```

The API key should **not** be written directly into notebook code.

### Recommended Setup

In Google Colab:

```text
Secrets
   ↓
Add new secret
   ↓
Name: GROQ_API_KEY
   ↓
Store the API key securely
```

The notebook retrieves the secret at runtime.

---

## 5. Running the Project

Once the environment and API key are configured:

1. Open the SOC-Aid notebook.
2. Make sure the required secret is available.
3. Run the project cells in order.
4. Confirm that the security-alert tools initialize successfully.
5. Start the SOC-Aid workflow.
6. Start the Gradio interface.
7. Open the generated Gradio URL in a browser.

---

## 6. Running the Working Prototype

The final notebook contains the working prototype and user interface.

When the Gradio interface starts, the notebook generates a URL.

It may look similar to:

```text
https://xxxxxxxx.gradio.live
```

or another Gradio-generated address depending on the runtime.

### Important

The Gradio URL is associated with the active runtime/session.

It is a **demo endpoint**, not a permanent production deployment.

If the Colab runtime is stopped or reset, the previous URL may no longer be available.

---

## 7. Using the User Interface

After opening the generated Gradio URL:

```text
Gradio URL
     ↓
Browser
     ↓
SOC-Aid Interface
     ↓
Provide Security Alert
     ↓
Run Triage
     ↓
Review Triage Result
```

The interface is intended to provide an analyst-friendly way to interact with the SOC-Aid workflow.

---

## 8. Alert Information

A security alert should contain the information required by the SOC-Aid workflow.

Typical fields include:

- Alert ID
- Timestamp
- User
- Source IP
- Event type
- Severity
- Relevant event details

The system validates required fields before processing the alert.

---

## 9. Example Alert Scenarios

The project testing includes multiple security-alert scenarios.

### 🔴 Suspicious Login

A suspicious authentication sequence can be analyzed together with related failed-login activity.

The system can identify:

- Related authentication events
- Failed-login evidence
- Authentication patterns
- Elevated risk
- Investigation recommendations

---

### 🟢 Normal Login

A normal authentication event can be processed without automatically treating every login as malicious.

This helps demonstrate that risk assessment considers context rather than simply labeling every authentication event as suspicious.

---

### 🔥 Critical Malware

The project includes a critical-malware test scenario to verify handling of high-severity security alerts.

---

### ⚠️ Invalid Alert

Invalid or incomplete alerts are used to verify input validation and graceful failure.

The system should not generate a misleading triage result from malformed input.

---

## 10. Authentication Evidence

For authentication-related activity, SOC-Aid can preserve evidence from correlated failed-login events.

The final verification demonstrated:

```text
Failed Logins : 50
First Failure : 2026-08-19 10:20:00
Last Failure  : 2026-08-19 10:28:10
Time Window   : 8.17 minutes
Pattern       : True
```

This evidence contributes to the security context used by downstream processing.

---

## 11. Risk Assessment

SOC-Aid applies deterministic risk scoring before AI analysis.

Base severity scores are:

| Severity | Base Score |
|---|---:|
| LOW | 10 |
| MEDIUM | 30 |
| HIGH | 60 |
| CRITICAL | 90 |

Additional contextual evidence may increase the score.

The maximum risk score is:

```text
100
```

Risk levels are:

| Score | Risk |
|---:|---|
| 0–29 | LOW |
| 30–59 | MEDIUM |
| 60–79 | HIGH |
| 80–100 | CRITICAL |

---

## 12. Understanding the Triage Result

A SOC-Aid result should be reviewed as a complete evidence chain.

Look for:

### 🔎 Alert

What happened?

### 🔗 Related Alerts

What additional activity is connected to the alert?

### 🔐 Evidence

What observable information supports the analysis?

### 📊 Risk

Why was the alert assigned its risk level?

### 🤖 AI Analysis

What does the evidence suggest?

### 💡 Recommendation

What should the analyst investigate next?

### 👤 Decision

What requires human review?

---

## 13. Evidence-Aware AI Analysis

The AI analysis should be interpreted together with the evidence.

SOC-Aid is designed to distinguish:

```text
FACT
↓
Directly supported evidence

INFERENCE
↓
Reasonable interpretation

UNKNOWN
↓
Not established by available evidence
```

Analysts should not treat unsupported AI statements as confirmed security facts.

---

## 14. Human Review

The final security decision remains with a human SOC analyst.

SOC-Aid does not automatically:

- Disable accounts
- Block IP addresses
- Isolate endpoints
- Execute irreversible actions

The analyst should review the evidence and recommendations before deciding on a response.

---

## 15. Running Tests

Tests are located in:

```text
tests/test_soc_aid.py
```

Run the test suite from the project root:

```bash
pytest
```

The final automated verification reported:

```text
7 passed in 0.02s
```

The exact execution time can vary between environments.

---

## 16. Expected Test Status

A successful test run should show all defined tests passing.

Final MVP verification:

```text
Automated Tests       : 7 PASSED
Failed Tests          : 0
Evidence Verification : PASSED
Risk Verification     : PASSED
Safety Checks         : PASSED
Human Oversight       : ENABLED
Autonomous Blocking   : DISABLED
```

---

## 17. Demo Workflow

For a project demonstration, use the following sequence:

```text
1. Open the clean SOC-Aid Colab notebook
          ↓
2. Run the required project cells
          ↓
3. Start the Gradio interface
          ↓
4. Wait for the generated URL
          ↓
5. Open the URL in a browser
          ↓
6. Enter/select the demonstration alert
          ↓
7. Run the triage workflow
          ↓
8. Review the generated result
          ↓
9. Explain the evidence
          ↓
10. Explain the risk assessment
          ↓
11. Explain the AI analysis
          ↓
12. Explain the human-review requirement
```

### Demo Tip 💡

During a demonstration, focus on the **reasoning chain**:

> **Alert → Evidence → Risk → AI Analysis → Recommendation → Human Review**

This demonstrates the core purpose of SOC-Aid more effectively than showing only the final output.

---

## 18. Troubleshooting

### Gradio URL Does Not Appear

Check that:

- The Gradio cell is running.
- Required dependencies are installed.
- The runtime is connected.
- The API configuration is available if required by the workflow.

---

### Notebook Remains Executing

A Gradio server cell may remain in an executing/running state while the interface is active.

This can be normal.

If the interface is working and the URL is available, the running cell is serving the application.

---

### API Key Error

Verify that the Colab Secret exists with the exact name:

```text
GROQ_API_KEY
```

Do not paste the key directly into source code.

---

### Invalid Alert Error

Check that the input contains all required fields and uses a supported severity value.

---

### Tests Fail

Run:

```bash
pytest
```

Then inspect the failing test and error message before changing project logic.

---

## 19. Current MVP Status

```text
🟢 SOC-Aid MVP READY

Alert Parsing              ✓
Alert Correlation          ✓
Evidence Integration      ✓
Risk Assessment            ✓
AI Analysis                ✓
Recommendations            ✓
Error Handling             ✓
Safety Checks              ✓
Human Oversight            ✓
Autonomous Blocking        🚫 Disabled
```

---

## 20. Important Usage Principle

> 🛡️ **SOC-Aid is an analyst-assistance system.**

Use the generated triage result to understand and prioritize security activity, but always verify important conclusions against the available evidence.

The final security decision belongs to the human SOC analyst.
