# app/service/ser_report_assistant.py
import os
from haystack.nodes import EmbeddingRetriever
from haystack.nodes import OpenAIAnswerGenerator
from haystack.pipelines import Pipeline
from haystack import Document
from .hs_store import document_store

class ReportAssistantService:
    def __init__(self):
        # Retriever using SentenceTransformers embeddings
        self.retriever = EmbeddingRetriever(
            document_store=document_store,
            embedding_model="sentence-transformers/all-MiniLM-L6-v2",
            use_gpu=True
        )

        # OpenAI LLM node
        self.llm = OpenAIAnswerGenerator(
            model_name="gpt-4",
            api_key=os.getenv("OPENAI_API_KEY")
        )

        # Pipeline: Retriever -> LLM
        self.pipeline = Pipeline()
        self.pipeline.add_node(component=self.retriever, name="Retriever", inputs=["Query"])
        self.pipeline.add_node(component=self.llm, name="AnswerGenerator", inputs=["Retriever"])

    async def answer_question(self, query: str, top_k_retriever: int = 10):
        """
        Receive a natural-language question and return an answer
        from the embedded reports.
        """
        # Run Haystack pipeline
        result = self.pipeline.run(
            query=query,
            params={"Retriever": {"top_k": top_k_retriever}}
        )

        # The OpenAIAnswerGenerator returns answers in 'answers'
        answers = result.get("answers", [])
        if answers:
            return answers[0].answer
        return "No answer found."
