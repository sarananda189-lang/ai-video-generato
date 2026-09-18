import streamlit as st
import requests

st.set_page_config(page_title="AI Video Studio", layout="centered")
st.title("🎬 AI Video Generator Studio")
st.write("Enter a prompt to generate AI videos instantly.")

API_URL = "https://api-inference.huggingface.co/models/damo-vilab/text-to-video-ms-1.7b"
HF_TOKEN = "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"

prompt = st.text_area("Prompt එක ඇතුළත් කරන්න:", "A cute cat playing with a ball, high quality")

if st.button("Generate Video 🚀"):
    if not prompt:
        st.error("කරුණාකර Prompt එකක් ඇතුළත් කරන්න.")
    else:
        st.info("Video එක Generate වෙමින් පවතියි. තත්පර කිහිපයක් රැඳී සිටින්න...")
        headers = {"Authorization": f"Bearer {HF_TOKEN}"}
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
        
        if response.status_code == 200:
            st.video(response.content)
            st.success("🎉 Video එක සාර්ථකව හැදී අවසන්!")
        else:
            st.error("Model එක Load වෙමින් පවතී හෝ සීමාව ඉක්මවා ඇත. තත්පර කිහිපයකින් නැවත උත්සාහ කරන්න.")
