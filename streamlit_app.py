import streamlit as st
import pyrebase
import firebase_admin
from firebase_admin import credentials, auth
from firebase_admin import initialize_app

# Firebase Admin SDK credentials (from your JSON file)
cred = credentials.Certificate({
    "type": "service_account",
    "project_id": "t7-securities-database",
    "private_key_id": "29200d5431bdc51b404c298164034aaa5a3a5270",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDa9owU+m8nqLpP\n0bNfBINLsC7L/0Da/hs6OywFDoWGlb7LI/tBaCrxnE3N+dtfo6vwIXaUV3SRUjWk\nNpFdRyIjOJXxAcKGHdHP6TsYR4tD9LFqof7FKz7ykzgv67+oVWKpsPWxWhOnZqO+\ndJ7Qrd2OTxF3I/HeVOnO1QNk7aXQ9dxUtu5BrP+25tPLQXEoijwmi6A5fZveIBd/\nHkLQHWUOdwCxU0PZwbMzn/Js4DnDlWRCwLrESAAe6+8qgvW4kBlZnWsusYwA6wVh\ngqY2sroph8TVmKkI1TvgY5hL442QNVh+pjRWspOdonqoz1SPpGHvwx1moxsxnu3A\n4girhiyvAgMBAAECggEAQNu71bDywPAZM/B9Lb2D+KT4z6NNvjB7ty101hCdm6Z6\ni+ieEZs98TBn2YXTpcow8WGwIrOfCzarPfeN6m/aHE20GF35lUl67xd6UjBK/7eY\n3+mZMiUjsa3K/GLb9AxKu9H3jO+OF81u3kjkDBMcJ/2iwkQq7jz/vqzZIwnDzpeg\nnyEMtZrVQ76H8T4q8MV+CodCiOhVSA4d6Sy3v4W605qIbg8ejlQblkEc/VHzggwW\nXS0uyVi4/Rtuz11fc/pH3ViphXHKgd8Yu+xFUuUB3VREivz0cArdqUn8orks6pfu\nsMs+WTvFLX/m2n9dVI1ckiJw5uKVL3xm8hyZI9VOZQKBgQD4SxsHi8k7qSt7urID\ndrbELl0vS6Jpopnm8eDW8StPKf0kDWT/iZqAcqK8vmN1FzPKgC986Q00ms1Ge7cz\nAgY9tCoqF05nTRDlfxlhkHunosVkfRJ29ro+Nu9i/9Lf7v7CcIrglBrZH6FHJZpN\nPaeLN+5s6HOjVR5JmTV51vCIowKBgQDhwmNm6oot2S7MC0irUD82RQiSnuRW1Dcw\n7HiMSfR2E6s91+NrMK+VT8J2mpux5rHQZFEIY0OSx5ZhsqM8+acQQyNQaec3Mhmd\nIZyVZmdUAq+ZZcptldz2GoAz/tKTuDbJbG4rHe76NBagRSoLuCeC8E/szRRBT5MN\nPQl6vzcQhQKBgG5bq4riFbI/0cTvyTmC5V8zIFXqLyj2jaM5dO70SISqLAp/LZnq\nxlI7IZv0n24mvu1Npk3FpAnymDSwvk+cobuBPZBxxXZiqZTnthdISb3LuiKc+L0J\nkuQeNK5y+H5x0qgHr6J8EabZySw/SWL1eWeGl6Gue99n8MtTnpIl98kzAoGAdq6v\nfQotzD6RqHkCIfWU1Z3jDNl1JuR3g0O9d9rlJjHe4yschlxY4gDFNX6//P1PW0Nx\nihxNCNveBcxYnpSMLDNvXDXgdJbk+kMSQ0RLa9HhqJ3nlkajm8mAvlTnNPsx6iAT\npp0c5fH+NxFFMlYEh4R4L//79v2zS9Fbq2jctNUCgYAKj840NTTyodmwVAKJBm8H\ntXgNHyvQgXr1lBcgHtkaXHEXhIxGavwOoDMp5QMT35JLVk3RjlJFnuySL/lVywHz\nozkHd8AOFbRW+Lda0IanULrjVf9wmzd9F+LIVAgShFrZTj2buw8ASeZW5RWXQoi/\nnei5LNzpJ4RvVCgXth4dFA==\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-ztu4u@t7-securities-database.iam.gserviceaccount.com",
    "client_id": "103402632275992014907",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-ztu4u%40t7-securities-database.iam.gserviceaccount.com"
})

# Initialize Firebase Admin SDK only if not already initialized
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

# Pyrebase setup for client-side operations
firebase_config = {
    "apiKey": "AIzaSyB0gbs0qPbl4fZkIVBZ6_UQwZxKV0uPwAk",
    "authDomain": "t7-securities-database.firebaseapp.com",
    "databaseURL": "https://t7-securities-database.firebaseio.com",
    "projectId": "t7-securities-database",
    "storageBucket": "t7-securities-database.appspot.com",
    "messagingSenderId": "278676976057",
    "appId": "1:278676976057:web:182f8c1110d96f9d7f4668",
    "measurementId": "G-DNJN5ZKZEP"
}

firebase = pyrebase.initialize_app(firebase_config)
auth_client = firebase.auth()

# Authentication functions for login and registration
def login_user(email, password):
    try:
        user = auth_client.sign_in_with_email_and_password(email, password)
        return user
    except:
        return None

def register_user(email, password):
    try:
        auth_client.create_user_with_email_and_password(email, password)
        return True
    except:
        return False

def main():
    st.title('Firebase Authentication with Streamlit')

    # Initialize session states
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    if "register" not in st.session_state:
        st.session_state["register"] = False

    if st.session_state["logged_in"]:
        st.write("You have logged in.")
        if st.button("Logout"):
            st.session_state["logged_in"] = False
            st.rerun()

    elif st.session_state["register"]:
        st.subheader("Register a New Account")
        email = st.text_input("Enter your email")
        password = st.text_input("Enter your password", type="password")
        confirm_password = st.text_input("Confirm your password", type="password")

        if st.button("Register"):
            if password == confirm_password:
                if register_user(email, password):
                    st.success("Registration successful! You can now log in.")
                    st.session_state["register"] = False
                    st.rerun()
                else:
                    st.error("Registration failed. Try again.")
            else:
                st.error("Passwords do not match. Please try again.")

        if st.button("Back to Login"):
            st.session_state["register"] = False
            st.rerun()

    else:
        st.subheader("Login")
        email = st.text_input("Enter your email")
        password = st.text_input("Enter your password", type="password")

        if st.button("Login"):
            user = login_user(email, password)
            if user:
                st.session_state["logged_in"] = True
                st.rerun()
            else:
                st.error("Invalid email or password")

        if st.button("Sign Up"):
            st.session_state["register"] = True
            st.rerun()

if __name__ == '__main__':
    main()
