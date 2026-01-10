"""Core story primitives for the agentic director."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable


@dataclass(frozen=True)
class Character:
    """A story character with a name and role."""

    name: str
    role: str


@dataclass(frozen=True)
class Shot:
    """A cinematic shot description."""

    name: str
    description: str
    camera: str
    audio: str


@dataclass(frozen=True)
class Scene:
    """A single scene with location, beats, and shots."""

    title: str
    location: str
    beats: tuple[str, ...]
    shots: tuple[Shot, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class Script:
    """A script consisting of scenes and overarching themes."""

    title: str
    logline: str
    theme: str
    scenes: tuple[Scene, ...]

    def beat_sheet(self) -> list[str]:
        """Flatten beats across scenes for quick outlining."""

        return [beat for scene in self.scenes for beat in scene.beats]

    def summarize(self) -> str:
        """Return a short summary of the script."""

        scene_titles = ", ".join(scene.title for scene in self.scenes)
        return f"{self.title}: {self.logline} Themes: {self.theme}. Scenes: {scene_titles}."


def format_shots(shots: Iterable[Shot]) -> str:
    """Format shots into a readable string for quick CLI output."""

    lines = []
    for index, shot in enumerate(shots, start=1):
        lines.append(
            "\n".join(
                [
                    f"  Shot {index}: {shot.name}",
                    f"    Camera: {shot.camera}",
                    f"    Description: {shot.description}",
                    f"    Audio: {shot.audio}",
                ]
            )
        )
    return "\n".join(lines)
