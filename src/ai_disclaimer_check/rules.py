from __future__ import annotations

from ai_disclaimer_check.models import Rule

PROJECT_NAME = 'ai-disclaimer-check'
SUMMARY = 'Lint AI-generated content templates for disclosure and unsupported-claim gaps.'
SAMPLE_RISK = 'generated answer disclaimer missing medical advice guaranteed'
SAMPLE_CLEAN = 'generated answer disclosure included health domain blocked certainty none'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "service", "endpoint", "field", "event")

RULES = (
    Rule(
        code='missing-disclaimer',
        severity='high',
        pattern='disclaimer\\s+(missing|none|unknown)',
        message='AI disclosure missing',
        recommendation='add appropriate disclosure',
    ),
    Rule(
        code='medical-advice',
        severity='medium',
        pattern='medical advice',
        message='medical advice phrase detected',
        recommendation='route to safe domain policy',
    ),
    Rule(
        code='guarantee-claim',
        severity='low',
        pattern='guaranteed|guarantee',
        message='guarantee language detected',
        recommendation='soften unsupported guarantees',
    ),
)
