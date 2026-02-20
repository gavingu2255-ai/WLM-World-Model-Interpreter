"""
World Model Interpreter — v0.2
World Model Output → Dimensional Structure
"""

from .spatial import extract_spatial
from .temporal import extract_temporal
from .affordances import extract_affordances


def interpret(world_output):
    """
    Convert world-model output (video frame, segmentation, depth, etc.)
    into WLM dimensional structure.
    """
    spatial = extract_spatial(world_output)
    temporal = extract_temporal(world_output)
    affordances = extract_affordances(world_output)

    return {
        "objects": list(spatial.keys()),
        "spatial": spatial,
        "temporal": temporal,
        "affordances": affordances,
        "causal": [],  # v0.2 placeholder
    }
