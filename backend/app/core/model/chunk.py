from dataclasses import dataclass, field

@dataclass
class Chunk:
    text: str
    chunk_id: int
    metadata: dict=field(default_factory=dict)