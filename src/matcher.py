import csv
def load_books():
    books = []
    with open("data/books.csv", encoding="utf-8") as file:
        reader = csv.DictReader(file)   
        for row in reader:
            row["pages"] = int(row["pages"]) 
            books.append(row)
    return books

def find_books(taste, max_pages=250, free=False, n=5):
    books = load_books()
    taste_words = taste.lower().split()

    scored_books = []

    for book in books:
        if book["pages"] > max_pages:
            continue
        if free and book["cost"] != "free":
            continue

        book_text = (book["vibes"] + " " + book["hook"]).lower()
        score = 0
        for word in taste_words:
            word = word.strip(".,!?")        
            if len(word) < 4:                  
                continue
            if word in book_text:
                score = score + 1           
        scored_books.append((score, book))

    scored_books.sort(key=lambda x: x[0], reverse=True)
    best = []
    for score, book in scored_books[:n]:
        best.append(book)
    return best