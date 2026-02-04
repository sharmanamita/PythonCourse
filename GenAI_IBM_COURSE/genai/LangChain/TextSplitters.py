from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter

text = """Paragraph one. Sentence two. This is a long document that needs splitting.


New paragraph with more content. Let's see how different splitters handle this text."""

# CharacterTextSplitter - cuts anywhere
char_splitter = CharacterTextSplitter(chunk_size=50, chunk_overlap=10)
char_chunks = char_splitter.split_text(text)
print("Character chunks:", [c for c in char_chunks])
# Might get: [50, 50, ...] - cuts mid-sentence

# Recursive - respects structure
rec_splitter = RecursiveCharacterTextSplitter(chunk_size=50, chunk_overlap=0)
rec_chunks = rec_splitter.split_text(text)
print("Recursive chunks:", [c for c in rec_chunks])