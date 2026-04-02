"""Agentic movie director logic."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Sequence

from tucal.models import Character, Scene, Script, Shot


@dataclass(frozen=True)
class DirectorPersona:
    """Defines a directing persona that biases story output."""

    name: str
    style_notes: str
    pacing: str


@dataclass
class DirectorAgent:
    """A lightweight agent that produces a directed script outline."""

    persona: DirectorPersona
    crew_notes: str

    def generate_script(
        self,
        title: str,
        logline: str,
        theme: str,
        characters: Sequence[Character],
    ) -> Script:
        """Generate a script structure based on the persona and characters."""

        scenes = (
            self._build_opening(characters),
            self._build_midpoint(characters),
            self._build_finale(characters),
        )
        return Script(title=title, logline=logline, theme=theme, scenes=scenes)

    def direct_scene(self, scene: Scene) -> Scene:
        """Attach a directed shot list to a scene."""

        shots = (
            Shot(
                name="Establishing",
                description=f"Reveal {scene.location} with {self.persona.style_notes}.",
                camera="Wide crane move",
                audio="Ambient tone with sparse score",
            ),
            Shot(
                name="Character focus",
                description="Follow the lead as stakes rise.",
                camera=f"Handheld, {self.persona.pacing}",
                audio="Dialogue-forward mix",
            ),
            Shot(
                name="Transition",
                description="Visual motif connects to next beat.",
                camera="Slow push-in",
                audio="Score swell",
            ),
        )
        return Scene(
            title=scene.title,
            location=scene.location,
            beats=scene.beats,
            shots=shots,
        )

    def revise_script(self, script: Script, note: str) -> Script:
        """Produce a revision with a new thematic note and timestamp."""

        timestamp = datetime.utcnow().strftime("%Y-%m-%d")
        revised_theme = f"{script.theme} | Note: {note} ({timestamp})"
        return Script(
            title=script.title,
            logline=script.logline,
            theme=revised_theme,
            scenes=script.scenes,
        )

    def _build_opening(self, characters: Sequence[Character]) -> Scene:
        focus = characters[0] if characters else Character("Protagonist", "lead")
        beats = (
            f"Introduce {focus.name} in their ordinary world.",
            "Inciting incident disrupts the status quo.",
        )
        return Scene(title="Opening", location="City streets", beats=beats)

    def _build_midpoint(self, characters: Sequence[Character]) -> Scene:
        ally = characters[1] if len(characters) > 1 else Character("Ally", "support")
        beats = (
            f"{ally.name} reframes the mission.",
            "Plan escalates into the point of no return.",
        )
        return Scene(title="Midpoint", location="Hidden workshop", beats=beats)

    def _build_finale(self, characters: Sequence[Character]) -> Scene:
        rival = characters[2] if len(characters) > 2 else Character("Rival", "antagonist")
        beats = (
            f"Face off with {rival.name}.",
            "Resolve the thematic question with a decisive choice.",
        )
        return Scene(title="Finale", location="Skyline rooftop", beats=beats)
