# Verification evidence protocol

## Three separate claims

- **Generated:** a fixture or source was produced. This does not demonstrate compilation.
- **Compiled:** the compiler reported exit code 0. This does not demonstrate execution.
- **Certified in a local test log:** build/run exit codes were 0, expected marker matrix was complete, sanitizer output was absent and manifest/hash checks passed.

The `data/milestones.json` registry captures claims observed from operator logs provided in the project's development conversation. It is a **historical log summary**, not independent CI validation. GitHub workflow success, if present, covers only the tasks explicitly executed by that workflow.

## Evidence required before changing a pending milestone to PASS

- Exact Git commit or source SHA-256.
- Host/OS/toolchain and reproducible command.
- `BUILD_RC`, `RUN_RC`, exact test counts and gate string.
- Sanitizer output and all negative-case verification.
- Evidence of original source and shadow-file immutability.
- Logged output is stored without passwords, personal information, game binaries or paths that should remain private.

## Next state

As of 2026-11-23, the latest certified stage is P9-S1. P10-S1-R1 was prepared but has no observed PASS log. Do not change this status merely because a command was written or a PE file generated.
