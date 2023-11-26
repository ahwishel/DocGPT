from service.document.pdf_doc.pdf_doc import PDFDoc
from service.input.pdf_input.pdf_input import PDFInput
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma
from langchain.document_loaders import PyPDFLoader
# from langchain.chat_models import ChatOpenAI

# server_url = "http://localhost:1234/v1"
#
# chat = ChatOpenAI(
#     model="text-davinci-003",
#     openai_api_key="YOUR_API_KEY",
#     openai_api_base=server_url,
# )
#

pdf_input = PDFInput()
pdf_doc = PDFDoc()

pdf_doc.create_doc(PyPDFLoader("./Fundamentals_of_Immigration_Law.pdf"))

docs = pdf_doc.chunk()

# load embeddings model
embedding_function = SentenceTransformerEmbeddings(model_name="all-mpnet-base-v2")

db = Chroma.from_documents(docs, embedding_function)

retriever = db.as_retriever()

relevant_docs = retriever.get_relevant_documents("What is an Alien?")

print(relevant_docs[0])


# query = "What is an Alien?"
# result = db.similarity_search(query)
#
# print(result[0].page_content)

