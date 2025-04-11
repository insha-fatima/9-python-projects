import streamlit as st

def main():
    st.title("My First Streamlit Website")
    st.write("Welcome to my website!🎉")

    st.sidebar.title("Navigation 📖")
    page = st.sidebar.selectbox("Choose a page", ["Home 🏡", "About 📝", "Contact 📱"])

    if page == "Home 🏡":
        st.write("This is the home page 🏡.")
        with st.form("my_form"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            submit_button = st.form_submit_button(label='Submit')
        if submit_button:
            st.write(f"Hello, {name}! Your email is {email}.")

    elif page == "About 📝":
        st.write("This is the about page.📝")
        with st.form("about_myself"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            age = st.text_input("Age")
            qualification = st.text_input("Qualification")
            skills = st.text_input("Skills")
            submit_button = st.form_submit_button(label='Submit')
        if submit_button:
            st.write(f"Name : {name}")
            st.write(f"Email : {email} ")
            st.write(f"Age : {age} ")
            st.write(f"Qualification : {qualification} ")
            st.write(f"Skills : {skills} ")
    
    elif page == "Contact 📱":
        st.write("This is the contact page 📱.")
        with st.form("contact"):
            cell_number = st.number_input("Cell Number")
            linkedin_account = st.text_input("Linkedin Account")
            dicord_account = st.text_input("Dicord Account")
            submit_button = st.form_submit_button(label='Submit')
        if submit_button:
            st.write("Contact me from here 👇🏻")
            st.write(f"Cell Number : {cell_number} ")  
            st.write(f"Linkedin Account : {linkedin_account} ")
            st.write(f"Dicord Account : {dicord_account} ")


if __name__ == "__main__":
    main()
