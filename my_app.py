import streamlit as st

# Custom HTML for centered title and subtitle
st.markdown("""
    <div style='text-align: center; margin-top: 30px;'>
        <h1 style='margin-bottom: 0;'>Welcome to My System</h1>
        <h2 style='color: #61dafb; margin-top: 5px;'>by Sayed Codes</h2>
    </div>
""", unsafe_allow_html=True)

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# Function to show main app
def show_main_app():
    # Step 1
    a = st.text_input("Hi there what's up?👀")
    if a:
        st.success("I am happy to hear that you are doing well!😊")
        st.write("Thank you for sharing your feelings with me!💕")
        st.write("I am here to listen to you and support you!😉")
        st.write("I hope you have a great day ahead!")
        st.markdown("---")

        # Step 2
        b = st.text_input("what is your name?")
        if b:
            st.success("Nice to meet you, my friend!🙌")
            st.write("by the way nice name, bro/sis")
            st.write("My name is Sayed Hamza!❤️")
            st.write("Say the name of Sayed Hamza—and stay blessed and joyful!!😉")
            st.markdown("---")

            # Step 3
            sm = st.text_input("So, what brings you here?")
            if sm:
                st.write("'Oh wow, impressive! You're quite smart!😎'")
                st.write("-------------------------------------------------")
                st.success("Welcome to my virtual world of Sayed Hamza!🫶🏻")
                st.markdown("---")

                # Final Goodbye
                st.write("Okay!See you later,👍")
                st.write("That's all for today,my friend!")
                st.write("-----------------------------------")
                st.success("And yes,Do remember me in your prayers.'Goodbye🥰🫂'")
                st.markdown("---")

                # Logout
                if st.button("Logout"):
                    st.session_state.logged_in = False
                    st.rerun()

# Login screen
if not st.session_state.logged_in:
    username = st.text_input("Enter your username:")
    password = st.text_input("Enter your password:", type="password")
    login_button = st.button("Login")

    if login_button:
        if username == username and password == "2004":
            st.session_state.logged_in = True
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("hehe, wrong username or password!")

# Main app screen
if st.session_state.logged_in:
    show_main_app()
#  cd "C:\Users\Sayed Mohammad Hamza\OneDrive\文件\Python"
#  streamlit run my_app.py