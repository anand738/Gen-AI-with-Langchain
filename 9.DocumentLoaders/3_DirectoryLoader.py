from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader

loader = DirectoryLoader(
    path=r'9.DocumentLoaders\Books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()
# docs = loader.load()

# print(len(docs))
# print(docs[343].page_content)

for document in docs:
    print(document.metadata)

