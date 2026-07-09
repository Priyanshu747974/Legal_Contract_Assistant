from app.core.interfaces.retriever import RetrieverInterface
from app.core.interfaces.prompt_builder_interface import PromptBuilderInterface
from app.core.interfaces.llm_interface import LLMInterface

class RAGServices:
    def __init__(self,retriever:RetrieverInterface,prompt_builder:PromptBuilderInterface,llm:LLMInterface, k: int = 5):
        self.retriever=retriever
        self.prompt_builder=prompt_builder
        self.llm=llm
        self.k=k

    def generate_answer(self, question: str) -> str:
        search_results = self.retriever.retrieve(question, self.k)
        prompt = self.prompt_builder.build_prompt(question,search_results)
        answer = self.llm.generate(prompt)
        return answer
    
    