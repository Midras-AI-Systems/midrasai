import importlib.util

__all__ = []

if importlib.util.find_spec("qdrant_client"):
    from midrasai.vectordb._qdrant import AsyncQdrant, Qdrant

    _, __ = Qdrant, AsyncQdrant  # Redundant alias for F401

    __all__.extend(["Qdrant", "AsyncQdrant"])

# Check for AstraDB support
if importlib.util.find_spec("astrapy"):
    from midrasai.vectordb._astradb import AstraDB

    _ = AstraDB  # Redundant alias for F401

    __all__.extend(["AstraDB"])
