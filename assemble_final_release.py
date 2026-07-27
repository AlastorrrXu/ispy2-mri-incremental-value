#!/usr/bin/env python3
"""Reconstruct the exact frozen one-file I-SPY2 research release from source parts."""
from __future__ import annotations

import hashlib
from pathlib import Path

EXPECTED_SHA256 = "0d90623bbbb1419d5e658621c1a2a361babc9da7926cfb68fb99dfdd7f91525c"
OUTPUT_NAME = "ispy2_FINAL_RESEARCH_FROZEN_v1_4_0.py"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    root = Path(__file__).resolve().parent
    parts = sorted((root / "release_parts").glob(f"{OUTPUT_NAME}.*.part"))
    if not parts:
        raise FileNotFoundError("No release source parts were found.")
    payload = b"".join(path.read_bytes() for path in parts)
    observed = sha256_bytes(payload)
    if observed != EXPECTED_SHA256:
        raise RuntimeError(f"SHA-256 mismatch: expected {EXPECTED_SHA256}, observed {observed}")
    output = root / OUTPUT_NAME
    output.write_bytes(payload)
    print(f"Wrote: {output}")
    print(f"SHA-256: {observed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
