# 🤝 Contributing to SOC-Aid

Thank you for your interest in contributing to **SOC-Aid**.

SOC-Aid is an evidence-aware, AI-assisted security-alert triage project focused on explainability, safe AI usage, and human analyst oversight.

Contributions are welcome, especially those that improve reliability, testing, documentation, security, and analyst usability.

---

## 📌 Before You Contribute

Before making changes, please:

1. Read the `README.md`
2. Review `ARCHITECTURE.md`
3. Review `SECURITY.md`
4. Check the existing `ROADMAP.md`
5. Understand the project's human-in-the-loop design
6. Make sure your proposed change fits the project's goals

---

# 🛠️ Development Setup

SOC-Aid is currently developed and demonstrated using Python-based tooling.

Install the project dependencies with:

```bash
pip install -r requirements.txt
```

For development and testing, make sure the required Python environment is available before running the test suite.

---

# 🌿 Branching

Create a separate branch for your work instead of making changes directly on `main`.

Example:

```bash
git checkout -b feature/improve-alert-correlation
```

Suggested branch prefixes include:

```text
feature/     New functionality
fix/         Bug fixes
docs/        Documentation changes
test/        Testing improvements
security/    Security-related changes
refactor/    Code restructuring
```

Examples:

```text
feature/add-alert-type
fix/risk-score-edge-case
docs/update-analyst-guide
test/add-correlation-tests
security/improve-input-validation
```

---

# ✏️ Making Changes

When making a change:

### 1. Keep the change focused

Avoid combining unrelated changes in one pull request.

For example:

```text
Good:
Improve authentication-alert correlation

Avoid:
Improve correlation + redesign UI + rewrite documentation
```

unless those changes are directly related.

### 2. Preserve existing behavior

Do not unintentionally break existing functionality.

### 3. Keep security in mind

Security-related functionality should be designed conservatively.

### 4. Prefer explainable logic

Changes to risk assessment or alert processing should remain understandable and testable.

---

# 🧪 Testing

Before submitting a contribution, run the test suite.

```bash
pytest -q
```

All existing tests should pass before opening a pull request.

If you add new functionality, add appropriate tests whenever practical.

### Testing should cover

- Normal inputs
- Invalid inputs
- Edge cases
- Expected failures
- Security-relevant behavior
- Regression scenarios

---

# 🔐 Security Requirements

Security issues should be treated carefully.

Do **not** commit:

- API keys
- Passwords
- Access tokens
- Private credentials
- Personal secrets
- Sensitive security data

Never hard-code credentials into source code.

Use secure environment configuration or an appropriate secret-management mechanism instead.

---

# 🤖 AI-Specific Guidelines

Because SOC-Aid uses AI-assisted analysis, contributions affecting the LLM workflow should follow these principles.

### Evidence First

AI-generated conclusions should be grounded in available evidence.

### No Unsupported Claims

The system should not present assumptions as confirmed facts.

### Fact / Inference / Unknown

Where appropriate, distinguish between:

```text
FACT
INFERENCE
UNKNOWN
```

### Human Oversight

AI output should support the analyst rather than replace appropriate human judgment.

### No Autonomous Blocking

Do not introduce autonomous destructive security actions without explicit architectural review and appropriate safety controls.

---

# 📊 Changes to Risk Assessment

Changes to the risk-assessment logic require extra care.

If you modify:

- Severity scores
- Risk thresholds
- Correlation bonuses
- Risk-level mapping
- Evidence-based scoring

then update the relevant tests and documentation.

Risk behavior should remain:

- Explainable
- Reproducible
- Testable
- Clearly documented

---

# 🧩 Changes to the Agent Workflow

Changes to the agent workflow should preserve the overall processing model:

```text
Alert
  ↓
Parse
  ↓
Correlate
  ↓
Assess Risk
  ↓
Evidence-Aware Analysis
  ↓
Recommendation
  ↓
Triage Report
  ↓
Human Review
```

If a contribution significantly changes this architecture, update `ARCHITECTURE.md` as part of the same change.

---

# 📝 Documentation Changes

Documentation improvements are encouraged.

Relevant documentation includes:

- `README.md`
- `ARCHITECTURE.md`
- `INSTALLATION.md`
- `USAGE.md`
- `TESTING.md`
- `ANALYST_GUIDE.md`
- `SECURITY.md`
- `ROADMAP.md`
- `CHANGELOG.md`

When functionality changes, update the relevant documentation so that the repository remains consistent.

---

# 💬 Commit Messages

Use clear commit messages that describe the change.

Examples:

```text
feat: add authentication alert correlation
fix: handle missing alert severity
test: add invalid alert scenarios
docs: update analyst workflow
security: improve input validation
refactor: simplify risk assessment
```

Keep commits focused where practical.

---

# 🔄 Pull Requests

When opening a pull request, include:

### What changed?

Briefly describe the implementation.

### Why was it needed?

Explain the problem or motivation.

### How was it tested?

Mention the tests or verification performed.

### Security impact

Explain whether the change affects security behavior.

### Documentation

Mention any documentation that was updated.

---

# ✅ Pull Request Checklist

Before submitting a pull request:

- [ ] The change is focused and relevant
- [ ] Existing functionality still works
- [ ] Tests pass
- [ ] New tests were added where appropriate
- [ ] Documentation was updated where necessary
- [ ] No secrets or credentials were committed
- [ ] Security implications were considered
- [ ] AI-generated conclusions remain evidence-aware
- [ ] Human oversight has not been bypassed
- [ ] Commit messages are clear

---

# 🚨 Reporting Security Issues

Please do not publicly disclose sensitive security vulnerabilities before they can be responsibly reviewed.

If you discover a security issue, follow the reporting guidance described in:

`SECURITY.md`

Avoid including:

- API keys
- Credentials
- Private logs
- Sensitive user information
- Exploit details that could immediately enable misuse

---

# 🎯 Contribution Areas

Contributions are particularly useful in the following areas:

### 🛡️ Security

- Input validation
- Security hardening
- Secret handling
- Safe AI integration

### 🧪 Testing

- New test cases
- Edge cases
- Regression tests
- Evaluation methodology

### 🔗 Correlation

- Improved alert relationships
- Temporal correlation
- Additional security context

### 🤖 AI Analysis

- Evidence grounding
- Hallucination evaluation
- Better structured analysis

### 👤 Analyst Experience

- UI improvements
- Report readability
- Investigation workflow

### 📖 Documentation

- Tutorials
- Examples
- Architecture explanations
- Analyst guidance

---

# 🌱 Development Philosophy

SOC-Aid values:

> **Safety over automation.**

> **Evidence over assumptions.**

> **Explainability over opaque decisions.**

> **Human oversight over uncontrolled autonomy.**

Contributions should strengthen these principles rather than weaken them.

---

# 🙌 Thank You

Every useful contribution helps improve SOC-Aid.

Whether you contribute code, tests, documentation, research, security feedback, or ideas, your contribution is appreciated.

**Thank you for helping make SOC-Aid more reliable, explainable, and useful for security analysts.** 🛡️
