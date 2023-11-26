from service.document.pdf_doc.pdf_doc import PDFDoc
from service.input.pdf_input.pdf_input import PDFInput
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma


pdf_input = PDFInput()
pdf_doc = PDFDoc()

pdf_doc.create_doc(pdf_input.from_file("./Fundamentals_of_Immigration_Law.pdf"))

docs = pdf_doc.chunk()

# load embeddings model
embedding_function = SentenceTransformerEmbeddings(model_name="all-mpnet-base-v2")

db = Chroma.from_documents(docs, embedding_function)

query = "What is an Alien?"
result = db.similarity_search(query)

print(result[0].page_content)