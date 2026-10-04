from src.matcher import find_books
from src.llm import recommend

taste = "want to read something light that doesnt exhaust me much and is interesting"

books = find_books(taste, 250, False)
print("Finding you your perfect first book...")
print(recommend(taste, books))