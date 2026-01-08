title: `simrec`: Schema-first records for evidence-tethered analysis
tags:
  - simulation
  - reproducibility
  - provenance
  - scientific-computing
  - methods
authors:
  - name: Eugene J. Ragasa
    orcid: https://orcid.org/0000-0002-3856-734X
    affiliation: 1
affiliations:
 - name: Department of Physics, De La Salle University, Manila, Philippines
   index: 1
date: 2026-XX-XX
bibliography: paper.bib
---
## Summary

**simrec** is a schema-first framework for constructing falsifiable analytical claims by explicitly tethering them to structured records derived from simulation outputs. A claim is falsifiable if its supporting evidence can be identified and examined to determine whether it supports the claim. Claims with missing, contradictory, or ill-posed evidence can be rejected without reliance on narrative interpretation.
## Statement of Need

Analytical claims are often derived from simulation outputs without an explicit representation of how those claims are grounded in the underlying record. Figures, tables, logs, and summaries are treated as self-evident, while the inferential steps linking them to conclusions remain implicit.

This limits traceability and reanalysis across workflows. **simrec** addresses this gap by defining formal schemas for events and claims, and by allowing unstructured simulation artifacts to be converted into structured records using automated extraction tools, without constraining domain theory or solver implementation.
## Software Design

**simrec** is organized around two core abstractions: events and claims. Events represent observational occurrences extracted from simulation records. Claims represent analytical statements that explicitly reference supporting evidence.

The framework is schema-first. JSON Schemas define the structure of events and claims, and validation enforces evidence tethering. Domain semantics, solver internals, and analytical interpretation are intentionally excluded.

A reference implementation provides tooling for record ingestion, event extraction, schema validation, and claim construction. Independent implementations are supported.
## Research Impact Statement

The primary impact of `simrec` is methodological: it makes the evidentiary basis of analytical claims explicit and checkable across simulation workflows. The framework applies to simulation-driven workflows, including cases where internal model state is inaccessible and analysis proceeds through recorded artifacts.
## Availability

All materials associated with this work are publicly available. Documentation is released under a permissive attribution license. The reference implementation code is released under the MIT License. The event and claim schemas are released under CC0-1.0 and are intended to function as open, reusable specifications. Source code and schemas are available in the public repository [@ragasa2026simrec_github].
## AI usage disclosure

LLM-based tools were used to support ideation, drafting of documentation, generation of initial code and tests, and routine development assistance such as stack trace analysis. All AI-assisted outputs were reviewed, edited, and validated by the author. Conceptual design, methodological decisions, and final implementation choices were made by the human author.

