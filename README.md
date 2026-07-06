# AI Disclaimer Check

![AI Disclaimer Check cover](assets/readme-cover.svg)

Lint machine-written content templates for disclosure and unsupported-claim gaps.

## The rule file is the product

- `missing-disclaimer` (high): AI disclosure missing. Fix: add appropriate disclosure.
- `medical-advice` (medium): medical advice phrase detected. Fix: route to safe domain policy.
- `guarantee-claim` (low): guarantee language detected. Fix: soften unsupported guarantees.

Everything else in the repo exists to feed records into those checks and render the answer in a way a person can act on.

## Shell session

```bash
git clone https://github.com/mertefekurt/ai-disclaimer-check.git
cd ai-disclaimer-check
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
ai-disclaimer-check examples/sample.txt
ai-disclaimer-check examples/sample.txt --json
```

## Repository shape

```text
.github/        CI workflow
examples/       sample inputs
src/            package source
tests/          test coverage
.gitignore      project file
pyproject.toml  package metadata
```
