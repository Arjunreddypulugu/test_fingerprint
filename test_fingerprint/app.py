import streamlit as st
from streamlit_js_eval import streamlit_js_eval
 
st.title("🔍 Fingerprint Test")
 
if st.button("🔐 Get My Device Fingerprint"):
    fingerprint = streamlit_js_eval(
        js_expressions="""
        const fpPromise = import('https://openfpcdn.io/fingerprintjs/v3')
            .then(FingerprintJS => FingerprintJS.load());
        fpPromise.then(fp => fp.get()).then(result => result.visitorId);
        """,
        key="fingerprint"
    )
 
    if fingerprint:
        st.success("✅ Fingerprint Detected!")
        st.code(f"Fingerprint ID: {fingerprint}")
    else:
        st.error("❌ Could not generate fingerprint.")