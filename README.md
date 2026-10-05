# 📖 VibeLivre

**A low-pressure first-book picker for people who want to start reading but are scared of picking the wrong book.**

> Built for the [Hacktoberfest Weekend Challenge: Build for a Friend](https://dev.to/challenges/hacktoberfest-weekend-2026-10-01)
> 
> My submission : https://dev.to/alsopayalll/vibelivre-a-low-pressure-first-book-picker-built-with-gemma-19p3
> 
> Project started on October 2, 2026.

---

## Why I built this

A friend of mine wanted to get into reading, but she was worried that one boring first book would convince her she's "not a reader", so she never started. There were also too many choices.

VibeLivre removes that pressure. You tell it what you like, and it suggests a few short, easy, affordable books, then turns your pick into a simple reading plan.

> You don't have to become a reader before you start reading. You just need to find one book that makes you want to turn the next page.

---

## What it does

You tell VibeLivre:

- what kind of vibe or genre you like
- the longest book (in pages) you're okay with
- how many minutes a day you can read
- whether you want only free books

It then gives you:

- **3 book suggestions** from a curated list, each with a short friendly reason
- **A reading plan:** pages per day and an estimated finish date
- **The 30-page rule:** give a book 30 pages, and if it's not clicking, it's okay to switch

---

## How it works

The AI never invents books. Instead of asking an LLM to recommend anything, VibeLivre works as a small pipeline:

1. **Curated book list** (`data/books.csv`): each book has a title, author, page count, cost (free or cheap), vibe tags and a short spoiler-free hook.
2. **Python filters and scores** (`src/matcher.py`): books above the page limit are removed, "free only" removes paid books, and the rest are scored by how well their vibes and hooks match what the user typed.
3. **Gemma picks from the shortlist** (`src/llm.py`): only the filtered books are sent to the model. It chooses 3 and explains why each might suit the reader. Since it can only choose from books already in the list, it can't make anything up.
4. **Reading planner** (`src/planner.py`): pages per day → number of days → estimated finish date.

---

## Tech stack

| Part | Tool |
|---|---|
| Open-weight model | **Gemma** (`gemma3:4b`) |
| Local inference | **Ollama** |
| Language | **Python** |
| Interface | **Streamlit** |
| Data | **CSV** |

---

## Project structure

```
VibeLivre/
├── data/
│   └── books.csv        # the curated book list
├── src/
│   ├── __init__.py
│   ├── matcher.py       # filtering and scoring
│   ├── llm.py           # Gemma calls through Ollama
│   └── planner.py       # reading plan math
├── app.py               # Streamlit interface
├── test.py              # quick terminal test
├── requirements.txt
└── README.md
```

---

## Run it locally

### 1. Install Ollama and pull the model

Download Ollama from [ollama.com](https://ollama.com), then run:

```bash
ollama pull gemma3:4b
```

(On a low-RAM laptop you can use `gemma3:1b` instead. Change the model name in `src/llm.py` to match.)

### 2. Clone the repo

```bash
git clone https://github.com/alsopayalll/VibeLivre.git
cd VibeLivre
```

### 3. Create a virtual environment and install packages

```bash
python -m venv .venv
```

Activate it:

- **Windows (PowerShell):** `.venv\Scripts\Activate.ps1`
- **Mac / Linux:** `source .venv/bin/activate`

Then install the requirements:

```bash
pip install -r requirements.txt
```

### 4. Start the app

Make sure Ollama is running, then:

```bash
streamlit run app.py
```

The app opens in your browser, usually at `http://localhost:8501`.

### Quick test without the UI (optional)

```bash
python test.py
```

---

## Demo
🔗 **Demo video:** https://drive.google.com/drive/folders/1NGdoS5f1mYRjDPJ1m3EUHWErVTbqPgBv?usp=sharing

🔗 **Live link:** https://vibelivre.streamlit.app/
The live link runs on Streamlit's free hosting, which cannot run Ollama, so the hosted version can't use Gemma. The full experience, with Gemma running on your own machine, works when you follow the steps above.

---

## Why open-source AI?

- **Private:** with Gemma running locally through Ollama, what someone types never goes to a company's server.
- **Free to run:** no API key and no billing.
- **Under my control:** I decided exactly how the model behaves (pick only from my list, keep it short, be warm) and could switch to a smaller model when the bigger one was too slow.

---

## Notes on the data

- Books marked `free` are assumed to be in the public domain (Project Gutenberg / Standard Ebooks). Copyright rules vary by country, so please check availability where you live.
- Page counts are approximate and vary by edition.
- The list mixes books I've read myself with suggestions from the internet. I checked each entry and wrote the tags and hooks myself.

---

## Known limitations

- The matcher uses keyword matching, so it only matches exact words (for example, "thrillers" won't match "suspense").
- Gemma can be slow on laptops without a GPU.
- The book list is small compared to a real catalogue.

---

## What I'm planning to build next:

- A daily check-in with a spoiler-free recap of where you left off
- A "this book isn't clicking" rescue feature that suggests an easier replacement
- Smarter matching that understands meaning, not just exact words

---

## Credits

- [Gemma](https://ai.google.dev/gemma) by Google
- [Ollama](https://ollama.com)
- [Streamlit](https://streamlit.io)
- Book suggestions from Reddit threads, Goodreads lists and Project Gutenberg(and some of my personal recommendations!)

---


Built during the Hacktoberfest Weekend Challenge window (Oct 2 to 5, 2026). Any commits made after the submission deadline will be noted here.
