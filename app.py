import streamlit as st 
from spello.model import SpellCorrectionModel

# Load the spell correction model
sp = SpellCorrectionModel(language='en')

# Ensure 'en.pkl' is the correct path to your model file
sp.load('en.pkl') 

# Streamlit App Title
st.title(" Spell Checker with Spello")

# Text area for user input
text_input = st.text_area("Enter your text here:", height=200)

# Button to check and correct text
if st.button("Check"):
    if text_input:
        # Correct the text using Spello
        correction_result = sp.spell_correct(text_input)
        
        # Display only the corrected text
        corrected_text = correction_result['spell_corrected_text']  # Extract corrected text
        st.write("### Corrected Text:")
        st.write(corrected_text)
    else:
        st.warning("Please enter some text to check.")
