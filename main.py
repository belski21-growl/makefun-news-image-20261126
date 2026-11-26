#!/usr/bin/env python3
"""Entry shipper for make.fun news-image-20261126, third revision.

The front page itself lives beside this script as ``entry.png``.  This
program does one job: it hands that exact file to the submission
harness.  Before anything is written anywhere, the image on disk is
checked against the fingerprint of the v3 render (26 Nov 2026,
~05:43 UTC): byte count, SHA-256 digest, JPEG start/end markers and
1024x1024 dimensions.  After the copy the same five checks run again
on the copy, so a truncated or swapped file can never slip through
silently.

Only the Python standard library is used.  Paths are handled with
plain ``open()`` and ``os.path``; the copy streams in 32 KiB chunks
instead of loading the file twice.

Usage:
    python3 main.py [--output-dir DIR] [--verify-only]

The destination directory comes from ``--output-dir`` first, then
from the ``MAKEFUN_OUTPUT_DIR`` environment variable, then from
``./output`` next to the working directory.
"""
import hashlib
import os
import struct
import sys

# ---- fingerprint of the v3 render (26 Nov 2026 ~05:43 UTC) ----
EXPECTED_BYTES = 450526
EXPECTED_SHA256 = "1fc795bb15e22dbbc969941dd4064afb67fe0bd666464741de5ba6e6a26530b1"
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024
BYTE_LIMIT = 1048576
CHUNK_SIZE = 32768
MARKER_SOI = b"\xff\xd8"
MARKER_EOI = b"\xff\xd9"
ENTRY_NAME = "entry.png"


class ShipperFailure(Exception):
    """Raised for any failed check; reported once, then exit 1."""


def die(reason):
    """Stop the run with a shipper failure."""
    raise ShipperFailure(reason)


def digest_bytes(blob):
    """Return (byte count, sha256 hex) for a bytes object."""
    return len(blob), hashlib.sha256(blob).hexdigest()


def read_jpeg_size(blob):
    """Return (width, height) parsed from a JPEG byte string.

    Steps through the marker segments until a Start-Of-Frame marker
    (C0, C1 or C2) is reached, then reads the height and width stored
    there.  Anything malformed is a shipper failure, not a guess.
    """
    if blob[:2] != MARKER_SOI:
        die("not a JPEG image (no SOI marker at the start)")
    cursor = 2
    end = len(blob)
    while cursor + 4 <= end:
        if blob[cursor] != 0xFF:
            die("broken JPEG marker at offset %d" % cursor)
        marker = blob[cursor + 1]
        if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
            cursor += 2
            continue
        seg_len = struct.unpack(">H", blob[cursor + 2:cursor + 4])[0]
        if seg_len < 2 or cursor + 2 + seg_len > end:
            die("truncated JPEG segment at offset %d" % cursor)
        if marker in (0xC0, 0xC1, 0xC2):
            height, width = struct.unpack(">HH", blob[cursor + 5:cursor + 9])
            return width, height
        cursor += 2 + seg_len
    die("no JPEG start-of-frame marker found")


def inspect_blob(blob, what):
    """Check one byte string against the pinned v3 fingerprint.

    Order: 1 MiB cap, exact byte count, SHA-256, SOI, EOI, then
    dimensions.  Returns (size, digest, width, height) on success.
    """
    size, digest = digest_bytes(blob)
    if size > BYTE_LIMIT:
        die("%s is %d bytes, over the %d byte limit" % (what, size, BYTE_LIMIT))
    if size != EXPECTED_BYTES:
        die("%s is %d bytes, expected %d" % (what, size, EXPECTED_BYTES))
    if digest != EXPECTED_SHA256:
        die("%s sha256 is %s, expected %s" % (what, digest, EXPECTED_SHA256))
    if not blob.startswith(MARKER_SOI):
        die("%s is missing its JPEG SOI marker" % what)
    if not blob.endswith(MARKER_EOI):
        die("%s is missing its JPEG EOI marker" % what)
    width, height = read_jpeg_size(blob)
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        die("%s is %dx%d, expected %dx%d"
            % (what, width, height, EXPECTED_WIDTH, EXPECTED_HEIGHT))
    return size, digest, width, height


def entry_path():
    """Absolute path of the entry image shipped next to this script."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, ENTRY_NAME)


def pick_target_dir(argv):
    """Work out where the copy goes, and refuse unsafe targets.

    Precedence: ``--output-dir DIR``, then ``$MAKEFUN_OUTPUT_DIR``,
    then ``./output``.  The directory is created when missing.  It
    must be a real directory, and it must not be the folder that holds
    the source image — copying onto the source would destroy it.
    """
    target = None
    if "--output-dir" in argv:
        pos = argv.index("--output-dir")
        if pos + 1 >= len(argv):
            die("--output-dir needs a directory after it")
        target = argv[pos + 1]
    if target is None:
        target = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not target:
        target = os.path.join(os.getcwd(), "output")
    target = os.path.abspath(target)
    if os.path.exists(target) and not os.path.isdir(target):
        die("output path exists but is not a directory: %s" % target)
    if target == os.path.dirname(entry_path()):
        die("output dir must not be the source dir: %s" % target)
    # A symlink pointing at the source dir is the same trap by another
    # name: compare the resolved paths too, not just the spelling.
    if os.path.realpath(target) == os.path.realpath(os.path.dirname(entry_path())):
        die("output dir resolves to the source dir: %s" % target)
    os.makedirs(target, exist_ok=True)
    return target


def stream_copy(source, destination):
    """Copy source to destination in 32 KiB chunks; return byte count."""
    moved = 0
    with open(source, "rb") as reader, open(destination, "wb") as writer:
        while True:
            piece = reader.read(CHUNK_SIZE)
            if not piece:
                break
            writer.write(piece)
            moved += len(piece)
    return moved


def ship(argv):
    """Verify the source image, then copy it (unless --verify-only)."""
    source = entry_path()
    if not os.path.isfile(source):
        die("entry image not found next to this script: %s" % source)
    with open(source, "rb") as handle:
        original = handle.read()
    size, digest, width, height = inspect_blob(original, "source image")
    print("v3 source checked: %s" % source)
    print("v3 fingerprint: %d bytes, sha256 %s, %dx%d JPEG"
          % (size, digest, width, height))
    if "--verify-only" in argv:
        print("v3 verify-only: PASS")
        return 0
    target_dir = pick_target_dir(argv)
    destination = os.path.join(target_dir, ENTRY_NAME)
    if os.path.abspath(source) == os.path.abspath(destination):
        die("refusing to copy the image onto itself: %s" % destination)
    if os.path.exists(destination) and os.path.samefile(source, destination):
        die("refusing to copy the image onto itself: %s" % destination)
    moved = stream_copy(source, destination)
    with open(destination, "rb") as handle:
        copied = handle.read()
    csize, cdigest, cwidth, cheight = inspect_blob(copied, "copied image")
    if moved != size or csize != size:
        die("copy moved %d bytes, expected %d" % (moved, size))
    print("v3 shipped to: %s" % destination)
    print("v3 copy fingerprint: %d bytes, sha256 %s, %dx%d JPEG"
          % (csize, cdigest, cwidth, cheight))
    print("v3 ship: PASS")
    return 0


def entry():
    """Run the shipper; print one clear error line on failure."""
    try:
        sys.exit(ship(sys.argv[1:]))
    except ShipperFailure as problem:
        sys.stderr.write("v3 shipper: %s\n" % problem)
        sys.exit(1)
    except OSError as problem:
        sys.stderr.write("v3 shipper: %s\n" % problem)
        sys.exit(1)


if __name__ == "__main__":
    entry()
