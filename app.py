import streamlit as st
from main import Workflow


def main():
    st.title("NoteApp")
    youtube_sidebar, file_sidebar = st.sidebar.tabs(["YouTube", "File Upload"])

    with youtube_sidebar:
        input_url = st.text_input("YouTube URL")

    with file_sidebar:
        input_file = st.file_uploader("Choose a PDF")

    model = st.sidebar.selectbox("Generative Model", ["GPT-3.5"])
    task = st.sidebar.selectbox("Generative Task", ["Blog", "Summary"])
    generate_button = st.sidebar.button("Generate", type="secondary")

    if input_url:
        upload_type = "YouTubeURL" 
        input_io = input_url
    
    if input_file:
        upload_type = "FileUpload"
        input_io = input_file

    if generate_button and (input_url or input_file):

        if input_url:
            st.video(input_url)
            st.divider()

        response = Workflow().run(input_io, model, task, upload_type)
        if response:
            st.subheader(task)
            st.markdown(response)

if __name__ == "__main__":
    main()
