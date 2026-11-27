#!/usr/bin/env python3
"""News image entry: the world news of Friday 27 November 2026 in one image.

The picture sits beside this file as entry.png. This program checks that
the file is a PNG inside the competition limits (at most 1 MiB, at most
1024 by 1024 pixels) and copies it to the output directory as entry.png.
Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import struct
import sys

MAX_BYTES = 1_048_576
MAX_SIDE = 1024
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def read_dimensions(path):
    """Return (width, height) from the PNG IHDR chunk, or raise ValueError."""
    with open(path, "rb") as handle:
        head = handle.read(24)
    if len(head) < 24 or not head.startswith(PNG_SIGNATURE):
        raise ValueError("entry.png is not a PNG file")
    if head[12:16] != b"IHDR":
        raise ValueError("entry.png has no IHDR chunk")
    return struct.unpack(">II", head[16:24])


def check_whole(path):
    """Raise ValueError unless the file ends with a complete IEND chunk."""
    with open(path, "rb") as handle:
        handle.seek(-12, os.SEEK_END)
        tail = handle.read(12)
    if len(tail) < 12 or tail[4:8] != b"IEND":
        raise ValueError("entry.png is truncated: no complete IEND chunk")


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    size = os.path.getsize(source)
    if size > MAX_BYTES:
        raise ValueError(f"entry.png is {size} bytes, over the {MAX_BYTES} byte limit")
    width, height = read_dimensions(source)
    if width > MAX_SIDE or height > MAX_SIDE:
        raise ValueError(f"entry.png is {width}x{height}, over the {MAX_SIDE} pixel limit")
    check_whole(source)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(source, os.path.join(out_dir, "entry.png"))
    print(f"entry.png: {width}x{height}, {size} bytes, copied to {out_dir}")


if __name__ == "__main__":
    sys.exit(main())
