import streamlit as st
from classifier import classify_feedback

def main():
    st.set_page_config(page_title="College Feedback Classifier", layout="centered")
    st.title("🎓 College Feedback Classifier (Powered by watsonx.ai)")
    st.write("Classify open-ended student feedback into categories using IBM Foundation Models.")

    feedback = st.text_area("Enter student feedback:", height=200)
    if st.button("Classify") and feedback.strip():
        with st.spinner("Classifying with watsonx.ai..."):
            try:
                result = classify_feedback(feedback)
                st.success("Prediction Complete!")
                st.markdown("### 📘 Predicted Category")
                st.code(result)
            except Exception as e:
                st.error(f"API call failed: {str(e)}")

if __name__ == "__main__":
    main()
