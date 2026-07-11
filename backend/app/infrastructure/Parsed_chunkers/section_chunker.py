from app.core.interfaces.chunker import ChunkerInterface
from app.core.model.chunk import Chunk
from app.core.model.parsed_document import ParsedDocument
import re

class SectionChunker(ChunkerInterface):
    def chunk(self, document: ParsedDocument) -> list[Chunk]:
        clean_text = self._clean_text(document.text)
        sections = self._find_sections(clean_text)
        chunks = self._create_chunks(sections)
        return chunks

    def _clean_text(self, text: str) -> str:
        text = text.replace("\r\n", "\n")
        text = re.sub(r"\n{2,}", "\n\n", text)
        text = text.strip()
        return text
    
    def _find_sections(self, text: str) -> list[tuple[str, str]]:
        # Solves Problem 3: A flexible regex lookahead that splits by:
        # - Numbered headers (e.g. 1., 1.1, 1.1.1)
        # - Roman numerals (e.g. I., II., IV.)
        # - Named headings (e.g. Section 1, Article II, Clause 3.1, SECTION 4)
        pattern = r"(?=^(?:(?:Section|Article|ARTICLE|SECTION|Clause|CLAUSE)\s+(?:[a-zA-Z0-9]+(?:\.[0-9]+)*)|(?:[0-9]+(?:\.[0-9]+)*|\b[IVXLCDM]+\b)[\.\)]?)\s+)"
        
        split_text = re.split(pattern, text, flags=re.MULTILINE)
        sections = []
        for section in split_text:
            section = section.strip()
            # Solves Problem 1: correctly checks for empty strings or pure whitespace
            if section:  
                title = section.split("\n")[0].strip()
                # Solves Problem 2: appends to a list of tuples to keep duplicate headers intact
                sections.append((title, section))
        return sections
    
    def _create_chunks(self, sections: list[tuple[str, str]]) -> list[Chunk]:
        chunks = []
        for chunk_id, (title, content) in enumerate(sections):
            chunk = Chunk(
                chunk_id=chunk_id,
                text=content,
                metadata={
                    "section": title
                }
            )
            chunks.append(chunk)
        return chunks