# 🛡️ SOC-Aid Security & Safety

> Security considerations, responsible use, evidence handling, and safety boundaries for the SOC-Aid MVP.

## 1. Security Overview

SOC-Aid is an AI-assisted security-alert triage prototype designed to help SOC analysts understand and prioritize security events.

Because the system operates in a cybersecurity context, it follows a **security-first and human-in-the-loop approach**.

The system is designed to:

- 🔎 Analyze available security evidence
- 🔗 Correlate related activity
- 📊 Produce explainable risk assessments
- 🤖 Assist with evidence-aware analysis
- 💡 Recommend investigation steps
- 👤 Keep final security decisions under human control

---

## 2. Human-in-the-Loop Security

The most important safety boundary in SOC-Aid is:

> **AI analysis does not replace human security judgment.**

The final security decision must be reviewed by a qualified SOC analyst.

```text
Security Alert
      ↓
SOC-Aid Analysis
      ↓
Evidence + Risk + Recommendation
      ↓
👤 Human SOC Analyst
      ↓
Final Security Decision
```

### 🚫 Autonomous Blocking Disabled

SOC-Aid does not autonomously:

- Block IP addresses
- Disable user accounts
- Isolate endpoints
- Delete resources
- Execute irreversible security actions

This prevents an AI-generated interpretation from directly causing a potentially harmful security action.

---

## 3. Evidence-Aware Security

SOC-Aid follows an:

> **Evidence before inference**

approach.

Analysis should be grounded in information available from:

- Original security alerts
- Correlated alerts
- Authentication evidence
- Risk assessment
- Structured workflow state

The system is designed to distinguish between:

### FACT

Information directly supported by available evidence.

### INFERENCE

A reasonable interpretation derived from the available evidence.

### UNKNOWN

Information that cannot be established from the available evidence.

This distinction helps reduce unsupported security conclusions.

---

## 4. Authentication Evidence

Authentication-related activity can contain important indicators of suspicious behavior.

SOC-Aid preserves relevant authentication evidence such as:

- Failed-login count
- First failed-login timestamp
- Last failed-login timestamp
- Calculated time window
- Detected authentication pattern

The final verification confirmed:

```text id="g4q4yp"
Failed Logins : 50
First Failure : 2026-08-19 10:20:00
Last Failure  : 2026-08-19 10:28:10
Time Window   : 8.17 minutes
Pattern       : True
```

This evidence is used to support downstream risk assessment and analysis.

---

## 5. Explainable Risk Assessment

SOC-Aid does not rely exclusively on an LLM to determine risk.

A deterministic risk-assessment layer provides a structured risk signal.

Base severity scores are:

| Severity | Base Score |
|---|---:|
| LOW | 10 |
| MEDIUM | 30 |
| HIGH | 60 |
| CRITICAL | 90 |

Contextual evidence may increase the score, with a maximum score of:

```text id="j9y3z6"
100
```

Risk categories are:

| Score | Risk Level |
|---:|---|
| 0–29 | LOW |
| 30–59 | MEDIUM |
| 60–79 | HIGH |
| 80–100 | CRITICAL |

This makes the core risk signal reproducible and explainable.

---

## 6. AI Safety

The LLM is used as an **analysis assistant**, not as an autonomous decision-maker.

AI-generated analysis should be evaluated against the available evidence.

The intended flow is:

```text
Evidence
   ↓
Structured Security Context
   ↓
LLM Analysis
   ↓
Analyst Review
```

The system should not treat unsupported AI-generated claims as confirmed security facts.

---

## 7. Hallucination Safeguards

SOC-Aid includes safeguards intended to reduce unsupported AI reasoning.

The analysis should not invent:

- Security events
- User activity
- Authentication results
- Network activity
- Malware behavior
- Incident details
- Evidence that was not provided

If information is unavailable, it should remain unknown.

### Analyst Verification Rule

For an important AI-generated statement, ask:

> **What evidence supports this statement?**

If the evidence cannot be identified, the statement should be treated as uncertain and investigated before being used for a security decision.

---

## 8. Input Validation

SOC-Aid validates incoming security-alert data before processing.

The system checks for:

- Required fields
- Valid severity values
- Valid alert structure

Invalid input should produce an explicit validation failure rather than a misleading security result.

Example:

```text id="kwk2z7"
Invalid Alert
     ↓
Validation Failure
     ↓
Graceful Error Handling
```

---

## 9. Secrets and API Keys

API credentials must not be hard-coded into source files.

The working prototype uses a secure secret mechanism in Google Colab.

The expected secret name is:

```text id="j38q0c"
GROQ_API_KEY
```

### Never Commit Secrets

The following must never be committed to the repository:

- API keys
- Passwords
- Access tokens
- Private credentials
- `.env` files containing secrets
- Cloud credentials
- Private certificates

The repository's `.gitignore` is configured to exclude common secret and credential files.

---

## 10. GitHub Security

The project source code is maintained in a GitHub repository.

When working with GitHub authentication:

- Use a Personal Access Token when required.
- Never place a token inside source code.
- Never publish tokens in documentation.
- Never send tokens through chat.
- Revoke tokens that are no longer required.
- Use the minimum permissions necessary.

### Token Safety

If a token is ever accidentally exposed:

1. Revoke it immediately.
2. Create a new token if required.
3. Check repository history for exposure.
4. Remove the exposed credential from affected files.
5. Avoid reusing the compromised token.

---

## 11. Repository Protection

The repository should not contain runtime-generated or environment-specific files.

Examples include:

```text id="h8a5c0"
.config/
.pytest_cache/
.gradio/
__pycache__/
.ipynb_checkpoints/
.env
*.key
*.pem
credentials.json
secrets.json
```

These files may contain environment information, temporary data, credentials, or generated runtime artifacts.

---

## 12. Dependency Security

Project dependencies are explicitly defined in:

```text id="x7hl0d"
requirements.txt
```

Current pinned versions include:

```text id="3b6f4a"
langgraph==1.2.11
langchain==1.3.15
langchain-core==1.5.5
gradio==6.24.0
pydantic==2.13.4
pytest==8.4.2
```

Dependencies should be reviewed and updated carefully rather than changed without testing.

---

## 13. Security Testing

Security-related behavior is included in the project verification process.

The final automated test suite reported:

```text id="b5s4x9"
7 passed in 0.02s
```

The final verification also confirmed:

```text id="0l3wz4"
✓ Authentication evidence integrated
✓ Timestamps preserved
✓ Risk assessment verified
✓ Human oversight preserved
```

Additional safety checks cover:

- Invalid input handling
- Graceful failure
- Evidence safety
- Hallucination safeguards
- Human analyst review

---

## 14. Data Handling Considerations

SOC-Aid should be tested with appropriate security-alert data.

When using real organizational data, analysts should follow their organization's:

- Data-classification policies
- Privacy requirements
- Security policies
- Logging requirements
- Access-control policies

Sensitive production data should not be placed into a public repository or demonstration environment unless explicitly authorized.

---

## 15. Safe Demonstration Practices

For demonstrations, use sanitized or synthetic security-alert data whenever possible.

Avoid exposing:

- Real user credentials
- Passwords
- API keys
- Internal IP information when sensitive
- Private hostnames
- Confidential incident details
- Personally identifiable information

A demo should demonstrate the **workflow and reasoning process**, not expose real secrets or sensitive organizational data.

---

## 16. Responsible Use

SOC-Aid is an AI-assisted triage prototype.

It should be used to:

- Support alert investigation
- Organize evidence
- Prioritize analyst attention
- Explain risk signals
- Suggest investigation steps

It should not be used as an unsupervised mechanism for:

- Autonomous incident response
- Automatic account termination
- Automatic infrastructure blocking
- Irreversible production actions

---

## 17. Security Boundaries

The current MVP intentionally maintains the following boundaries:

| Security Boundary | Status |
|---|---|
| Alert validation | ✅ Enabled |
| Evidence-aware analysis | ✅ Enabled |
| Explainable risk assessment | ✅ Enabled |
| Human review | ✅ Required |
| Autonomous blocking | 🚫 Disabled |
| Automatic destructive actions | 🚫 Disabled |

These boundaries are part of the project's safety design.

---

## 18. Reporting a Security Issue

If a security issue is discovered in the project, avoid publicly posting sensitive details before the issue can be responsibly reviewed.

When reporting an issue, provide:

- A clear description
- Affected component
- Reproduction steps where appropriate
- Expected behavior
- Actual behavior
- Potential security impact

Do not include secrets, credentials, or private security data in an issue report.

---

## 19. Security Principle

> 🛡️ **SOC-Aid provides evidence and analysis to support a human security decision. It does not make irreversible security decisions autonomously.**

This principle is central to the architecture and safety model of the SOC-Aid MVP.
