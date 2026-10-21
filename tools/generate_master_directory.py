#!/usr/bin/env python3
"""Generate the vault's static Markdown master directory from note metadata."""

from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "Master Directory.md"
EXCLUDED_PARTS = {".git", ".obsidian", "Excalidraw", "attachements", "Templates"}
REQUIRED_FIELDS = ("course", "chapter", "concept")
FRONTMATTER_DELIMITER = "---"
COURSEWORK_COURSES = {
    "AWS cloud pract basic",
    "CSCI203",
    "CSCI218",
    "CSCI262",
    "CSCI316",
    "CSCI323",
    "CSCI369",
    "CSIT 123",
    "CSIT 127",
    "CSIT 213",
    "CSIT114",
    "CSIT224",
    "CSIT 235",
    "CSIT302",
    "ISIT 312",
    "JC Computing",
    "MATH 225",
}


@dataclass(frozen=True)
class Note:
    path: Path
    title: str
    course: str
    chapter: str
    concept: str


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str] | None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith(f"{FRONTMATTER_DELIMITER}\n"):
        return None

    closing = text.find(f"\n{FRONTMATTER_DELIMITER}\n", len(FRONTMATTER_DELIMITER))
    if closing == -1:
        raise ValueError("frontmatter is not closed")

    metadata: dict[str, str] = {}
    for line in text[len(FRONTMATTER_DELIMITER) + 1 : closing].splitlines():
        if not line or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"invalid metadata line: {line!r}")
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not key or not value:
            raise ValueError(f"invalid metadata line: {line!r}")
        metadata[key] = value.strip("\"'")

    return metadata, text[closing + len(FRONTMATTER_DELIMITER) + 2 :]


def note_title(body: str, path: Path) -> str:
    match = re.search(r"(?m)^#\s+(.+?)\s*$", body)
    if not match:
        return path.stem
    return match.group(1).strip()


def is_candidate(path: Path) -> bool:
    return (
        path.suffix == ".md"
        and path != OUTPUT
        and path.stat().st_size > 0
        and not (EXCLUDED_PARTS & set(path.relative_to(ROOT).parts))
    )


def collect_notes() -> tuple[list[Note], list[str]]:
    notes: list[Note] = []
    errors: list[str] = []
    for path in sorted(ROOT.rglob("*.md")):
        if not is_candidate(path):
            continue
        relative = path.relative_to(ROOT)
        try:
            parsed = parse_frontmatter(path)
            if parsed is None:
                errors.append(f"{relative}: missing frontmatter")
                continue
            metadata, body = parsed
            if metadata.get("index") == "false":
                continue
            if metadata.get("index") != "true":
                errors.append(f"{relative}: index must be true or false")
                continue
            missing = [field for field in REQUIRED_FIELDS if not metadata.get(field)]
            if missing:
                errors.append(f"{relative}: missing {', '.join(missing)}")
                continue
            notes.append(
                Note(
                    path=relative,
                    title=note_title(body, path),
                    course=metadata["course"],
                    chapter=metadata["chapter"],
                    concept=metadata["concept"],
                )
            )
        except ValueError as error:
            errors.append(f"{relative}: {error}")
    return notes, errors


def render(notes: list[Note]) -> str:
    grouped: dict[str, dict[str, dict[str, dict[str, list[Note]]]]] = defaultdict(
        lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    )
    for note in notes:
        section = (
            "Coursework"
            if note.course in COURSEWORK_COURSES
            or (note.course == "Independent study" and note.chapter == "Assignments")
            else "Independent study"
        )
        grouped[section][note.course][note.chapter][note.concept].append(note)

    lines = [
        "<!-- GENERATED FILE: run python3 tools/generate_master_directory.py --write -->",
        "# Master Directory",
        "",
        "This directory is generated from note frontmatter. Create new study notes from",
        "[[Templates/Study Note|Study Note]], complete its metadata, then regenerate this file.",
        "",
    ]
    for section in ("Coursework", "Independent study"):
        if section not in grouped:
            continue
        lines.extend((f"## {section}", ""))
        for course in sorted(grouped[section], key=str.casefold):
            course_notes = sum(
                len(notes)
                for chapters in grouped[section][course].values()
                for notes in chapters.values()
            )
            lines.append(f"> [!folder]- {course} ({course_notes} notes)")
            for chapter in sorted(grouped[section][course], key=str.casefold):
                concepts = grouped[section][course][chapter]
                chapter_notes = sum(len(notes) for notes in concepts.values())
                lines.append(f"> > [!note]- {chapter} ({chapter_notes} notes)")
                for concept in sorted(concepts, key=str.casefold):
                    for note in sorted(
                        concepts[concept],
                        key=lambda item: (item.title.casefold(), str(item.path).casefold()),
                    ):
                        target = note.path.with_suffix("").as_posix()
                        label = (
                            note.title
                            if note.title.casefold() == concept.casefold()
                            else f"{concept}: {note.title}"
                        )
                        lines.append(f"> > - [[{target}|{label}]]")
                lines.append(">")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate Master Directory.md from indexed note frontmatter."
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="write the generated directory")
    mode.add_argument("--check", action="store_true", help="fail if metadata or output is stale")
    args = parser.parse_args()

    notes, errors = collect_notes()
    if errors:
        print("Metadata validation failed:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1

    output = render(notes)
    if args.write:
        OUTPUT.write_text(output, encoding="utf-8")
        print(f"Wrote {OUTPUT.relative_to(ROOT)} with {len(notes)} indexed notes.")
        return 0

    if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != output:
        print("Master Directory.md is stale; run:", file=sys.stderr)
        print("python3 tools/generate_master_directory.py --write", file=sys.stderr)
        return 1
    print(f"Master Directory.md is current with {len(notes)} indexed notes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
