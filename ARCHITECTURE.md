# 🏗️ SOC-Aid Architecture

> Evidence-aware agentic workflow for security alert triage.

## 1. Overview

SOC-Aid is structured as an agentic security-alert triage workflow.

The architecture separates deterministic security processing from evidence-aware language-model analysis.

The overall pipeline is:

```text
Security Alert
      │
      ▼
┌──────────────────┐
│  Alert Parsing   │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Alert Correlation│
└────────┬─────────┘
         │
         ▼
┌──────────────────────┐
│ Authentication /     │
│ Evidence Extraction  │
└────────┬─────────────┘
         │
         ▼
┌──────────────────┐
│ Risk Assessment  │
└────────┬─────────┘
         │
         ▼
┌──────────────────────┐
│ Evidence-Aware LLM   │
│ Analysis             │
└────────┬─────────────┘
         │
         ▼
┌──────────────────────┐
│ Recommendation Engine │
└────────┬─────────────┘
         │
         ▼
┌──────────────────────┐
│ Human SOC Analyst     │
│ Review                │
└──────────────────────┘
```

---

## 2. Core Design Principles

### 🔎 Evidence First

The workflow preserves relevant evidence before generating AI analysis.

The AI analysis therefore receives structured information produced by the earlier workflow stages.

### 📊 Deterministic Risk Layer

Risk assessment is performed using explicit scoring rules rather than relying entirely on the LLM.

This provides:
- Reproducibility
- Explainability
- Consistent severity handling
- A clear basis for escalation

### 🤖 AI-Assisted, Not AI-Controlled

The LLM provides analysis and interpretation of available evidence.

It does not independently authorize security actions.

### 👤 Human-in-the-Loop

The final security decision remains with a human SOC analyst.

Autonomous blocking is disabled.

---

## 3. Workflow State

SOC-Aid maintains structured workflow state containing the information required by downstream nodes.

The final state includes:

```text
alert
parsed_alert
related_alerts
authentication_evidence
risk_assessment
analysis
recommendation
decision
error
```

This structure allows evidence and decisions to remain connected throughout the workflow.

---

## 4. Alert Parsing

The parsing stage validates and normalizes incoming security alerts.

It checks required fields and validates supported severity values.

Expected severity categories include:

```text
LOW
MEDIUM
HIGH
CRITICAL
```

Invalid alerts are handled through explicit error handling rather than being silently accepted.

---

## 5. Alert Correlation

After parsing, SOC-Aid searches for related security activity.

Correlation can use contextual attributes such as:

- User
- Source IP
- Authentication activity

The purpose is to move from isolated-alert analysis toward activity-based triage.

For example:

```text
Failed Login
Failed Login
Failed Login
      │
      ├── same user
      ├── same source IP
      └── related authentication activity
              │
              ▼
        Successful Login
```

This context can significantly change the interpretation of an otherwise ordinary event.

---

## 6. Authentication Evidence

Authentication evidence is explicitly preserved in workflow state.

The evidence structure includes:

```text
failed_login_count
time_window_minutes
pattern_detected
first_failed_login
last_failed_login
```

The final verification demonstrated the following evidence:

```text
Failed Logins : 50
First Failure : 2026-08-19 10:20:00
Last Failure  : 2026-08-19 10:28:10
Time Window   : 8.17 minutes
Pattern       : True
```

The evidence is derived from the actual correlated failed-login events.

The first and last timestamps were verified against the first and last actual failed events.

---

## 7. Risk Assessment

SOC-Aid performs deterministic risk assessment before AI analysis.

Base severity scores are:

| Severity | Score |
|---|---:|
| LOW | 10 |
| MEDIUM | 30 |
| HIGH | 60 |
| CRITICAL | 90 |

Contextual evidence can increase the score.

The final score is capped at:

```text
100
```

Risk levels are derived from the resulting score:

| Score | Risk Level |
|---:|---|
| 0–29 | LOW |
| 30–59 | MEDIUM |
| 60–79 | HIGH |
| 80–100 | CRITICAL |

This layer provides an explainable security-risk signal independent of the LLM.

---

## 8. Evidence-Aware LLM Analysis

The LLM analysis operates after structured evidence and risk information have been produced.

Its purpose is to interpret the available evidence and provide analyst-oriented context.

The architecture emphasizes:

```text
Evidence
   ↓
Structured State
   ↓
LLM Analysis
   ↓
Explanation
```

rather than:

```text
Raw Alert
   ↓
Unconstrained AI Guess
```

The system is designed to distinguish between supported facts, reasonable inferences, and unknown information.

---

## 9. Hallucination Safeguards

SOC-Aid includes safeguards intended to reduce unsupported claims.

The analysis should remain grounded in:

- The original alert
- Correlated alerts
- Authentication evidence
- Risk assessment
- Available workflow state

When information is unavailable, it should not be presented as an established fact.

This evidence-aware approach is especially important in security operations, where unsupported claims can lead to incorrect investigations or unnecessary response actions.

---

## 10. Recommendation Engine

After analysis, SOC-Aid generates an investigation recommendation.

For high-risk authentication activity, the recommendation can direct the analyst toward:

- Affected account review
- Endpoint review
- Authentication-log review
- Related activity investigation
- Human escalation

The recommendation is advisory.

It does not execute an autonomous blocking action.

---

## 11. Human Oversight

The final decision stage explicitly preserves human control.

The final workflow can produce:

```text
Decision:
Human SOC analyst approval required.
```

This is an intentional safety boundary.

### 🚫 Autonomous Blocking

SOC-Aid does not autonomously block accounts, endpoints, IP addresses, or other resources.

The system is designed to assist the analyst and provide evidence for human review.

---

## 12. Error Handling

Invalid input is handled explicitly.

The project includes testing for invalid alerts and graceful failure behavior.

This prevents malformed input from silently flowing through the complete triage pipeline.

---

## 13. Verification

The architecture was verified through end-to-end testing.

Final evidence verification confirmed:

```text
✓ Authentication evidence integrated
✓ Timestamps preserved
✓ Risk assessment verified
✓ Human oversight preserved
```

The project test suite also reported:

```text
7 passed in 0.02s
```

---

## 14. Source Code Structure

```text
src/
└── soc_aid/
    ├── __init__.py
    ├── agent.py
    ├── models.py
    ├── report.py
    └── tools.py
```

### `agent.py`

Contains the agent/workflow implementation.

### `models.py`

Contains the structured data models used by the project.

### `tools.py`

Contains supporting security-analysis tools such as parsing, correlation, and risk-related processing.

### `report.py`

Contains reporting/output functionality.

---

## 15. Execution Environment

The working MVP was developed and tested in Google Colab.

The project also includes a Gradio-based interface for interacting with the working prototype.

The live Gradio endpoint is runtime-dependent and is therefore treated as a demonstration interface rather than permanent infrastructure.

---

## 16. Architecture Summary

SOC-Aid follows a layered approach:

```text
┌─────────────────────────────────────────┐
│         Human SOC Analyst               │
│            Final Review                 │
└────────────────────┬────────────────────┘
                     │
┌────────────────────▼────────────────────┐
│       Recommendation / Decision         │
└────────────────────┬────────────────────┘
                     │
┌────────────────────▼────────────────────┐
│       Evidence-Aware LLM Analysis       │
└────────────────────┬────────────────────┘
                     │
┌────────────────────▼────────────────────┐
│          Deterministic Risk             │
│             Assessment                  │
└────────────────────┬────────────────────┘
                     │
┌────────────────────▼────────────────────┐
│       Evidence & Correlation            │
└────────────────────┬────────────────────┘
                     │
┌────────────────────▼────────────────────┐
│           Alert Parsing                 │
└────────────────────┬────────────────────┘
                     │
┌────────────────────▼────────────────────┐
│          Security Alert                │
└─────────────────────────────────────────┘
```

The key architectural principle is:

> **Use deterministic logic and preserved evidence to establish the security context, then use AI to assist with interpretation—not to replace human security judgment.**
