# Architecture

## System Overview

SOC-Aid uses a LangGraph-based workflow to process security alerts through multiple stages.

```text
Security Alert
      |
      v
Alert Parser
      |
      v
Alert Correlation
      |
      v
Risk Assessment
      |
      v
Evidence-Aware LLM Analysis
      |
      v
Recommendation
      |
      v
Human SOC Analyst
```

## Main Components

1. Alert Parser
2. Alert Correlation
3. Rule-Based Risk Assessment
4. Evidence-Aware LLM Analysis
5. Recommendation Engine
6. Human Oversight
