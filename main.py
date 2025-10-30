#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Smart System Cleaner - Prototype skeleton (Python)

Goals:
- Scan common cache/log/temp locations per OS
- Provide dry-run preview and safe delete with optional recycle bin
- Collect stats and emit JSON/CSV reports

This is a scaffold for future development.
"""

import os
import sys
import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict

SUPPORTED_MODES = {"fast", "deep", "custom"}

@dataclass
class Target:
    path: Path
    kind: str  # e.g., "cache", "log", "temp"


def guess_targets(mode: str) -> List[Target]:
    targets: List[Target] = []
    home = Path.home()
    if sys.platform.startswith("win"):
        temp = Path(os.getenv("TEMP", str(home / "AppData" / "Local" / "Temp")))
        targets += [Target(temp, "temp")]
    elif sys.platform == "darwin":
        targets += [Target(Path("/Library/Caches"), "cache"), Target(home / "Library" / "Caches", "cache")]
    else:
        targets += [Target(Path("/var/tmp"), "temp"), Target(home / ".cache", "cache"), Target(Path("/tmp"), "temp")]
    if mode == "deep":
        targets.append(Target(home / "Downloads", "leftovers"))
    return targets


def scan_paths(targets: List[Target], exclude: List[str]) -> List[Path]:
    results: List[Path] = []
    for t in targets:
        if not t.path.exists():
            continue
        for root, dirs, files in os.walk(t.path):
            if any(ex in root for ex in exclude):
                continue
            for f in files:
                p = Path(root) / f
                results.append(p)
    return results


def human_size(num: int) -> str:
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if num < 1024.0:
            return f"{num:3.1f} {unit}"
        num /= 1024.0
    return f"{num:.1f} PB"


def summarize(paths: List[Path]) -> Dict[str, str]:
    total = 0
    for p in paths:
        try:
            total += p.stat().st_size
        except Exception:
            pass
    return {"count": str(len(paths)), "size": human_size(total)}


def safe_delete(paths: List[Path], dry_run: bool = True) -> None:
    for p in paths:
        try:
            if dry_run:
                print(f"DRY-RUN would delete: {p}")
            else:
                p.unlink(missing_ok=True)
                print(f"Deleted: {p}")
        except Exception as e:
            print(f"Skip {p}: {e}")


def main():
    ap = argparse.ArgumentParser(description="Smart System Cleaner (prototype)")
    ap.add_argument("--mode", choices=sorted(SUPPORTED_MODES), default="fast")
    ap.add_argument("--dry-run", action="store_true", help="Preview without deleting")
    ap.add_argument("--paths", nargs="*", default=[], help="Additional paths to include")
    ap.add_argument("--exclude", nargs="*", default=[".git", "node_modules"], help="Exclude patterns")
    args = ap.parse_args()

    targets = [Target(Path(p), "custom") for p in args.paths] or guess_targets(args.mode)
    candidates = scan_paths(targets, exclude=args.exclude)

    stats = summarize(candidates)
    print("Candidates:", stats)

    if not candidates:
        print("No candidates found. You're already clean!")
        return

    if args.dry_run:
        for p in candidates[:20]:
            print(f"Would delete: {p}")
        print("Use without --dry-run to execute deletion.")
    else:
        safe_delete(candidates, dry_run=False)
        print("Cleanup completed.")

if __name__ == "__main__":
    main()
