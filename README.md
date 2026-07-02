# ai-disclaimer-check

> Lint AI-generated content templates for disclosure and unsupported-claim gaps.

## CLI contract Overview

Lint AI-generated content templates for disclosure and unsupported-claim gaps. It solves review drift by turning plain-text plans into deterministic CI-friendly findings.

## Input Contract 23

Accepts AI content template. The reader supports plain text, JSON, JSONL, and CSV so the
tool can fit into scripts, CI jobs, and review exports.

## CLI Walkthrough 23

```bash
python -m pip install -e ".[dev]"
ai-disclaimer-check examples/sample.txt
ai-disclaimer-check examples/sample.txt --json --fail-on medium
python -m ai_disclaimer_check --help
```

## Rule Surface 23

| Rule | Severity | Meaning |
|---|---:|---|
| `missing-disclaimer` | high | AI disclosure missing |
| `medical-advice` | medium | medical advice phrase detected |
| `guarantee-claim` | low | guarantee language detected |

## Validation Notes 23

```bash
ruff check .
pytest
python -m ai_disclaimer_check --help
```

Example risky input:

```text
generated answer disclaimer missing medical advice guaranteed
```

Architecture: `cli.py` handles arguments, `core.py` reads and evaluates records, and
`rules.py` keeps the project-specific policy explicit.

License: MIT.
