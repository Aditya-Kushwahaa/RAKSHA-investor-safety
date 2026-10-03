import streamlit as st
from raksha.analyzer import analyze_content
from raksha.ocr import extract_text_from_image
from raksha.ui import render_result

st.set_page_config(page_title="RAKSHA", page_icon="🛡️", layout="centered")

st.title("🛡️ RAKSHA")
st.caption("Investor safety layer — understand, verify, and pause before you pay.")

with st.sidebar:
    st.header("Input")
    language = st.selectbox("Explanation language", ["English", "Hindi"])
    mode = st.radio("Input type", ["Message / Claim", "Screenshot", "Website URL"])
    st.info("RAKSHA is an investor-protection prototype. It does not provide buy/sell/hold recommendations.")

if mode == "Message / Claim":
    content = st.text_area(
        "Paste the message or financial claim",
        height=220,
        placeholder="Example: Guaranteed 25% monthly returns. Pay ₹5,000 today and join our Telegram group..."
    )
elif mode == "Website URL":
    content = st.text_input("Paste the website URL", placeholder="https://example.com")
else:
    image = st.file_uploader("Upload a screenshot", type=["png", "jpg", "jpeg"])
    content = ""
    if image:
        with st.spinner("Reading screenshot..."):
            content = extract_text_from_image(image)
        if content:
            st.text_area("Extracted content", content, height=180)
        else:
            st.warning("Could not extract text. You can paste the message manually below.")
            content = st.text_area("Paste the message", height=180)

if st.button("🔎 Check with RAKSHA", type="primary", use_container_width=True):
    if not content.strip():
        st.error("Please provide a message, URL, or screenshot.")
    else:
        result = analyze_content(content, language=language)
        render_result(result)

st.divider()
st.caption("Prototype • Evidence should be independently verified through official channels.")
