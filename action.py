#!/usr/bin/env python
import os
from pathlib import Path
from rdflib import Graph

GITHUB_WORKSPACE = Path("/github/workspace")
GLOBS = os.getenv("GLOBS")
GLOBS = {k: v for k, v in (i.split(":") for i in GLOBS.split("|"))}
G = Graph()

for glb, fmt in GLOBS.items():
    for p in GITHUB_WORKSPACE.rglob(glb):
        if p.is_file():
            try:
                G.parse(p, format=fmt)
            except Exception as e:
                print(f"failed to parse {p}: {e}")

G.serialize(GITHUB_WORKSPACE / "all-triples.ttl", format="ttl")
