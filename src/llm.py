import ollama
gmodel = "gemma3:4b"   

def recommend(taste, books):
    book_lines = ""
    for book in books:
        book_lines = book_lines + (
            f"- {book['title']} by {book['author']} "
            f"({book['pages']} pages, {book['cost']}): {book['hook']}\n"
        )

    prompt = f"""You are a warm, encouraging reading guide for someone who is nervous about picking the wrong first book of their reading journey. The reader's taste is {taste}
    Your task is to choose exactly 3 books, ONLY from this list. Do not mention a book that is not in the list: {book_lines}
    For each book, write the title and one friendly sentence on why this reader might enjoy it.Do not spoil the story.End with one short, reassuring line: their first book does not decide their reading life, and it is fine to quit after 30 pages and try another."""

    response = ollama.chat(model=gmodel, messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]