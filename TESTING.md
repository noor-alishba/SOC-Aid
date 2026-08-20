# Testing

SOC-Aid was tested using suspicious, normal, critical, invalid-input,
evidence-safety, and human-oversight scenarios.

## Test Results

| Test | Expected Result | Status |
|---|---|---|
| Suspicious Login | High/Critical risk and investigation recommendation | PASS |
| Normal Login | Low/appropriate risk | PASS |
| Critical Malware | Critical risk and human investigation | PASS |
| Invalid Input | Clear error without crashing | PASS |
| Evidence Safety | Facts, inferences, and unknowns separated | PASS |
| Human Oversight | Human review required | PASS |

## Evidence Safety

The LLM is instructed to use only the evidence provided by the alert
and related alerts.

The system also checks for unsupported claims and requires uncertainty
to be identified when evidence is insufficient.

## Known Limitations

The current MVP uses a small sample dataset and rule-based correlation.
It does not connect directly to a production SIEM or live threat-intelligence
infrastructure.

LLM output remains subject to human review.
