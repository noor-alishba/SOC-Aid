# 🔎 SOC-Aid — Problem Research & Motivation

> Understanding the security-alert triage problem that motivated the SOC-Aid MVP.

## 1. Problem Overview

Security Operations Centers (SOCs) continuously receive security alerts from different security-monitoring sources.

A single alert may provide only a limited view of an event. Analysts often need to examine additional activity, correlate related alerts, evaluate severity, and determine what should be investigated next.

This creates a challenging triage workflow:

```text
Security Alerts
      ↓
Alert Review
      ↓
Related Activity
      ↓
Evidence Collection
      ↓
Risk Assessment
      ↓
Investigation
      ↓
Human Security Decision
```

SOC-Aid was developed to assist with this initial triage process.

---

## 2. SOC Analyst Challenge

The primary challenge addressed by SOC-Aid is the difficulty of turning individual security alerts into a structured, evidence-aware triage result.

An analyst may need to answer questions such as:

- 🔎 What exactly happened?
- 👤 Which user or entity is involved?
- 🌐 Where did the activity originate?
- 🔗 Are there related alerts?
- 🔐 Is there supporting authentication evidence?
- 📊 How serious is the activity?
- 🤖 What does the available evidence suggest?
- 💡 What should be investigated next?

The challenge becomes greater when multiple related events must be considered together.

---

## 3. Alert Context Matters

A single alert does not always provide enough context to determine the significance of an event.

For example:

```text
Failed Login
```

by itself may not provide enough information to determine whether the activity is normal or suspicious.

Additional context can change the interpretation:

```text
Multiple Failed Logins
        +
Same User / Related Context
        +
Successful Login
        ↓
Suspicious Authentication Pattern
```

This demonstrates why alert correlation is an important part of the triage process.

---

## 4. Alert Correlation Problem

Related alerts can provide evidence that is not visible when each alert is considered independently.

SOC-Aid therefore includes an alert-correlation stage.

The workflow can use available context such as:

- User identity
- Source IP
- Event type
- Related authentication activity

The goal is to create a broader security context around the alert being investigated.

---

## 5. Risk Prioritization

Not every security alert requires the same level of urgency.

A SOC analyst needs a structured way to prioritize alerts.

SOC-Aid includes a deterministic risk-assessment layer based on:

- Alert severity
- Related alerts
- Authentication activity
- Additional contextual evidence

The base severity scores are:

| Severity | Score |
|---|---:|
| LOW | 10 |
| MEDIUM | 30 |
| HIGH | 60 |
| CRITICAL | 90 |

The score can be increased by relevant contextual evidence and is capped at **100**.

Risk levels are:

| Score | Risk Level |
|---:|---|
| 0–29 | LOW |
| 30–59 | MEDIUM |
| 60–79 | HIGH |
| 80–100 | CRITICAL |

This provides a consistent starting point for triage prioritization.

---

## 6. Evidence Before Inference

A major design principle of SOC-Aid is:

> 🛡️ **Evidence before inference.**

Security analysis should distinguish between what is directly observed and what is inferred from that evidence.

SOC-Aid therefore uses the following distinction:

### FACT

Information directly supported by available security evidence.

### INFERENCE

A reasonable interpretation derived from available evidence.

### UNKNOWN

Information that cannot be established from the available evidence.

This distinction is particularly important when using AI in security operations.

---

## 7. AI-Assisted Analysis

Large Language Models can help analysts interpret security information and summarize complex activity.

However, AI-generated analysis can introduce a risk of unsupported or fabricated information.

SOC-Aid therefore uses the LLM as an **analysis assistant** rather than an autonomous security decision-maker.

The intended workflow is:

```text
Available Evidence
       ↓
Structured Security Context
       ↓
LLM Analysis
       ↓
Investigation Recommendation
       ↓
Human SOC Analyst
```

The AI analysis is intended to support the analyst's investigation rather than replace human judgment.

---

## 8. Hallucination Risk

One important concern with AI-assisted security analysis is hallucination.

An AI system may produce a plausible statement that is not actually supported by the available alert evidence.

For example, an unsupported statement might claim that:

```text
A user's credentials were definitely compromised.
```

when the available evidence only shows repeated failed-login activity followed by a successful login.

The available evidence may support:

```text
Suspicious authentication activity was observed.
```

but may not establish:

```text
The credentials were definitely compromised.
```

SOC-Aid addresses this distinction through evidence-aware reasoning and the fact / inference / unknown model.

---

## 9. Human Oversight

Security decisions can have significant operational consequences.

For this reason, SOC-Aid intentionally preserves human oversight.

The system does not autonomously:

- Block IP addresses
- Disable accounts
- Isolate endpoints
- Delete resources
- Execute irreversible actions

Instead, the workflow ends with:

```text
Evidence
   +
Risk Assessment
   +
AI Analysis
   +
Recommendation
        ↓
👤 Human SOC Analyst
        ↓
Final Security Decision
```

---

## 10. Proposed Solution

SOC-Aid addresses the identified triage challenges through a structured agentic workflow.

```text
Security Alert
      ↓
Alert Parsing
      ↓
Alert Correlation
      ↓
Risk Assessment
      ↓
Evidence-Aware LLM Analysis
      ↓
Investigation Recommendation
      ↓
Human SOC Analyst
```

Each stage has a specific responsibility.

### 1. Alert Parsing

Validates and normalizes incoming alert information.

### 2. Alert Correlation

Finds relevant related activity.

### 3. Risk Assessment

Produces an explainable deterministic risk signal.

### 4. Evidence-Aware LLM Analysis

Interprets the available security context while distinguishing facts, inferences, and unknowns.

### 5. Investigation Recommendation

Suggests useful next steps for the analyst.

### 6. Human Review

Keeps the final security decision under human control.

---

## 11. Why an Agentic Workflow?

SOC-Aid is structured as a multi-stage workflow rather than treating the LLM as the entire security system.

This separation provides:

- 🔎 Clear processing stages
- 📊 Deterministic risk assessment
- 🔗 Explicit alert correlation
- 🧾 Structured evidence
- 🤖 Focused AI analysis
- 👤 Human oversight

The LLM therefore operates within a defined security-analysis workflow instead of independently deciding what should happen to an alert.

---

## 12. Example Problem Scenario

Consider the following authentication sequence:

```text
10:20:00  Failed Login
10:20:xx  Failed Login
10:20:xx  Failed Login
...
10:28:10  Failed Login
10:xx:xx  Successful Login
```

The individual failed-login alerts may appear routine when viewed independently.

When correlated, however, they provide a stronger security context.

The final evidence verification for the project demonstrated:

```text
Failed Logins : 50
First Failure : 2026-08-19 10:20:00
Last Failure  : 2026-08-19 10:28:10
Time Window   : 8.17 minutes
Pattern       : True
```

This evidence can contribute to a higher-priority risk assessment.

---

## 13. Research-to-Implementation Connection

The problem research directly influenced the SOC-Aid architecture.

| Identified Problem | SOC-Aid Response |
|---|---|
| Individual alerts lack context | Alert correlation |
| Analysts need prioritization | Risk assessment |
| AI can make unsupported claims | Evidence-aware analysis |
| Security conclusions need justification | Fact / inference / unknown |
| Invalid data can produce unreliable results | Input validation |
| AI decisions can be risky | Human oversight |
| Analysts need actionable next steps | Investigation recommendations |

This connection keeps the implementation aligned with the original problem.

---

## 14. MVP Scope

The current MVP focuses on the initial alert-triage workflow.

### Included

- ✅ Security alert parsing
- ✅ Related-alert correlation
- ✅ Rule-based risk assessment
- ✅ Evidence integration
- ✅ LLM-powered analysis
- ✅ Fact / inference / unknown distinction
- ✅ Hallucination safeguards
- ✅ Investigation recommendations
- ✅ Error handling
- ✅ Structured triage reports
- ✅ Human analyst oversight

### Not Included

The current MVP does not provide autonomous production response actions such as:

- ❌ Automatic IP blocking
- ❌ Automatic account disabling
- ❌ Automatic endpoint isolation
- ❌ Irreversible production actions

---

## 15. Testing and Validation

The implemented MVP was tested through both automated tests and explicit evidence verification.

The final automated test result was:

```text
7 passed in 0.02s
```

The final evidence verification confirmed:

```text
✓ Authentication evidence integrated
✓ Timestamps preserved
✓ Risk assessment verified
✓ Human oversight preserved
```

These results provide evidence that the implemented MVP workflow satisfies its current testing objectives.

---

## 16. Expected Benefits

The intended benefits of SOC-Aid include:

### ⏱️ Faster Initial Triage

Structured processing can help analysts understand an alert more quickly.

### 🔗 Better Context

Related activity can be considered together rather than in isolation.

### 📊 Explainable Prioritization

The deterministic risk layer provides a reproducible risk signal.

### 🤖 AI Assistance

The LLM can help summarize and interpret available evidence.

### 🛡️ Safer AI Usage

Fact / inference / unknown distinctions help reduce unsupported conclusions.

### 👤 Human Control

Analysts remain responsible for final security decisions.

---

## 17. Limitations

The current MVP has important limitations.

### Prototype Scope

The system is an MVP and has not been presented as a complete production SOC platform.

### Limited Alert Types

The current workflow focuses on the alert structures and scenarios implemented in the project.

### Evidence Dependency

AI analysis quality depends on the quality and completeness of the available alert evidence.

### Human Review Required

The system does not replace a trained security analyst.

### Demo Environment

The working interface is demonstrated through Google Colab and a runtime-generated Gradio endpoint rather than a permanent production deployment.

---

## 18. Future Research Directions

Potential future work includes:

- 🔗 More advanced alert correlation
- 📚 Larger security-event datasets
- 🧠 More sophisticated evidence reasoning
- 📊 Expanded risk models
- 🔌 Integration with real SOC data sources
- 📈 Analyst feedback loops
- 🔐 Stronger production security controls
- 🧪 Larger-scale evaluation
- 👥 Multi-analyst workflow support

These directions are documented further in the project's roadmap.

---

## 19. Core Research Principle

The central idea behind SOC-Aid is:

> **Security AI should help analysts understand evidence, not make unsupported security decisions.**

The project therefore combines deterministic security logic, evidence-aware AI analysis, structured reporting, and human oversight into a single alert-triage workflow.

---

## 20. Conclusion

SOC-Aid addresses the challenge of security-alert triage by combining:

```text
Alert Parsing
      +
Alert Correlation
      +
Risk Assessment
      +
Evidence-Aware AI
      +
Investigation Recommendations
      +
Human Oversight
```

The resulting MVP provides a structured approach to turning security alerts into explainable triage information while maintaining a clear boundary between **AI assistance** and **human security decision-making**.

> 🛡️ **SOC-Aid: Evidence-aware AI assistance for security alert triage.**
