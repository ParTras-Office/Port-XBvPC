# Architecture — research scope

## Components observed in local operator tests

1. **Synthetic fixture generator.** Produces test PE32+ images and export/import descriptors; later tests incorporate separately compiled or assembled x64 routines.
2. **PE parser / mapping helpers.** Interprets headers, sections, image sizes, section flags, and maps guest pages with R, RX, or RW/NX access.
3. **Import binder.** For P9, inspects an external PE import descriptor, resolves `base.dll!Alpha` and `base.dll!#7` against a synthetic registry and commits IAT patches only after both symbols resolve.
4. **CPU execution.** Runs limited guest x86-64 instructions, tracking RIP, RAX, RSP, halts, faults and step counts.
5. **Graph lifecycle test coordinator.** Coordinates four synthetic modules and guest CPU-owned memory across attach, guest calls, unload, reload and rollback.
6. **Experimental DIR64 candidate.** Adds `.reloc`, an `IMAGE_REL_BASED_DIR64` record and staged rebasing of one absolute pointer; not yet certified as of 2026-11-23.

## Non-goals / unimplemented

- Xbox system API equivalence, services, kernel, content delivery, title launching.
- Full x64 instruction set or ABI completeness.
- GPU/Direct3D compatibility for actual Xbox titles.
- Package decryption, console key extraction, DRM circumvention.
- A robust generic PE loader for arbitrary untrusted executables.

**Trust boundaries:** fixture parsing and staged writes should be validated against bounds and permissions; failure should not publish partial graph state or IAT writes. Synthetic tests alone do not establish security for arbitrary PE files.
