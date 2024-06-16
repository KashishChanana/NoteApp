import streamlit as st
from main import Workflow

workflow = Workflow()

def main():
    st.set_page_config(
        page_title="TLDR",
        page_icon='💬',
        layout='wide'
    )
    
    web_sidebar, youtube_sidebar, file_sidebar = st.sidebar.tabs(["Web", "YouTube", "File Upload"])

    with web_sidebar:
        web_url = st.text_input("Enter URL")

    with youtube_sidebar:
        youtube_url = st.text_input("Enter YouTube URL")

    with file_sidebar:
        input_file = st.file_uploader("Choose a PDF")

    model = st.sidebar.selectbox("Generative Model", ["GPT-3.5"])
    task = st.sidebar.selectbox("Generative Task", ["Blog", "Summary"])
    generate_button = st.sidebar.button("Generate", type="secondary")

    if web_url:
        upload_type = "WebURL"
        input_io = web_url

    elif youtube_url:
        upload_type = "YouTubeURL" 
        input_io = youtube_url
    
    elif input_file:
        upload_type = "FileUpload"
        input_io = input_file

    if generate_button and (web_url or youtube_url or input_file):

        if youtube_url:
            st.video(youtube_url)
            st.divider()

        splits, response = workflow.run(input_io, model, task, upload_type)
        if response:
            st.subheader(task)
            st.markdown(response)

        if 'save_clicked' not in st.session_state:
            st.session_state.save_clicked = False

        def on_save_button_click():
            workflow.save(splits)
            st.session_state.save_clicked = True
            st.markdown(response)
            st.button('Saved', disabled=True)
        
        # Define save button with callback
        save_button = st.button('Save', type="primary", on_click=on_save_button_click)

if __name__ == "__main__":
    main()
