import streamlit as st
from main import Workflow


def main():
    st.title("NoteApp")
    input_url, input_model, input_task = st.columns(3)

    with input_url:
        input_url = st.text_input("YouTube URL")

    with input_model:
        model = st.selectbox("Generative Model", ["GPT-3.5"])

    with input_task:
        task = st.selectbox("Generative Task", ["Blog", "Summary"])

    st.divider()

    if input_url:
        st.video(input_url)
        response = Workflow().run(youtube_url=input_url, model=model, task=task)
        if response:
            st.divider()
            st.subheader(task)
            st.markdown(response)

if __name__ == "__main__":
    main()





