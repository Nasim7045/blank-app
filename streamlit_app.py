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
    return credentials.get(user) == password

# Function for registering new users
def register(user, password):
    if user in credentials:
        return False
    credentials[user] = password
    return True

# Main function
def main():
    st.title('Hello, this is my first Streamlit APP')

    # Initialize session states
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    if "forgot_password" not in st.session_state:
        st.session_state["forgot_password"] = False
    if "register" not in st.session_state:
        st.session_state["register"] = False

    # If the user is logged in
    if st.session_state["logged_in"]:
        st.write("You have logged in.")
        if st.button("Logout"):
            st.session_state["logged_in"] = False
            st.session_state["forgot_password"] = False
            st.session_state["register"] = False

    # Forgot password page
    elif st.session_state["forgot_password"]:
        st.subheader("Password Recovery")
        email = st.text_input("Enter your email for password recovery")
        if st.button("Submit"):
            st.success(f"Password recovery instructions have been sent to {email}")
            st.session_state["forgot_password"] = False

    # Registration page
    elif st.session_state["register"]:
        st.subheader("Register a New Account")
        new_user = st.text_input("Enter a new username")
        new_password = st.text_input("Enter a new password", type="password")
        confirm_password = st.text_input("Confirm your password", type="password")

        if st.button("Register"):
            if new_password == confirm_password:
                if register(new_user, new_password):
                    st.success("Registration successful! You can now log in.")
                    st.session_state["register"] = False
                else:
                    st.error("Username already exists. Please choose another.")
            else:
                st.error("Passwords do not match. Please try again.")

        if st.button("Back to Login"):
            st.session_state["register"] = False

    # Login form
    else:
        st.subheader("Login Page")
        user = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if login(user, password):
                st.session_state["logged_in"] = True
            else:
                st.error("Invalid Username or Password")

        # Forgot password link
        if st.button("Forgot Password"):
            st.session_state["forgot_password"] = True

        # Sign-up link
        if st.button("Sign Up"):
            st.session_state["register"] = True

# Run the app
if __name__ == '__main__':
    main()
