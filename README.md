# simrec

## Summary

`simrec` is a schema-first, domain-agnostic framework for treating simulation outputs as **evidentiary records**. It provides formal structures for extracting events from simulation artifacts and generating analytical claims that are explicitly tethered to evidence.

The framework operates strictly **above the solver layer**. It does not represent simulation internals, numerical operators, or model dynamics. Instead, it formalizes the record produced by a simulation and constrains how analytical claims may be derived from that record.

---
## Statement of Need

Across scientific and policy-relevant domains, simulation outputs are routinely used to justify analytical claims, yet the inferential link between raw artifacts and conclusions is often informal, narrative-driven, or irreproducible. Logs, figures, tables, and screenshots are summarized and reinterpreted without a formal representation of how claims are grounded in evidence.

This problem appears across domains, including density functional theory, molecular dynamics, climate modeling, agent-based simulations, and game-based simulations. While solver rigor is typically high, **post-simulation analysis lacks a shared, enforceable structure**.

`simrec` addresses this gap by introducing a minimal set of abstractions—**documents, events, evidence, and claims**—and enforcing their relationships through JSON Schema validation. In particular, it requires that every analytical claim explicitly reference concrete evidence tied to identifiable events in the simulation record.

---
## Design Principles
The design of `simrec` is guided by the following principles:
- **Record Primacy**  
    Analysis operates on records produced by simulations, not on simulators themselves.
- **Tethered Analysis**  
    All claims must cite explicit evidence fragments linked to events.
- **Domain Agnosticism**  
    The core library contains no domain-specific logic. Domain adapters live in separate repositories.
- **Above-the-Solver Boundary**  
    Numerical operators, trajectories, and internal model state are out of scope.
- **Auditability Over Expressiveness**  
    The framework prioritizes traceability and validation over narrative richness.
---
## Scope and Non-Goals
`simrec` is intentionally constrained.

--- begin TODO: this needs to be replaced with narrative prose
It does **not** attempt to:
- represent simulation models or numerical solvers,
- store full trajectories or continuous fields,
- perform causal inference or validate theoretical correctness,
- generate narratives or summaries,
- intervene in or control running simulations.
--- end TODO

The framework is concerned only with structuring and validating post-simulation reasoning. \[comment: this sentence is too strong\]

---

## Core Abstractions
`simrec` defines two primary schema-validated objects:
- **Event**  
    A non-interpretive description of an observed occurrence in the simulation record, backed by an evidence bundle (quotes, images, metrics, references).
- **Claim**  
    An analytical statement produced under a specified lens, which must reference one or more evidence units tied to events.

These schemas enforce the separation between observation and interpretation and make inferential steps explicit.

---
## Intended Audience

`simrec` is intended for researchers and practitioners who:
- analyze simulation outputs across domains,
- need auditable, evidence-based analytical workflows,
- work in environments where human judgment mediates simulation execution and interpretation.

The framework is particularly suited to settings where multiple analysts may reinterpret the same simulation record under different theoretical lenses.

---
## Repository Structure
```
simrec/
├── src/simrec/
│   ├── schema/        # JSON Schemas (Event, Claim)
│   ├── validate/      # Schema validation utilities
│   ├── core/          # Core invariants and helpers
│   └── io/            # Record I/O utilities
├── docs/              # Design notes and paper-style documentation
├── tests/             # Unit tests
└── README.md
```

Domain-specific corpora (e.g., Dwarf Fortress logs) and adapters are intentionally excluded from this repository.

---
## Related Work

`simrec` is conceptually related to work on:
- scientific provenance and reproducibility,
- audit logs and evidentiary systems,
- simulation methodology and post hoc analysis.

However, it differs in its explicit enforcement of evidence-tethered claims and its strict separation between simulation execution and analytical interpretation.

---
## License
MIT License.
---
## Citation
If you use this software or the associated schemas in your work, please cite:

`Ragasa, E. J. (2026). *simrec: Schema-first simulation records and evidence-tethered analysis*. GitHub repository. https://github.com/<your-username>/simrec`

```bibtex
@software{ragasa_simrec_2026,
  author  = {Ragasa, Eugene J.},
  title   = {simrec: Schema-first simulation records and evidence-tethered analysis},
  year    = {2026},
  url     = {https://github.com/<your-username>/simrec},
  note    = {Versioned releases available via the repository}
}
```
