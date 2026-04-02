"""Command-line interface for the agentic director."""

from __future__ import annotations

import argparse

from tucal.agents import DirectorAgent, DirectorPersona
from tucal.models import Character, format_shots


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Agentic movie director generator")
    parser.add_argument("title", help="Title for the screenplay")
    parser.add_argument("logline", help="One-sentence logline")
    parser.add_argument("theme", help="Core theme statement")
    parser.add_argument(
        "--character",
        action="append",
        default=[],
        help="Character entry in the form 'Name:role' (repeatable)",
    )
    parser.add_argument(
        "--note",
        default="Tighten the stakes and deepen emotional contrast.",
        help="Revision note to apply",
    )
    return parser


def parse_characters(entries: list[str]) -> list[Character]:
    characters = []
    for entry in entries:
        name, _, role = entry.partition(":")
        role_value = role if role else "support"
        characters.append(Character(name=name.strip(), role=role_value.strip()))
    return characters


def main() -> None:
    parser = build_arg_parser()
    args = parser.parse_args()

    persona = DirectorPersona(
        name="Autonomous ASI Director",
        style_notes="dreamlike symbolism and kinetic blocking",
        pacing="precise but elastic",
    )
    agent = DirectorAgent(persona=persona, crew_notes="Hybrid virtual unit")
    characters = parse_characters(args.character)

    script = agent.generate_script(
        title=args.title,
        logline=args.logline,
        theme=args.theme,
        characters=characters,
    )
    revised = agent.revise_script(script, args.note)

    print(revised.summarize())
    for scene in revised.scenes:
        directed = agent.direct_scene(scene)
        print(f"\nScene: {directed.title} | Location: {directed.location}")
        for beat in directed.beats:
            print(f"  - {beat}")
        print(format_shots(directed.shots))


if __name__ == "__main__":
    main()
