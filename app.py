import streamlit as st
import re

def password_strength(password):
    """Evaluate the strength of the password."""
    length = len(password)
    if length < 8:
        return "Weak", "Password is too short. It should be at least 8 characters."
    
    if not re.search("[a-z]", password):
        return "Weak", "Password should contain at least one lowercase letter."
    
    if not re.search("[A-Z]", password):
        return "Weak", "Password should contain at least one uppercase letter."
    
    if not re.search("[0-9]", password):
        return "Weak", "Password should contain at least one digit."
    
    if not re.search("[@#$%^&+=]", password):
        return "Weak", "Password should contain at least one special character."
    
    return "Strong", "Your password is strong!"

# Streamlit app
st.title("Password Strength Meter")
st.write("Enter your password below to check its strength:")

password_input = st.text_input("Password", type="password")

if password_input:
    strength, message = password_strength(password_input)
    st.success(f"Password Strength: {strength}")
    st.info(message)
else:
    st.warning("Please enter a password to check its strength.")