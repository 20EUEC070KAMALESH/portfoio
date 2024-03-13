import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/

def main():
    # Inject custom CSS
    st.markdown(
        """
        <style>
            body {
                background-color: #f0f0f0; /* Light gray background */
            }
        </style>
        """,
        unsafe_allow_html=True
    )

st.set_page_config(page_title="Portfolio", page_icon=":tada:", layout="wide")

#st.markdown("<style>body { background-color: #f0f2f6; }</style>", unsafe_allow_html=True)
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/0ee55b86-94ed-4428-b83f-236577989618/vny2UcDLhG.json")


# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Kamalesh Anandakumaresan :wave:")
    st.title("A Data Analyst From India")
    st.write(
        "As a data scientist, I see myself as a curious explorer navigating the vast landscape of data. With a keen eye for detail and a passion for uncovering hidden gems, I dive deep into datasets, armed with my expertise in statistics, programming, and machine learning. I thrive on the challenge of untangling complex problems and transforming raw data into valuable insights that drive informed decision-making. I'm driven by a desire to continuously learn and innovate, using my skills to make a meaningful impact and drive positive change in the world through data-driven solutions."
    )
    st.write("[Learn More >](https://www.linkedin.com/in/kamalesh-a-051500220)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("My Skills")
        st.write("##")
        st.write(
            """
SOFT SKILLS:-  
         
⦁	Problem Solving
⦁	Leadership
⦁	Logical Thinking
⦁	Time Management

HARD SKILLS:-

⦁	JAVA
⦁	C Programming
⦁	Python
⦁	SQL
⦁	HTML,CSS
⦁	Machine Learning
⦁	Data Science
⦁	JavaScript
⦁	Networking

             """
        )
        
        st.write("[Resume >](https://drive.google.com/file/d/1k5CJjfUb687jeGeB1mqzkndCIyGSIVM5/view?usp=drivesdk)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image('download.jpg')
    with text_column:
        st.subheader("Optical Text Reader")
        st.write(
            """
           Text-to-speech technology serves as a crucial tool for providing accessibility to information for visually impaired individuals. It works by converting written text into spoken words, allowing them to access a wide range of content such as books, articles, websites, and more.

            """
        )
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image('download (2).jpg')
    with text_column:
        st.subheader("Flight Ticket Booking")
        st.write(
            """
            Efficient airline management demands precise ticketing, meticulous flight coordination, personalized customer service, adept booking facilitation, and seamless vendor collaboration for optimal performance
            """
        )
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image('download (1).jpg')
    with text_column:
        st.subheader("Smart Bin")
        st.write(
            """
           Automated sensors within bins monitor garbage levels. If levels exceed set thresholds, notifications are sent to authorities, prompting timely emptying. Enhances waste management efficiency and cleanliness in urban areas.
            """
        )
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image('download (3).jpg')
    with text_column:
        st.subheader("Stress Detection Using Machine Learning")
        st.write(
            """
            Fusing facial expressions and physiological data for stress assessment enables continuous monitoring and personalized interventions for improved well-being.
            """
        )
        
#Achievements        
with st.container():
    st.write("---")
    st.header("My Achievements")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image('images.jpg')
    with text_column:
        st.subheader("Won 2nd place in ADBU HACKATHON")
        st.write(
            """
             The mini GPS sensor, paired with the My Comrade app, enhances women's safety. It provides real-time location tracking and distress signals, ensuring quick response and support during emergencies.
            """
        )
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image('download.png')
    with text_column:
        st.subheader("Won 1st place in Pitch it Up Fiestaa'24")
        st.write(
            """
            Pitch it Up Fiestaa'24" was an event conducted by KPR Institutions in Coimbatore. It likely involved participants pitching their innovative ideas or projects to a panel of judges. The event might have included various categories such as entrepreneurship, technology, or social impact. Winning first place indicates the success of the participant's pitch in impressing the judges with its creativity, feasibility, and potential impact.
            """
        )
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image('download (1).png')
    with text_column:
        st.subheader("CERTIFICATION IN INFOSYS SPRINGBOARD")
        st.write(
            """
            The Infosys Springboard certification offers training in Java and Python, equipping individuals with skills in both languages for software development.            
            """
        )
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image('images (1).png')
    with text_column:
        st.subheader("CERTIFICATION IN AWS Cloud Foundations")
        st.write(
            """
            The AWS Cloud Foundations certification provides fundamental knowledge of Amazon Web Services (AWS) cloud computing. It covers key concepts, services, and best practices, validating proficiency for cloud-based solutions and deployments.
            """
        )
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image('8-Essential-Soft-Skills-for-Developers-.jpg.webp')
    with text_column:
        st.subheader("CERTIFICATION IN ENGINEERING ETHICS AND SOFT SKILLS")
        st.write(
            """
            The Certification in Engineering Ethics and Soft Skills focuses on fostering ethical conduct and enhancing interpersonal abilities essential for engineers. It covers topics like professionalism, communication, teamwork, and ethical decision-making
            """
        )
# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("For Any Doubts!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/kamalesh.a02@gmail.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
