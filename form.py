import streamlit as st
import pandas as pd
import os

# File path to store contact messages
contact_file = 'contact_messages.csv'


# --- Functions to render different pages ---
def show_home_page():
    st.title("Welcome to PZ MEER Institute")
    st.subheader("About Us")
    st.write("""
        Our Institute is dedicated to providing quality education and professional training.
        We offer a wide range of programs to help you grow and succeed in your career.
    """)
    st.subheader("Our Mission")
    st.write("""
        To empower students with knowledge, skills, and experiences that will lead to
        success in their personal and professional lives.
    """)
    st.subheader("Our Values")
    st.write("""
        - Integrity
        - Innovation
        - Excellence
        - Respect
        - Diversity
    """)


def show_courses_page():
    st.title("Our Courses")
    st.subheader("Available Programs")

    # List of courses
    courses = [
        {"course_name": "Data Science", "duration": "6 Months", "fee": "Rs5000",
         "details": "Learn data analysis, machine learning, and AI."},
        {"course_name": "Web Development", "duration": "3 Months", "fee": "Rs3000",
         "details": "Become proficient in HTML, CSS, JavaScript, and frameworks like React."},
        {"course_name": "Digital Marketing", "duration": "4 Months", "fee": "Rs2500",
         "details": "Understand SEO, social media marketing, and online advertising."},
        {"course_name": "Business Management", "duration": "1 Year", "fee": "Rs7000",
         "details": "Get equipped with the skills to manage and lead businesses."}
    ]

    for course in courses:
        st.write(f"**{course['course_name']}**")
        st.write(f"Duration: {course['duration']}")
        st.write(f"Fee: {course['fee']}")
        st.write(f"Details: {course['details']}")
        st.write("---")


def show_admission_page():
    st.title("Admission Form")
    st.write("Fill out the form to apply for admission.")

    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    course = st.selectbox("Select Course",
                          ["Data Science", "Web Development", "Digital Marketing", "Business Management"])

    # Function to append admission data to a CSV file
    if st.button("Submit Application"):
        if name and email and phone:
            st.success(f"Thank you, {name}! Your application for the {course} course has been submitted.")
        else:
            st.error("Please fill out all fields.")


def show_contact_page():
    st.title("Contact Us")
    st.write("Have any questions? Reach out to us!")

    # Contact form
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    # Load existing contact data if the file exists
    if os.path.exists(contact_file):
        contact_data = pd.read_csv(contact_file)
    else:
        contact_data = pd.DataFrame(columns=["Name", "Email", "Message"])

    # Function to append new contact data
    def append_contact_data(name, email, message):
        new_data = pd.DataFrame([[name, email, message]], columns=["Name", "Email", "Message"])
        updated_data = pd.concat([contact_data, new_data], ignore_index=True)
        updated_data.to_csv(contact_file, index=False)

    # Handle form submission
    if st.button("Send Message"):
        if name and email and message:
            append_contact_data(name, email, message)  # Append data to CSV file
            st.success(f"Thank you for reaching out, {name}. We will get back to you soon!")
        else:
            st.error("Please fill out all fields.")



# --- Main Menu ---
def main():

    st.sidebar.title("PZ MEER INSTITUTE")
    page = st.sidebar.radio("Select Page", ["Home", "Courses", "Admission", "Contact"])

    if page == "Home":
        show_home_page()
    elif page == "Courses":
        show_courses_page()
    elif page == "Admission":
        show_admission_page()
    elif page == "Contact":
        show_contact_page()


# Run the app
if __name__ == "__main__":
    main()
