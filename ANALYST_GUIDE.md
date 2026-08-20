# 🧑‍💻 SOC-Aid Analyst Guide

> Practical guide for reviewing security-alert triage results produced by SOC-Aid.

## 1. Purpose

SOC-Aid is designed to assist Security Operations Center (SOC) analysts during the initial triage of security alerts.

It helps organize:

- 🔎 Alert information
- 🔗 Related activity
- 🔐 Authentication evidence
- 📊 Risk assessment
- 🤖 Evidence-aware AI analysis
- 💡 Investigation recommendations

SOC-Aid is an **analyst-assistance system**, not an autonomous security-response system.

---

## 2. SOC-Aid Triage Flow

When an alert is submitted, SOC-Aid processes it through the following workflow:

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

The analyst should review the final result together with the evidence that produced it.

---

## 3. Reading a Triage Result

A SOC-Aid triage result can contain the following major sections:

```text
Alert
Parsed Alert
Related Alerts
Authentication Evidence
Risk Assessment
AI Analysis
Recommendation
Decision
```

Each section answers a different question.

### 🔎 Alert

**What happened?**

Review the original alert details, including information such as:

- Alert ID
- Timestamp
- User
- Source IP
- Event type
- Severity
- Message

---

### 🔍 Parsed Alert

**Did SOC-Aid successfully understand the alert?**

The parsed alert represents the normalized form used by downstream workflow stages.

If required fields are missing or invalid, the alert should be handled as an error rather than treated as reliable input.

---

### 🔗 Related Alerts

**What other activity is connected to this alert?**

Review correlated events carefully.

Correlation can provide important context such as repeated authentication attempts from the same user or source IP.

For example:

```text
50 Failed Logins
       ↓
Successful Login
       ↓
Authentication Pattern
       ↓
Higher Risk
```

The analyst should confirm that the correlated events actually belong to the same activity context.

---

## 4. Authentication Evidence

Authentication evidence is particularly important when investigating suspicious login activity.

SOC-Aid can preserve:

- Failed-login count
- First failed-login timestamp
- Last failed-login timestamp
- Time-window calculation
- Pattern detection

### Verified Example

The final SOC-Aid verification produced:

```text
Failed Logins : 50
First Failure : 2026-08-19 10:20:00
Last Failure  : 2026-08-19 10:28:10
Time Window   : 8.17 minutes
Pattern       : True
```

This means the workflow successfully preserved evidence from the correlated failed-login events.

### Analyst Check

Do not rely only on the number.

Verify:

1. The failed-login events are actually related.
2. The user/context matches.
3. The source IP/context is consistent where applicable.
4. The first timestamp is the earliest relevant event.
5. The last timestamp is the latest relevant event.
6. The calculated time window is consistent with those timestamps.

---

## 5. Understanding Risk Assessment

SOC-Aid uses a deterministic risk-assessment layer.

Base severity scores are:

| Severity | Base Score |
|---|---:|
| LOW | 10 |
| MEDIUM | 30 |
| HIGH | 60 |
| CRITICAL | 90 |

Additional contextual evidence can increase the score.

The score is capped at:

```text
100
```

Risk levels are interpreted as:

| Score | Risk |
|---:|---|
| 0–29 | LOW |
| 30–59 | MEDIUM |
| 60–79 | HIGH |
| 80–100 | CRITICAL |

### Example

A suspicious authentication pattern with extensive correlated failed-login activity can produce:

```text
Risk Level : CRITICAL
Risk Score : 100
```

The analyst should still review the underlying evidence rather than treating the score as an unquestionable conclusion.

---

## 6. Understanding AI Analysis

🤖 The AI analysis is intended to **assist interpretation** of the evidence.

The analyst should distinguish between:

### FACT

Information directly supported by the alert or correlated evidence.

Example:

```text
50 failed-login events were correlated.
```

### INFERENCE

A reasonable interpretation based on available evidence.

Example:

```text
The authentication activity may indicate a suspicious login pattern.
```

### UNKNOWN

Information that cannot be established from the available evidence.

Example:

```text
The available alerts do not establish whether the user's password was compromised.
```

This distinction helps prevent unsupported assumptions.

---

## 7. Evidence-Aware Analysis

SOC-Aid is designed around the principle:

> **Evidence before inference.**

The AI should base its analysis on the information available in the workflow state.

An analyst should be cautious if an AI statement cannot be connected to:

- The original alert
- Related alerts
- Authentication evidence
- Risk assessment
- Other available workflow evidence

If something is not supported by the available evidence, it should not be treated as an established fact.

---

## 8. Hallucination Safeguards

SOC-Aid includes evidence-safety checks intended to reduce unsupported AI claims.

The system is designed to avoid presenting unavailable information as confirmed information.

### Analyst Rule

If the AI says something important, ask:

> **“What evidence in the alert or correlated activity supports this statement?”**

If the evidence cannot be identified, treat the statement as uncertain and investigate further.

---

## 9. Investigation Recommendation

The recommendation section tells the analyst what should be investigated next.

For a high-risk authentication pattern, a recommendation may include:

- 👤 Review the affected account
- 💻 Review the affected endpoint
- 🔐 Review authentication logs
- 🔎 Investigate related activity
- 🚨 Escalate for human investigation

Recommendations are **investigation guidance**, not automatic response commands.

---

## 10. Human Decision

The final decision remains with the SOC analyst.

SOC-Aid explicitly preserves human oversight:

```text
Human SOC analyst approval required.
```

### 🚫 No Autonomous Blocking

SOC-Aid does not automatically:

- Disable accounts
- Block IP addresses
- Isolate endpoints
- Delete resources
- Execute irreversible security actions

The system provides evidence and recommendations so that a qualified analyst can make the final decision.

---

## 11. Invalid Alerts

SOC-Aid also handles invalid or incomplete alert input.

Examples of problems include:

- Missing required fields
- Unsupported severity
- Malformed alert structure

The system should fail gracefully rather than silently producing a misleading triage result.

---

## 12. Testing Evidence

The project was tested against core functionality and reliability scenarios.

The automated test suite reported:

```text
7 passed in 0.02s
```

The final evidence verification also confirmed:

```text
✓ Authentication evidence integrated
✓ Timestamps preserved
✓ Risk assessment verified
✓ Human oversight preserved
```

These checks provide evidence that the core MVP workflow is functioning as intended.

---

## 13. Recommended Analyst Workflow

When reviewing a SOC-Aid result, use this sequence:

### Step 1 — Understand the Alert

Read the original alert and identify:

- What happened?
- Who was affected?
- When did it happen?
- Where did it originate?
- What event type was reported?

### Step 2 — Review Correlation

Check whether related alerts provide additional context.

### Step 3 — Verify Evidence

For authentication events, check the:

- Count
- First timestamp
- Last timestamp
- Time window
- Pattern

### Step 4 — Review Risk

Understand why the alert received its risk score.

### Step 5 — Evaluate AI Analysis

Separate facts from inferences and unknown information.

### Step 6 — Follow Investigation Recommendations

Use the recommendation as a starting point for further investigation.

### Step 7 — Make the Human Decision

The SOC analyst determines the appropriate response.

---

## 14. Example: Suspicious Authentication Pattern

Consider a successful login preceded by a large number of failed-login attempts.

SOC-Aid may identify:

```text
Failed Logins : 50
Time Window   : 8.17 minutes
Pattern       : True
Risk Level    : CRITICAL
Risk Score    : 100
```

An appropriate analyst workflow would be:

```text
Repeated failures
      ↓
Verify correlation
      ↓
Confirm timestamps
      ↓
Review successful login
      ↓
Review account activity
      ↓
Review endpoint/authentication logs
      ↓
Determine whether escalation is required
```

The result should support investigation rather than automatically triggering a destructive response.

---

## 15. Analyst Safety Checklist

Before making a security decision, confirm:

- [ ] The original alert is valid.
- [ ] Required alert fields are present.
- [ ] Related alerts are actually relevant.
- [ ] Authentication evidence is preserved.
- [ ] Timestamps are consistent.
- [ ] Risk level is understood.
- [ ] AI statements are supported by evidence.
- [ ] Unknown information is not treated as fact.
- [ ] Recommended investigation steps have been considered.
- [ ] A human SOC analyst makes the final security decision.

---

## 16. Key Principle

> 🛡️ **SOC-Aid assists the analyst; it does not replace the analyst.**

The purpose of the system is to make security-alert triage more structured, explainable, evidence-aware, and efficient while preserving human oversight over security decisions.
