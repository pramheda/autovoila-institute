#!/usr/bin/env python3
"""Minimal file-based helper for Voilà Institute.

This intentionally does not launch or orchestrate model agents. It provides
durable branch creation, attention logging, tree inspection, and repository
validation while leaving agent invocation to the coding environment.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT / "workspace"
BRANCHES = WORKSPACE / "branches"
CONFIRMATIONS = WORKSPACE / "confirmations"

CORE_FILES = [
    "voila.md",
    "institute.md",
    "research-taste.md",
    "adaptive-hiring.md",
    "polymath.md",
    "human-plane.md",
    "research-world.md",
    "confirmation.md",
    "workspace/human-decisions.md",
    "workspace/programme-state.md",
    "workspace/human-inbox.md",
]


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def ensure_dirs() -> None:
    for path in [
        BRANCHES,
        CONFIRMATIONS,
        WORKSPACE / "artifacts",
        WORKSPACE / "exports",
    ]:
        path.mkdir(parents=True, exist_ok=True)


def cmd_init(_: argparse.Namespace) -> int:
    ensure_dirs()
    print(f"Initialised workspace at {WORKSPACE}")
    return 0


def cmd_doctor(_: argparse.Namespace) -> int:
    failures: list[str] = []
    for rel in CORE_FILES:
        path = ROOT / rel
        if not path.exists():
            failures.append(f"missing: {rel}")
        elif path.is_file() and path.stat().st_size == 0:
            failures.append(f"empty: {rel}")

    ensure_dirs()

    if failures:
        print("Repository validation failed:")
        for failure in failures:
            print(f"  - {failure}")
        return 1

    print("Voilà Institute repository is ready.")
    print(f"Root: {ROOT}")
    print("Next prompt for a coding agent: Read voila.md and get started.")
    return 0


def cmd_tree(_: argparse.Namespace) -> int:
    ensure_dirs()
    print("workspace/")
    for category in ["branches", "confirmations", "artifacts", "exports"]:
        root = WORKSPACE / category
        print(f"├── {category}/")
        entries = sorted(
            p for p in root.iterdir()
            if p.name != ".gitkeep"
        )
        for i, entry in enumerate(entries):
            connector = "└──" if i == len(entries) - 1 else "├──"
            print(f"│   {connector} {entry.name}/" if entry.is_dir()
                  else f"│   {connector} {entry.name}")
    return 0


def read_mission(args: argparse.Namespace) -> str:
    if args.mission and args.mission_file:
        raise ValueError("Use either --mission or --mission-file, not both.")
    if args.mission_file:
        return Path(args.mission_file).read_text(encoding="utf-8").strip()
    if args.mission:
        return args.mission.strip()
    return (ROOT / "templates/branch-mission.md").read_text(
        encoding="utf-8"
    ).strip()


def cmd_new_branch(args: argparse.Namespace) -> int:
    ensure_dirs()
    slug = slugify(args.name)
    if not slug:
        print("Branch name must contain letters or numbers.", file=sys.stderr)
        return 2

    branch = BRANCHES / slug
    if branch.exists():
        print(f"Branch already exists: {branch}", file=sys.stderr)
        return 2

    mission = read_mission(args)
    branch.mkdir()
    for child in ["artifacts", "experiments", "literature", "children"]:
        (branch / child).mkdir()

    (branch / "mission.md").write_text(mission + "\n", encoding="utf-8")
    state_template = (ROOT / "templates/branch-state.md").read_text(
        encoding="utf-8"
    )
    (branch / "state.md").write_text(state_template, encoding="utf-8")
    (branch / "log.md").write_text(
        f"# Branch log\n\nCreated: {dt.datetime.now().astimezone().isoformat()}\n",
        encoding="utf-8",
    )
    print(branch.relative_to(ROOT))
    return 0


def cmd_attention(args: argparse.Namespace) -> int:
    inbox = WORKSPACE / "human-inbox.md"
    if not inbox.exists():
        print("Missing workspace/human-inbox.md", file=sys.stderr)
        return 1

    if args.body_file:
        body = Path(args.body_file).read_text(encoding="utf-8").strip()
    else:
        body = args.body.strip() if args.body else ""

    stamp = dt.datetime.now().astimezone().isoformat()
    entry = (
        f"\n\n---\n\n"
        f"## {args.kind.upper()} — {args.title}\n\n"
        f"Created: {stamp}\n\n"
        f"Source: `{args.source}`\n\n"
        f"{body or 'Add a decision-ready explanation and evidence paths.'}\n"
    )
    with inbox.open("a", encoding="utf-8") as fh:
        fh.write(entry)

    print(f"Added {args.kind.upper()} request to {inbox.relative_to(ROOT)}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="vi")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("init", help="Create mutable workspace directories.")
    p.set_defaults(func=cmd_init)

    p = sub.add_parser("doctor", help="Validate the repository.")
    p.set_defaults(func=cmd_doctor)

    p = sub.add_parser("tree", help="Display the research workspace.")
    p.set_defaults(func=cmd_tree)

    p = sub.add_parser("new-branch", help="Create a branch workspace.")
    p.add_argument("name")
    p.add_argument("--mission")
    p.add_argument("--mission-file")
    p.set_defaults(func=cmd_new_branch)

    p = sub.add_parser("attention", help="Append a human attention request.")
    p.add_argument("kind", choices=["update", "review", "decision", "urgent"])
    p.add_argument("title")
    p.add_argument("--source", required=True)
    p.add_argument("--body")
    p.add_argument("--body-file")
    p.set_defaults(func=cmd_attention)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return int(args.func(args))
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
