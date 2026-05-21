import pytesseract
from pdf2image import convert_from_path
from langchain_community.document_loaders import PyPDFLoader, UnstructuredWordDocumentLoader, UnstructuredPowerPointLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def process_with_ocr(file_path):
    """For scanned PDFs with no selectable text"""
    images = convert_from_path(file_path)
    full_text = ""
    for image in images:
        text = pytesseract.image_to_string(image)
        full_text += text
    doc = Document(page_content=full_text, metadata={"source": file_path})
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=600,
        chunk_overlap=120,
        separators=["\n\n", "\n", ".", " ", ""]
    )
    return splitter.split_documents([doc])

def process_document(file_path):
    if file_path.endswith('.pdf'):
        loader = PyPDFLoader(file_path)
    elif file_path.endswith('.docx'):
        loader = UnstructuredWordDocumentLoader(file_path)
    elif file_path.endswith('.pptx'):
        loader = UnstructuredPowerPointLoader(file_path)
    elif file_path.endswith('.txt'):
        loader = TextLoader(file_path)
    else:
        return []

    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=600,
        chunk_overlap=120,
        separators=["\n\n", "\n", ".", " ", ""]
    )
    return splitter.split_documents(docs)
