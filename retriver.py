def create_retriever(vectore_store):
    return vectore_store.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 5, "lambda_mult": 0.5},
    )