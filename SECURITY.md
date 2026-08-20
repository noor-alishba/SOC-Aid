# Security Policy

## Security Considerations

SOC-Aid is a cybersecurity analysis prototype designed for defensive
security alert triage.

## API Key Security

API keys must never be committed to the repository.

The current implementation retrieves the Groq API key from
Google Colab Secrets.

Expected secret:

`GROQ_API_KEY`

## Human Oversight

SOC-Aid does not automatically block IP addresses, disable accounts,
delete files, or perform destructive security actions.

Human analyst review is required before security actions are taken.

## Evidence Safety

The LLM is instructed to:

- Use only provided evidence.
- Distinguish facts from inferences.
- Identify unknown information.
- Avoid unsupported claims.
- Avoid claiming an IP is malicious without evidence.
- Avoid claiming credential compromise without evidence.

## Reporting a Security Issue

Do not publicly expose API keys, passwords, credentials, private logs,
or other sensitive information.

Security issues should be reported privately to the project maintainers.
