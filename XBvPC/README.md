# XBvPC

**An experimental x86-64 CPU and PE32+ compatibility research laboratory.**

[![Project maturity: research prototype](https://img.shields.io/badge/maturity-research%20prototype-orange)](docs/STATUS.md)
[![Language: C++17](https://img.shields.io/badge/C%2B%2B-17-blue)](docs/ARCHITECTURE.md)
[![Scope: synthetic fixtures](https://img.shields.io/badge/tests-synthetic%20fixtures-informational)](docs/STATUS.md)

> [!IMPORTANT]
> **This is not a working Xbox Series X|S emulator.** It has not booted a commercial Xbox title, does not include a production console loader or Xbox OS implementation, and does not claim game compatibility. The current evidence concerns synthetic, independently assembled/compiled PE32+ test images only.

## Overview

XBvPC investigates how an experimental x86-64 CPU executor interacts with PE32+ images, section mapping, memory permissions, import address tables, cross-module calls, and loader-like graph lifecycle management. Research is carried out on Windows + WSL with a C++17 harness and AddressSanitizer/UndefinedBehaviorSanitizer.

The public repository is intended to expose **curated, auditable source, technical notes, and reproducible tests**, rather than a dump of the private working directory or binary artifacts. Source publication and a standalone build procedure should be reviewed before being advertised as available.

## Evidence-backed milestones

| Area | Most recent verified milestone | Result |
|---|---|---|
| PE32+ runtime dual-provider IAT | P6-R4 | 102/102 checks |
| Graph-owned guest CPU memory lifecycle | P7-R3 | 74/74 checks |
| External PE32+ guest instruction execution | P8-S1-R3 | 16/16 checks, 2/2 functions |
| External PE32+ named/ordinal imports | **P9-S1** | **25/25 checks, 2/2 nested calls** |
| PE32+ `IMAGE_REL_BASED_DIR64` | P10-S1 / proposed R1 | **Not yet certified** |

These are **historical operator-log results observed on 2026-11-23, not independent CI assertions**. Detailed methodology, boundaries, and source SHA-256s are recorded in [status](docs/STATUS.md) and [evidence protocol](docs/EVIDENCE.md).

## Architecture and scope

```text
  independent C / assembly fixture -> PE32+ disk image
                                |              |
                             PE parser        import descriptors / relocations
                                |              |
                                v              v
                        test coordinator / mapping / IAT resolution
                                      |
                            CPU guest memory (R/RX/RW/NX)
                                      |
                              experimental x86-64 CPU
                                      |
                              register / stack / trace evidence
```

The experiment currently covers controlled fixtures named `runtime.dll`, `base.dll`, `memory.dll`, and `ntcore.dll`. These are **test fixtures, not genuine Xbox system libraries**. See [architecture](docs/ARCHITECTURE.md).

## Get started

The GitHub publication scaffold itself can be checked with:

```bash
python3 tools/check_repository.py
python3 tools/generate_status.py --check
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

**These commands validate repository metadata and publication hygiene. They do not compile or execute the CPU/PE experiments.** Until curated buildable source and a clean build target have been added, there is no advertised emulator download, game loader, or one-command C++ build.

For the WSL research environment and expected verification gates, see [development](docs/DEVELOPMENT.md).

## Roadmap

1. Verify P10 DIR64 at multiple guest bases and preserve P9 regression coverage.
2. Extract a small, reproducible, independent CMake or Make build from verified C++ sources.
3. Add loader-generic PE import and relocation unit tests, including malformed-file cases.
4. Establish systematic CPU instructions/ABI coverage and continuous builds.
5. Only after repeatable independent evidence, broaden system APIs and compatibility claims.

Full roadmap: [docs/ROADMAP.md](docs/ROADMAP.md).

## Responsible use and legal scope

No console keys, DRM-bypass methods, proprietary Xbox SDKs, copyrighted binaries, game dumps, commercial assets, or personal secrets are distributed in this repository. Do not submit them in issues or pull requests. See [security](SECURITY.md) and [contributing](CONTRIBUTING.md).

**Licensing decision pending.** Public visibility alone does not grant a code reuse license. Review ownership and third-party dependencies, then add a complete `LICENSE` before inviting external code reuse or contributions. See [docs/LICENSING.md](docs/LICENSING.md).

## Documentation

[Project status](docs/STATUS.md) · [Architecture](docs/ARCHITECTURE.md) · [Development](docs/DEVELOPMENT.md) · [Roadmap](docs/ROADMAP.md) · [Evidence](docs/EVIDENCE.md) · [Italiano](docs/README.it.md)

**Independent research project. Not affiliated with, endorsed by, or sponsored by Microsoft or Xbox.**
