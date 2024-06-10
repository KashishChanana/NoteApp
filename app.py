import streamlit as st
from main import Workflow


def main():
    st.title("NoteApp")
    # input_url, input_model, input_task = st.sidebar.columns(3)

    youtube_sidebar, file_sidebar = st.sidebar.tabs(["YouTube", "File Upload"])
    with youtube_sidebar:
        input_url = st.text_input("YouTube URL")

    with file_sidebar:
        input_file = st.file_uploader("Choose a PDF")

    model = st.sidebar.selectbox("Generative Model", ["GPT-3.5"])
    task = st.sidebar.selectbox("Generative Task", ["Blog", "Summary"])
    generate_button = st.sidebar.button("Generate", type="secondary")

    if generate_button and (input_url or input_file):
        st.video(input_url)
        response = Workflow().run(youtube_url=input_url, model=model, task=task)
        if response:
            st.divider()
            st.subheader(task)
            st.markdown(response)

if __name__ == "__main__":
    main()





