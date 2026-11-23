# Project status — evidence from local research logs

**As of:** 2026-11-23

**Latest certified milestone:** `P9-S1`

> This table summarizes user-supplied local operator logs. It is not a GitHub CI or independent audit.

| Milestone | Status | Tests | Verified research scope |
|---|---|---|---|
| P0 | Local PASS | 78/78 | PE/IAT guest calls |
| P1-R1 | Local PASS | 80/80 | four DLL chain |
| P2 | Local PASS | 58/58 | nested calls and ABI |
| P3 | Local PASS | 42/42 | page protections and W^X |
| P4-R2 | Local PASS | 42/42 | RW data and header rebase |
| P5 | Local PASS | 62/62 | four DLL data stores and nested calls |
| P6-R4 | Local PASS | 102/102 | two-provider PE import binding |
| P7-R3 | Local PASS | 74/74 | guest CPU memory lifecycle |
| P8-S1-R3 | Local PASS | 16/16 | externally compiled PE32+ x64 guest code |
| P9-S1 | Local PASS | 25/25 | external named/ordinal PE imports |
| P10-S1-R1 | PENDING / not certified | — | DIR64 rebasing at two guest bases; operator prepared; result not yet observed |

No real commercial Xbox title has been booted or tested in this research lab. This is **not** a working Xbox emulator.

Source/fixture hashes and full gate logs should be retained in a private provenance archive and redacted before selective publication.
