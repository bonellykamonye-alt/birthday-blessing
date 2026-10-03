
import streamlit as st


st.title("🎁🎂 Awesome Gift From Bones 🎂🎁")
st.write("✨ Enter your name below to receive your special birthday/ day  blessing ✨")
verse="""Numbers 6:24-25
May the Lord bless you and keep you;
the Lord make his face shine on you and be gracious to you;
the Lord turn his face toward you and give you peace."""
name=st.text_input("ENTER YOUR NAME:")

if st.button("Submit"):
    st.balloons()
    if name =="Patience" or name == "Pashy" or name =="P":
        st.info(verse)
        st.success(f"Happy Birthday to {name}, be blessed")

    elif name == "James" or name == "Jamo":
     st.info(verse)
     st.success(f"happy birthday to {name}, be blessed")
    elif name == "JB" or name == "Hope" or name == "Anita":
     st.info(verse)
     st.success(f"{name},be blessed")
    elif name == "BONES" or "BONELLY":
     st.success(f"{name} ,you are great")
    elif name == "Myles" or " Prince" or "Claire":
     st.info(verse)
     st.success(f"{name}, hope you are doing well be blessed")
    else:
      st.error("Invalid name ")
    
