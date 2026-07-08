from app.core.interfaces.chunker import ChunkerInterface
from app.core.model.chunk import Chunk
from app.core.model.parsed_document import ParsedDocument
import re

class SectionChunker(ChunkerInterface):
    def chunk(self, document: ParsedDocument)-> list[Chunk]:
        clean_text = self._clean_text(document.text)
        sections = self._find_sections(clean_text)
        chunks = self._create_chunks(sections)
        return chunks

    def _clean_text(self, text: str) -> str:
        text = text.replace("\r\n", "\n")
        text = re.sub(r"\n{2,}", "\n\n", text)
        text = text.strip()
        return text
    
    def _find_sections(self,text: str)->dict:
        pattern = r"(?=^\d+\.\s+.*)"
        split_text = re.split(pattern, text, flags=re.MULTILINE)
        sections = {}
        for index, section in enumerate(split_text):
            section = section.strip()
            if section != " ":
                title = section.split("\n")[0]
                sections[title] = section
        return sections
    
    def _create_chunks(self, sections: dict) -> list[Chunk]:
        chunks = []
        for chunk_id, (title, content) in enumerate(sections.items()):
            chunk = Chunk(
                chunk_id=chunk_id,
                text=content,
                metadata={
                    "section": title
                }
            )
            chunks.append(chunk)
        return chunks