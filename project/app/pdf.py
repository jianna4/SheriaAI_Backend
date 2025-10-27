from langchain_community.document_loaders import PyPDFLoader

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
import json

pdf_path = r"F:\Program Files\projects\sheria_AI\Sheria_backend\project\app\Labour Relations Act.pdf"
loader = PyPDFLoader(pdf_path)

docs = loader.load()
print(f"Loaded {len(docs)} documents from PDF.")


#coz it goes page by page,add this
full_text = ""
for page in pages:
    full_text += page.page_content + "\n"
#splitting the document
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
documents = splitter.split_documents(docs)

#saving as ajson file
json_data = [
    {"content": doc.page_content, "metadata": doc.metadata}
    for doc in documents
]
with open("chunks.json", "w", encoding="utf-8") as f:
    json.dump(json_data, f, indent=4, ensure_ascii=False)