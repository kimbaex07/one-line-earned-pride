"""One Line of Earned Pride — entry program.

Reads the single line stored in entry.txt (kept beside this file) and
writes its exact bytes to $MAKEFUN_OUTPUT_DIR/entry.txt, the path the
make.fun grader reads. Pure Python standard library, no third-party
imports, no network access, no secrets.
"""

import os
import stat
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "entry.txt"
    text = source.read_text(encoding="utf-8")
    # The contest gate accepts 1 to 240 characters; refuse to emit
    # anything outside that range rather than submit an invalid entry.
    stripped = text.strip()
    if not 1 <= len(stripped) <= 240:
        raise ValueError(
            f"entry.txt must hold 1-240 characters, got {len(stripped)}"
        )
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(text.encode("utf-8"))
    os.chmod(target, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    print(f"wrote {len(text.encode('utf-8'))} bytes to {target}")


if __name__ == "__main__":
    main()
