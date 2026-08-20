# Usage

## Overview

SOC-Aid accepts a security alert and processes it through:

1. Alert parsing
2. Alert correlation
3. Risk assessment
4. Evidence-aware LLM analysis
5. Human investigation recommendation

## Running the Agent

The current MVP is demonstrated through Google Colab.

Run the notebook cells sequentially.

The system requires a Groq API key stored securely in Google Colab Secrets.

Expected secret name:

`GROQ_API_KEY`

## Example

```python
result = run_soc_aid(alert)
```

A custom alert can also be passed to the agent for analysis.
