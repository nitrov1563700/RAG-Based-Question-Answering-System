from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

def create_rag_chain(llm, retriever):
    prompt = ChatPromptTemplate.from_template(
        """You are an helpful assistant.
        Answer the question based on the context below.

        Context:
        {context}

        Question:
        {question}
        """
    )
    
    rag_chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough(),
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain