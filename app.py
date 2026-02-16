import streamlit as st

books = [
  "Kumcho vulcho i kuma lisa",
  "Chervenata shapchica",
  "Tom i Jerry",
  "Pitur Pan",
  "Robinzon kruzo"
]  





st.title("Book checker app")
st.write("Enter the book title to check if it exists in the database.")

user_input = st.text_input("Book title")

if st.button("Check Book"):
  if user_input.strip() == "":
    st.warning("Please enter a book title.")
  elif user_input in books:
    st.success("The book exists in the database!")
  else:
    st.error("The book is NOT exists in the database")




  
  
