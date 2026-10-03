import streamlit as st

def render_result(result):
    level = result["risk_level"]
    score = result["risk_score"]

    if level == "High":
        st.error(f"🚨 {level} risk indicators detected — {score}/100")
    elif level == "Medium":
        st.warning(f"⚠️ {level} risk indicators detected — {score}/100")
    else:
        st.success(f"ℹ️ {level} risk indicators detected — {score}/100")

    st.subheader("Why was it flagged?")
    if result["flags"]:
        for flag in result["flags"]:
            st.write(f"• {flag}")
    else:
        st.write("• No predefined warning pattern was detected.")

    st.subheader("Simple explanation")
    st.write(result["explanation"])

    st.subheader("Safer next steps")
    for step in result["next_steps"]:
        st.write(f"• {step}")

    st.caption("Important: This is a safety-screening prototype, not a legal or regulatory verdict.")
