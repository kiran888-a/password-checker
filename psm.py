import re
import streamlit as st 

#page styling
st.set_page_config(page_title="Password Strength Checker", page_icon="🔑", layout="centered")
st.markdown("""
            <style>
            .main{text-align: center;}
            .stTextInput{width: 50%;, margin: 0 auto;}
            .stButton button{width: 50%;, background:blue;, color:white;,font-size:20px;}
            .stButton button:hover{background:darkblue;}
            </style>
            """, unsafe_allow_html=True)
#page tittle and description
st.title("🔒Password Strength Checker")
st.write("Enter your password to check its strength🔍")

#function to check password strength
def check_strength(password):
    score = 0
    feedback = []
    if len(password) >= 8:
        score += 1
    else:   
        feedback.append("❌Password must be at least 8 characters long.")
    
       
    if re.search(r"[A-Z]", password)  and re.search(r"[a-z]", password) :
         score += 1
    else:
        feedback.append("❌Password must contain both ""uppercase(A-Z) and lowercase(a-z)"".")
   
        
    if re.search(r"\d", password) :
        score += 1
    else:
        feedback.append("❌Password must contain at least one digit(0-9).")
    
    if re.search(r"[!@#$%&*]", password): 
        score += 1
    else:
        feedback.append("❌Password must contain at least one special character [!@#$%&*].")
    
    #display password strength feedback
    if score == 4:
        st.success("✅ Password is strong.")
    elif score == 3:
        st.info("🟡 Modrate password.")
    else:
        st.error("🔴"" Weak password."" Follow the instructions to make it strong.")
        if feedback:
            with st.expander("🔍improve your password"):
                for item in feedback:
                    st.write(item)


           

#input field for password
password = st.text_input("Enter your password:", type="password", help="Enter your password strong.🔒")
#button to check password strength
if st.button("Check Strength"):
    if password:
        check_strength(password)
        
    else:
        st.warning("Please enter a password first.")

    