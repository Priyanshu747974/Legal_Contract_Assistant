from app.core.interfaces.prompt_builder_interface import PromptBuilderInterface
from app.core.model.search_result_vDB import SearchResult


class DefaultPromptBuilder(PromptBuilderInterface):

    PROMPT_TEMPLATE = """
You are a legal assistant.

Answer the user's question using ONLY the provided context.

If the answer cannot be found in the context, say:
"I could not find the answer in the provided documents."

Context:
--------------------
{context}
--------------------

Question:
{question}

Answer:
"""

    def build_prompt(
        self,
        question: str,
        search_results: list[SearchResult]
    ) -> str:

        context = self._build_context(search_results)

        return self._create_prompt(context, question)

    def _build_context(
        self,
        search_results: list[SearchResult]
    ) -> str:

        context_parts = []

        for result in search_results:

            chunk = result.embedding.chunk

            context_parts.append(
                f"[Chunk {chunk.chunk_id}]\n{chunk.text}"
            )

        return "\n\n".join(context_parts)

    def _create_prompt(
        self,
        context: str,
        question: str
    ) -> str:

        return self.PROMPT_TEMPLATE.format(
            context=context,
            question=question
        )