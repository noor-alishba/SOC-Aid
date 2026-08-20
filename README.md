# 🛡️ SOC-Aid

> **Evidence-Aware Agentic AI for Security Alert Triage**

SOC-Aid is an AI-assisted Security Operations Center (SOC) alert-triage agent designed to help security analysts understand alerts, correlate related activity, assess risk, analyze available evidence, and identify recommended investigation steps.

The project combines deterministic security logic with evidence-aware LLM analysis while keeping **human analysts in control of security decisions**.

---

## 🎯 Project Goal

Security Operations Centers receive large numbers of alerts that require investigation and prioritization.

SOC-Aid provides a structured triage workflow that transforms a raw security alert into an explainable investigation result:

**Security Alert → Parsing → Correlation → Evidence Extraction → Risk Assessment → AI Analysis → Recommendation → Human Review**

The system is designed to assist analysts rather than replace them.

---

## ✨ Key Features

### 🔎 Security Alert Parsing
- Validates incoming alert data.
- Normalizes required security fields.
- Handles invalid or incomplete input gracefully.
- Validates supported severity levels.

### 🔗 Related Alert Correlation
SOC-Aid identifies related activity using available alert context such as:
- User
- Source IP
- Event type
- Related authentication activity

This allows an individual alert to be evaluated within its surrounding activity.

### 📊 Explainable Risk Assessment
SOC-Aid uses a deterministic risk-assessment layer before AI analysis.

Severity contributes to the initial risk score:

| Severity | Base Score |
|---|---:|
| LOW | 10 |
| MEDIUM | 30 |
| HIGH | 60 |
| CRITICAL | 90 |

Additional contextual evidence can increase the score, with the final score capped at **100**.

Risk levels are mapped as:

- **LOW:** score < 30
- **MEDIUM:** score 30–59
- **HIGH:** score 60–79
- **CRITICAL:** score ≥ 80

This makes the core risk decision explainable and reproducible.

### 🔐 Authentication Evidence

For authentication-related activity, SOC-Aid preserves evidence from correlated failed-login events, including:

- Failed-login count
- First failed-login timestamp
- Last failed-login timestamp
- Calculated time window
- Authentication pattern detection

During final verification, the system correctly preserved:

- **50 failed logins**
- **First failure:** `2026-08-19 10:20:00`
- **Last failure:** `2026-08-19 10:28:10`
- **Calculated window:** `8.17 minutes`
- **Pattern detected:** `True`

### 🤖 Evidence-Aware AI Analysis

The LLM analysis is performed using evidence available in the workflow state.

SOC-Aid is designed to distinguish between:
- Known facts supported by evidence
- Reasonable inferences
- Information that is unknown or unavailable

This reduces unsupported conclusions and helps maintain analyst trust.

### 🛡️ Hallucination Safeguards

The system includes evidence-safety checks so that AI analysis is grounded in the alert and correlated evidence rather than unsupported assumptions.

### 💡 Investigation Recommendations

SOC-Aid produces investigation-oriented recommendations based on the available evidence.

For high-risk authentication activity, the system can recommend escalation and review of relevant:
- Account activity
- Endpoint activity
- Authentication logs
- Related security events

### 👤 Human Oversight

Security decisions remain under human control.

**Human SOC analyst approval is required.**

🚫 Autonomous blocking is disabled.

---

## 🧠 SOC-Aid Workflow

```text
                    ┌─────────────────────┐
                    │   Security Alert    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Alert Parsing     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Alert Correlation   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Evidence Extraction │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Risk Assessment    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Evidence-Aware LLM  │
                    │      Analysis       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Investigation       │
                    │ Recommendation      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Human SOC Analyst   │
                    │       Review        │
                    └─────────────────────┘
```

---

## 🧪 Testing & Verification

SOC-Aid was tested across core functionality and safety/reliability scenarios.

### Core Functional Tests

The project includes tests covering:

- Suspicious login
- Normal login
- Critical malware
- Invalid alert handling

Final automated test result:

```text
7 passed in 0.02s
```

### Final Evidence Verification

The authentication evidence integration was independently verified.

```text
Failed Logins : 50
Time Window   : 8.17 minutes
Pattern       : True
First Failure : 2026-08-19 10:20:00
Last Failure  : 2026-08-19 10:28:10
Risk Level    : CRITICAL
Risk Score    : 100
```

The final verification confirmed:

- ✓ Authentication evidence integrated
- ✓ Timestamps preserved
- ✓ Risk assessment verified
- ✓ Human oversight preserved

---

## 🖥️ Working Prototype

The SOC-Aid MVP was developed and tested in **Google Colab**.

The prototype includes a Gradio-based user interface where an analyst can provide security alert information and receive the generated triage result.

The live Gradio URL is generated when the application is running in the Colab runtime.

> **Note:** The Gradio URL is a runtime-based demo endpoint and should not be treated as a permanent deployment URL.

---

## 📁 Repository Structure

```text
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

## 🔐 Security & Safety Principles

SOC-Aid follows several safety principles:

1. **Evidence before inference**
2. **Explainable risk assessment**
3. **Graceful invalid-input handling**
4. **Evidence-aware AI analysis**
5. **Human approval for security decisions**
6. **No autonomous blocking**

The system is intended to support analysts, not make irreversible security decisions autonomously.

---

## 🚀 Current Status

### SOC-Aid MVP — READY

| Capability | Status |
|---|---|
| Alert Parsing | ✅ |
| Alert Correlation | ✅ |
| Authentication Evidence | ✅ |
| Risk Assessment | ✅ |
| Evidence-Aware AI Analysis | ✅ |
| Recommendation Engine | ✅ |
| Explainable Output | ✅ |
| Error Handling | ✅ |
| Hallucination Safeguards | ✅ |
| Human Oversight | ✅ |
| Autonomous Blocking | 🚫 Disabled |

---

## 🛣️ Roadmap

Future improvements can build on the current MVP with additional integrations, richer security telemetry, improved analyst workflows, and broader alert coverage.

See [`ROADMAP.md`](ROADMAP.md) for the project roadmap.

---

## 📄 Documentation

- [`ARCHITECTURE.md`](ARCHITECTURE.md) — System architecture and workflow
- [`ANALYST_GUIDE.md`](ANALYST_GUIDE.md) — Analyst-oriented guidance
- [`INSTALLATION.md`](INSTALLATION.md) — Installation and environment setup
- [`USAGE.md`](USAGE.md) — Usage instructions
- [`TESTING.md`](TESTING.md) — Testing strategy and results
- [`SECURITY.md`](SECURITY.md) — Security considerations
- [`PROBLEM_RESEARCH.md`](PROBLEM_RESEARCH.md) — Problem background and research
- [`ROADMAP.md`](ROADMAP.md) — Future development
- [`CHANGELOG.md`](CHANGELOG.md) — Project changes

---

## ⚠️ Disclaimer

SOC-Aid is an AI-assisted security triage prototype. It is intended to support human analysts and should not be treated as an autonomous security-response system.

**Human SOC analyst review is required for security decisions.**
