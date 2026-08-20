# SOC-Aid

> Evidence-aware Agentic AI for Security Alert Triage

SOC-Aid is an AI-assisted Security Operations Center (SOC) alert-triage agent that helps analysts understand security alerts, correlate related activity, assess risk, and identify recommended investigation steps.

## Features

- Security alert parsing
- Related-alert correlation
- Rule-based risk assessment
- LLM-powered analysis
- Evidence-aware reasoning
- Fact / inference / unknown distinction
- Hallucination safeguards
- Human analyst recommendations
- Error handling
- Professional triage reports

## How It Works

Security Alert
→ Alert Parsing
→ Alert Correlation
→ Risk Assessment
→ Evidence-Aware LLM Analysis
→ Investigation Recommendation
→ Human SOC Analyst

## Current Status

SOC-Aid MVP is implemented and tested in Google Colab.

Human analyst review is required for security decisions.
Autonomous blocking is disabled.

## Usage

The current implementation is provided as a Google Colab notebook.

The system requires a Groq API key stored securely in Google Colab Secrets.

Expected secret name:

`GROQ_API_KEY`
