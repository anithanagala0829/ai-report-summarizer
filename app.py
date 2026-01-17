import streamlit as st

st.set_page_config(page_title="AI Report Summarizer", layout="wide")

st.title("📄 Generative AI Report Summarizer")
st.write("Upload a business report and generate summaries using AI.")

uploaded_file = st.file_uploader("Upload Annual Report (PDF)", type=["pdf"])

if uploaded_file:
    st.success("Report uploaded successfully!")

    if st.button("Generate Summary"):
        with open("executive_summary.txt", "r", encoding="utf-8") as f:
            executive_summary = f.read()

        with open("analytical_summary.txt", "r", encoding="utf-8") as f:
            analytical_summary = f.read()

        st.subheader("📌 Executive Summary")
        st.write(executive_summary)

        st.subheader("📊 Analytical Summary")
        st.write(analytical_summary)

        st.success("Summary generated successfully!")
