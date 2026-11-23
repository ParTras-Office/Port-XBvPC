# Development and reproducibility

## Host environment used historically

- Windows host with WSL user `zdf8test`.
- C++17 toolchain at `/home/zdf8test/.local/bin/g++` in the historical local test environment.
- Representative flags: `-std=c++17 -O0 -g0 -Wall -Wextra -Wpedantic -pthread -fsanitize=address,undefined -fno-omit-frame-pointer`.
- Representative runtime: `ASAN_OPTIONS=detect_leaks=1:halt_on_error=1` and `UBSAN_OPTIONS=halt_on_error=1:print_stacktrace=1` with timeouts.

**Note:** historic command paths are deliberately not embedded in this public starter pack. They should be generalized before publishing an independently buildable codebase.

## Safe change management

1. Verify source and test artifacts against recorded SHA-256 values.
2. Create a **new stage directory**; do not overwrite previously certified stages or historical shadow files.
3. Copy exact bytes only (`shutil.copyfile`, `cp` without `-a` on mounted NTFS) and compare SHA-256.
4. Make anchored, reversible C++ transformations; require unique anchors and compare original regression suite bodies.
5. Compile with explicit warnings and sanitizers; never mark compile-only as a successful runtime test.
6. Run tests and assert exact markers, case matrix, absence of test failures and sanitizer reports.
7. Write `provenance.txt`, `build.log`, `run.log`, `gate_report.txt`, `stage_manifest.sha256`, and verify the manifest.
8. Advance the milestone only when the local operator **actually** reports PASS.

## Public repository checks

```bash
python3 tools/check_repository.py
python3 tools/generate_status.py --check
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

These checks do not compile the CPU core. Once curated code and a self-contained build target exist, the CI workflow should be extended to run real C++ tests.

## No uploading entire laboratory directories

Avoid `git add .` from the original working tree. Stage a curated export instead. Never publish OS-dependent absolute paths, home directories, temporary logs, game files, decrypted executables, third-party binaries, or credentials without deliberate review.
