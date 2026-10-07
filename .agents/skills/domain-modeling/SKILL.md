---
name: domain-modeling
description: "Use when clarifying domain terms, write boundaries, glossary definitions, or consequential architecture decisions."
---

# Domain Modeling

Read `GLOSSARY.md`. Challenge conflicting/overloaded terms and propose precise definitions.
Test relationships using concrete scenarios, especially indirect equipment effects and
agent versus application permissions. Check claims against existing code when possible.

Capture agreed terms promptly in a term/meaning table, without implementation choices
or speculative requirements. Create files only for resolved content, not empty trees.

Offer ADRs only for costly-to-reverse decisions needing context with real trade-offs.
Use `docs/adr/<number>-<name>.md` with status, context, alternatives, decision,
consequences, owner, and date. Never record secrets.

Requirements belong in PRD, gaps in handover, and policies in standards. Do not duplicate
these in the glossary or interpret this workflow as permission to expand scope.