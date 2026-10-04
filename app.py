import streamlit as st
from src.matcher import find_books
from src.llm import recommend
from src.planner import make_plan

st.set_page_config(page_title="First Book Picker", page_icon="📖")

st.title("📖 First Book Picker")
st.write(
    "Scared of picking the wrong first book? Don't be. "
    "Your first book doesn't decide your reading life. "
    "Tell me a bit about you and I'll suggest short, easy, affordable books."
)

taste = st.text_input("What do you like? (movies/shows/moods/genres)",placeholder="eg. fast thrillers, funny stories, spooky, gentle")
minutes = st.slider("How many minutes in a day can you read?", 5, 60, 20)
max_pages = st.slider("Longest book you're okay with (pages)", 50, 300, 200)
free_only = st.checkbox("Show only free books?")

if st.button("Find my first book"):
    if taste.strip() == "":
        st.warning("Please tell me what you like first.")
    else:
        books = find_books(taste, max_pages, free_only)
        if len(books) == 0:
            st.error("No books matched. Try a longer page limit or untick 'free only'.")
        else:
            with st.spinner("Thinking about the best books for you..."):
                answer = recommend(taste, books)
            st.session_state["books"] = books
            st.session_state["answer"] = answer
            st.session_state["minutes"] = minutes

if "answer" in st.session_state:
    st.subheader("Your picks")
    st.write(st.session_state["answer"])

    st.subheader("Plan your reading")
    books = st.session_state["books"]
    titles = [book["title"] for book in books]
    chosen_title = st.selectbox("Which book do you want to try?", titles)

    for book in books:
        if book["title"] == chosen_title:
            chosen_book = book

    plan = make_plan(chosen_book["pages"], st.session_state["minutes"])

    st.write(f"**{chosen_book['title']}** has {chosen_book['pages']} pages.")
    st.write(f"📅 Read about **{plan['pages_per_day']} pages a day**.")
    st.write(f"🏁 You'll finish in about **{plan['days_needed']} days** "
             f"(around {plan['finish_date'].strftime('%d %b %Y')}).")
    st.info(
        f"Give it until page {plan['bail_out_page']}. "
        "If it's not clicking, switch books guilt-free. That's not failing, that's choosing."
    )
