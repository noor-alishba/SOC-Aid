# 📋 SOC-Aid — Changelog

All notable changes to the SOC-Aid project are documented in this file.

The project follows a release-oriented changelog format so that major improvements, fixes, testing updates, and architectural changes can be tracked over time.

---

## [Unreleased]

### 🔮 Planned

Future development may include:

- Expanded security-alert correlation
- Additional alert types
- Larger test datasets
- Improved evidence attribution
- Enhanced analyst experience
- Additional security-data integrations
- Stronger production-readiness controls
- Expanded evaluation of AI-assisted analysis

These items are part of the project's development roadmap and are not necessarily implemented in the current MVP.

---

# [0.1.0] — Initial SOC-Aid MVP

### 🎉 Added

The initial SOC-Aid MVP introduced a structured security-alert triage workflow.

#### Alert Processing

- Added security-alert parsing
- Added required-field validation
- Added severity validation
- Added normalized alert processing
- Added invalid-input handling

#### Alert Correlation

- Added related-alert discovery
- Added user-based correlation
- Added source-IP correlation
- Added contextual alert analysis

#### Risk Assessment

- Added deterministic risk scoring
- Added severity-based scoring
- Added contextual risk adjustments
- Added risk-score capping at 100
- Added LOW / MEDIUM / HIGH / CRITICAL risk levels
- Added explainable risk reasons

#### AI-Assisted Analysis

- Added LLM-powered security analysis
- Added evidence-aware analysis
- Added fact / inference / unknown distinction
- Added hallucination safeguards
- Added structured security interpretation

#### Investigation Support

- Added investigation recommendations
- Added analyst-oriented triage output
- Added structured SOC-Aid triage reports

#### Safety

- Added human-in-the-loop review
- Disabled autonomous blocking
- Disabled destructive autonomous actions
- Added graceful handling of invalid input
- Added evidence-safety checks

#### Testing

- Added automated SOC-Aid test suite
- Added suspicious-login test coverage
- Added normal-login test coverage
- Added critical-malware test coverage
- Added invalid-alert validation
- Added evidence verification
- Added authentication-pattern verification
- Added timestamp verification
- Added risk-assessment verification
- Added human-oversight verification

Final automated verification reported:

```text
7 passed in 0.02s
```

Additional evidence verification confirmed:

```text
✓ Authentication evidence integrated
✓ Timestamps preserved
✓ Risk assessment verified
✓ Human oversight preserved
```

---

## Documentation

The initial MVP documentation set includes:

- `README.md`
- `PROBLEM_RESEARCH.md`
- `ARCHITECTURE.md`
- `INSTALLATION.md`
- `USAGE.md`
- `TESTING.md`
- `ANALYST_GUIDE.md`
- `SECURITY.md`
- `ROADMAP.md`
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `CHANGELOG.md`

The documentation covers project motivation, architecture, setup, usage, testing, analyst workflow, security considerations, development plans, and contribution guidance.

---

## Repository Structure

The MVP introduced the following primary implementation structure:

```text
SOC-Aid/
│
├── src/
│   └── soc_aid/
│       ├── __init__.py
│       ├── agent.py
│       ├── models.py
│       ├── report.py
│       └── tools.py
│
├── tests/
│   └── test_soc_aid.py
│
├── Documentation
│
└── requirements.txt
```

---

# Release Philosophy

SOC-Aid development follows several principles when introducing new functionality.

### 🛡️ Safety First

New capabilities should not bypass appropriate security controls or human oversight.

### 🔎 Evidence First

Important security conclusions should remain connected to available evidence.

### 📊 Explainability

Risk and triage decisions should remain understandable and testable.

### 🤖 Controlled AI

AI should assist analysts rather than independently control security infrastructure.

### 🧪 Test Before Expansion

New functionality should be validated before being treated as a stable project capability.

---

# Versioning

SOC-Aid uses semantic-style versioning:

```text
MAJOR.MINOR.PATCH
```

For example:

```text
0.1.0
```

represents an initial MVP release.

Future releases may use:

```text
0.2.0
0.3.0
1.0.0
```

depending on the scope and maturity of changes.

---

# Change Categories

Future changelog entries may use the following categories:

- `Added` — New functionality
- `Changed` — Changes to existing functionality
- `Fixed` — Bug fixes
- `Security` — Security-related improvements
- `Testing` — Test and validation improvements
- `Documentation` — Documentation changes
- `Deprecated` — Features planned for removal
- `Removed` — Removed functionality

---

# Current Release Summary

| Version | Status | Description |
|---|---|---|
| `0.1.0` | 🟢 Released | Initial SOC-Aid MVP |
| `Unreleased` | 🔮 Planned | Future improvements |

---

> 🚀 **SOC-Aid 0.1.0 establishes the foundation for evidence-aware, explainable, human-supervised security alert triage.**
