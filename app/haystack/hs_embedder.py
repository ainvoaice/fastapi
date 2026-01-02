# # app/ai/embedder.py
# from haystack.components.embedders import SentenceTransformersTextEmbedder

# embedder = SentenceTransformersTextEmbedder(
#     model="sentence-transformers/all-MiniLM-L6-v2"
# )
# embedder.warm_up()


from haystack.components.embedders import SentenceTransformersDocumentEmbedder

embedder = SentenceTransformersDocumentEmbedder(
    model="sentence-transformers/all-MiniLM-L6-v2"
)
embedder.warm_up()
