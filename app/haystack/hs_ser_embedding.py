from haystack_integrations.document_stores.pgvector import PgvectorDocumentStore
from haystack import Document

class EmbeddingService:
    def run(self):
        store = PgvectorDocumentStore(
            embedding_dimension=1536,
            vector_function="cosine_similarity",
            recreate_table=False,
            search_strategy="hnsw",
        )

        docs = [
            Document(content="This is first", embedding=[0.1] * 1536),
            Document(content="This is first", embedding=[0.1] * 1536),
            Document(content="This is first", embedding=[0.1] * 1536),
            Document(content="This is second", embedding=[0.3] * 1536),
        ]

        store.write_documents(docs)
        return store.count_documents()
