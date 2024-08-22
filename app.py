import streamlit as st

# Title of the app
st.title("🎓 Graduation Wishes")

# Add a header for personalization
st.header("A Special Message for a Wonderful Graduate")

# Graduation message
message = """
Dear Binish (Sisteri),

Congratulations on your graduation! 🎉 You've worked so hard to reach this milestone, and your dedication has truly paid off. 
This is just the beginning of a bright and successful future. Remember to always believe in yourself and pursue your dreams with passion and determination.

Wishing you all the best as you embark on this exciting new chapter in your life!

With warmest wishes,

Shahzaib
"""

# Display the message
st.write(message)

# Add a celebration emoji or image
st.image("https://media.giphy.com/media/26ufdipQqU2lhNA4g/giphy.gif")

# Footer
st.text("P.S. The future is yours to create! 🌟")

st.markdown("---")
st.image("she_graduated_with_3_04_cgpa.jpeg")
st.markdown("---")
