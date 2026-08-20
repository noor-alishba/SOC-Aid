# SOC-Aid Analyst Guide

> Evidence-aware AI assistant for Security Alert Triage

## 1. Purpose

SOC-Aid is an AI-assisted security alert triage system.
It helps a SOC analyst understand security alerts, identify
related activity, assess risk, organize evidence, and
recommend investigation steps.

SOC-Aid does NOT replace the human SOC analyst.
The final security decision always remains with the human analyst.

## 2. Analyst Workflow

Security Alert
    |
    v
Alert Parsing
    |
    v
Alert Correlation
    |
    v
Risk Assessment
    |
    v
Evidence-Aware AI Analysis
    |
    v
Investigation Recommendation
    |
    v
Human SOC Analyst

## 3. Alert Input

A security alert contains:

- Alert ID
- Timestamp
- User
- Source IP
- Event type
- Message
- Severity

## 4. Alert Parsing

SOC-Aid validates the required alert fields before analysis.

Required fields:

- alert_id
- timestamp
- user
- source_ip
- event_type
- message
- severity

Invalid or incomplete alerts are rejected with an error.

## 5. Alert Correlation

The current MVP searches for related alerts using:

- Same user
- Same source IP

Example pattern:

Failed login
Failed login
Failed login
Successful login

If the events involve the same user or source IP, SOC-Aid
can identify them as related activity.

## 6. Suspicious Authentication Pattern

An important pattern in the current MVP is:

Failed Login + Successful Login + Same User or Source IP

This pattern can increase the rule-based risk assessment.

However, this pattern alone does NOT prove:

- Credential compromise
- Attacker identity
- Malicious IP ownership
- Unauthorized access
- Data exfiltration

Additional evidence is required to establish those facts.

## 7. Risk Assessment

Current severity base scores:

| Severity | Base Score |
|---|---:|
| LOW | 10 |
| MEDIUM | 30 |
| HIGH | 60 |
| CRITICAL | 90 |

Risk levels:

| Score | Priority |
|---|---|
| 0-29 | LOW |
| 30-59 | MEDIUM |
| 60-79 | HIGH |
| 80-100 | CRITICAL |

The final risk score is capped at 100.

## 8. Priority Meaning

### LOW

Limited evidence of suspicious activity.

Recommended action: monitor the activity and investigate
if additional suspicious evidence appears.

### MEDIUM

Some related or potentially unusual activity exists.

Recommended action: review related events and verify
whether the activity was expected.

### HIGH

The available evidence indicates elevated risk.

Recommended action: prioritize human investigation.

### CRITICAL

The available evidence produces a very high risk assessment.

Recommended action: escalate immediately for human SOC
analyst investigation.

## 9. Evidence-Aware AI Analysis

The LLM receives:

- Current alert
- Related alerts
- Rule-based risk assessment

The LLM is instructed to use only the provided evidence.

### FACT

Information directly present in the evidence.

Example: A successful login is recorded in the alert.

### INFERENCE

A reasonable interpretation that is not directly proven.

Example: The sequence may warrant additional investigation.

### UNKNOWN

Information that cannot be established from the available evidence.

Example: Whether credentials were compromised cannot be
determined from the available evidence.

## 10. Unsupported Claims

SOC-Aid should not claim without evidence that:

- An IP belongs to an attacker
- Credentials were compromised
- Malware spread
- Lateral movement occurred
- Data exfiltration occurred
- MFA was bypassed
- Privilege escalation occurred

## 11. Recommended Investigation

SOC-Aid may recommend that the analyst:

- Review related authentication events
- Verify whether the login was expected
- Review activity after the login
- Check internal network records
- Examine alerts from the same timeframe
- Verify available authentication controls

These are investigation suggestions, not confirmed facts.

## 12. Human Oversight

SOC-Aid does not automatically:

- Block an IP
- Disable an account
- Delete files
- Terminate systems
- Perform destructive security actions

The system provides an assessment and recommendation.
The human SOC analyst makes the final decision.

## 13. Analyst Decision

After reviewing the SOC-Aid report, the analyst may:

- Investigate further
- Request additional evidence
- Escalate the alert
- Close the alert as benign

SOC-Aid does not make this final decision automatically.

## 14. Current MVP Limitations

The current MVP uses a small sample alert dataset.

It does not yet directly connect to:

- Production SIEM
- Live threat intelligence
- WHOIS services
- Production endpoint security systems
- Persistent incident databases

## 15. Safety Principle

No automated blocking.
No unsupported claims.
No invented evidence.
Human analyst remains in control.