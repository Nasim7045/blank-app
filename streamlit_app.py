import streamlit as st

# Page Configurations
st.set_page_config(page_title="Login Page", layout="centered")

# Dummy credentials
credentials = {
    'user1': 'password1',
    'user2': 'password2',
}

# Function for login verification
def login(user, password):
    if user in credentials and credentials[user] == password:
        return True
    else:
        return False

# Main function
def main():
    st.title('Hello, this is my first Streamlit APP')

    # User state management
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if st.session_state["logged_in"]:
        st.write("You have logged in.")
        if st.button("Logout"):
            st.session_state["logged_in"] = False
            st.experimental_rerun()
    else:
        # Login form
        st.subheader("Login Page")
        user = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if login(user, password):
                st.session_state["logged_in"] = True
                st.experimental_rerun()
            else:
                st.error("Invalid Username or Password")
        
        # Forgot password link
        if st.button("Forgot Password"):
            st.session_state["forgot_password"] = True
            st.experimental_rerun()

        # Forgot password page
        if "forgot_password" in st.session_state and st.session_state["forgot_password"]:
            st.subheader("Password Recovery")
            email = st.text_input("Enter your email for password recovery")
            if st.button("Submit"):
                st.write(f"Password recovery instructions have been sent to {email}")
                st.session_state["forgot_password"] = False

# Run the app
if __name__ == '__main__':
    main()
