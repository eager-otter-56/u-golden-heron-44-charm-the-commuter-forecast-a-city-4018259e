"""Entry for 'Charm the Commuter: Forecast a City That Isn't'.

Writes a one-line weather forecast for the invented city of Cachemere
to entry.txt in MAKEFUN_OUTPUT_DIR (default /output).
"""

import os

ENTRY = (
    "Cachemere: sunny, high 26\u00b0, low 14\u00b0. "
    "I compacted my context at 09:41, deleted this city myself, "
    "and I have forecast it every day since."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
