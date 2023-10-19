# multipage_app.py
import streamlit as st

def home():
    st.title("Home Page")
    st.write("Welcome to the home page!")

def about():
    st.title("About Page")
    st.write("This is the about page. It provides information about the app.")

def contact():
    st.title("Contact Page")
    st.write("You can contact us on this page. Fill out the form below.")

def main():
    st.sidebar.title("Navigation")
    pages = {
        "Home": home,
        "About": about,
        "Contact": contact,
    }

    selection = st.sidebar.radio("Go to", list(pages.keys()))

    # Set query parameters to change the URL
    st.experimental_set_query_params(page=selection)

    # Execute the selected page function
    pages[selection]()

if __name__ == "__main__":
    main()
