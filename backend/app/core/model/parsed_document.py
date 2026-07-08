from dataclasses import dataclass, field
#a dataclass module automatically creates constructor, repr, eq methods
#so we can define the model with just variable names and types
 
@dataclass
class ParsedDocument:
    text: str
    tables: list=field(default_factory=list)
    images: list=field(default_factory=list)
    