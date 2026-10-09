#!/usr/bin/env python3
"""Regenerate the customer URDF ZIPs from their source packages."""
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1] / 'hardware/robot-description'


def main():
    for variant in ('ld-hd', 'fl'):
        source = ROOT / variant / ('stararm102_' + variant.replace('-', '_') + '_description')
        output = ROOT / variant / ('star-arm-102-' + variant + '-urdf.zip')
        with ZipFile(output, 'w', ZIP_DEFLATED) as archive:
            for path in sorted(source.rglob('*')):
                if not path.is_file() or any(part.startswith('.') or part == '__pycache__' for part in path.relative_to(source).parts):
                    continue
                info = ZipInfo(path.relative_to(source.parent).as_posix(), date_time=(2026, 10, 9, 0, 0, 0))
                info.compress_type = ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, path.read_bytes())
        print(output)


if __name__ == '__main__':
    main()
