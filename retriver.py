def create_retriever(vectore_store):
    return vectore_store.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 5, "lambda_mult": 0.5},
    )

def similarity_search(vector_store, query):
    result = vector_store.similarity_search_with_scores(query, k=5)
    return result