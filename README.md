# TUCAL

TUCAL (Temporal Unity Core Abstraction Language) is a lightweight toolkit for building
agentic, multimodal story directors. This starter package focuses on an autonomous director
persona that produces structured movie outlines, scene beats, and shot lists.

## What it includes

- **DirectorAgent**: Generates a three-act outline and shot list from a logline.
- **Story models**: Typed primitives for characters, scenes, shots, and scripts.
- **CLI**: A command-line interface to quickly prototype an agentic director output.

## Quick start

```bash
python -m tucal.cli "Neon Horizon" "A courier discovers a memory map" "Identity is mutable" \
  --character "Lena:lead" --character "Sol:ally" --character "Wraith:antagonist"
```

The CLI prints a summary, scene beats, and a directed shot list for each scene.
