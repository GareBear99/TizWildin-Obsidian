#!/usr/bin/env python3
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
SUMMARY = ROOT / 'Docs' / 'pack_summary.json'
INV = ROOT / 'Docs' / 'asset_inventory.json'


def main() -> int:
    if not SUMMARY.exists() or not INV.exists():
        print('Missing generated docs inventory files.')
        return 1

    summary = json.loads(SUMMARY.read_text())
    inventory = json.loads(INV.read_text())

    missing = []
    for item in inventory:
        target = ROOT / item['path']
        if not target.exists():
            missing.append(item['path'])

    print(f"Expected WAV count: {summary['wav_file_count']}")
    print(f"Inventory entries: {len(inventory)}")
    print(f"Missing files: {len(missing)}")

    if missing:
        for path in missing[:50]:
            print(f" - {path}")
        return 1

    print('Pack validation passed.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
