from haystack_integrations.document_stores.pgvector import PgvectorDocumentStore
from haystack import Document

document_store = PgvectorDocumentStore(
    embedding_dimension=384,
    vector_function="cosine_similarity",
    recreate_table=True,
    search_strategy="hnsw",
)

# # Example documents (replace with your CSV row concatenated content + embeddings)
# docs = [
#     Document(content="Date: 1/23/2025, Lead Owner: Selena Doyle, ...", embedding=[0.1]*1536),
#     Document(content="Date: 5/23/2025, Lead Owner: Kelsey Mosley, ...", embedding=[0.3]*1536)
# ]

# document_store.write_documents(docs)
# print("Total docs in PGVector:", document_store.count_documents())



# from haystack_integrations.document_stores.pgvector import PgvectorDocumentStore
# from haystack import Document

# from app.config import get_settings_singleton
# settings = get_settings_singleton()

# document_store = PgvectorDocumentStore(
#     embedding_dimension=1536,
#     vector_function="cosine_similarity",
#     recreate_table=True,
#     search_strategy="hnsw",
# )

# document_store.write_documents([
#     Document(content="This is first", embedding=[0.1]*1536),
#     Document(content="This is second", embedding=[0.3]*1536)
#     ])
# print(document_store.count_documents())