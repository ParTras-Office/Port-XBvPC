# Roadmap

This is a technical research roadmap, not a promised feature or release schedule.

| Priority | Milestone | Acceptance criterion |
|---|---|---|
| P0 | Complete P10-S1-R1 | Actual WSL `BUILD_RC=0`, `RUN_RC=0`, exact gate PASS, 48/48, 2/2 rebases, 4/4 calls, sanitizer clean. |
| P0 | Curate public sources | Reviewed ownership and no binary/proprietary materials; clean source-only snapshot with SHA-256. |
| P1 | Standalone C++ build | Fresh checkout builds on Ubuntu/WSL in a CI job; no dependence on the original nested private paths. |
| P1 | Harden PE parser / relocations | Table-driven tests for truncated/malformed headers, bounds, overflowing deltas, incompatible permissions, atomic failure. |
| P1 | Regression harness | Standardized structured test output, versioned fixtures and deterministic reports. |
| P2 | API / ABI coverage | Detailed matrix of implemented instructions and guest calling-convention semantics, evidence per behavior. |
| P3 | Expanded execution capability | Only after independent verified builds and benchmarks; no title compatibility claims without actual reproduction. |

## Release criteria

A release requires clean source provenance, build instructions tested from a fresh clone, a declared license, CI green for real code (not only docs), tests with preserved evidence, and a transparent limitations section.
