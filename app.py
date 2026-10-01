import os
import sys
import streamlit as st


# ============================================================
# LegalEase Project Root
# ============================================================

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


# ============================================================
# DOCX Export Module
# ============================================================

DOCX_AVAILABLE = False
DOCX_ERROR = ""
format_docx = None

DOCX_AVAILABLE = False
DOCX_ERROR = ""
format_docx = None

try:
    from formatting.docx_expord import format_docx
    DOCX_AVAILABLE = True
except Exception as e:
    DOCX_AVAILABLE = False
    DOCX_ERROR = str(e)


# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="LegalEase",
    page_icon="⚖️",
    layout="wide"
)


# ============================================================
# Title
# ============================================================

st.title("⚖️ LegalEase")
st.subheader("Legal Document Generator")


# ============================================================
# Input
# ============================================================

question = st.text_area(
    "Describe the legal document you want to generate:",
    placeholder=(
        "Example: Create a rental agreement "
        "between a landlord and tenant."
    )
)

language = st.selectbox(
    "Language",
    [
        "English",
        "Tamil"
    ]
)

parties = st.text_area(
    "Parties",
    placeholder=(
        "Example:\n"
        "Landlord: Ravi\n"
        "Tenant: Kumar"
    )
)

terms = st.text_area(
    "Terms / Conditions",
    placeholder=(
        "Enter the important terms and conditions..."
    )
)

effective_date = st.text_input(
    "Effective Date",
    placeholder="DD-MM-YYYY"
)


# ============================================================
# Generate Document
# ============================================================

if st.button("Generate Document", type="primary"):

    if not question.strip():
        st.error(
            "Please enter the document requirement."
        )
        st.stop()

    st.success(
        "Document request received."
    )

    st.write("### Document Details")

    st.write("**Requirement:**")
    st.write(question)

    st.write("**Language:**")
    st.write(language)

    if parties.strip():
        st.write("**Parties:**")
        st.write(parties)

    if terms.strip():
        st.write("**Terms:**")
        st.write(terms)

    if effective_date.strip():
        st.write("**Effective Date:**")
        st.write(effective_date)


# ============================================================
# DOCX Export
# ============================================================

st.divider()

st.write("### DOCX Export")


if DOCX_AVAILABLE:

    st.success(
        "✅ DOCX export module loaded successfully."
    )

    st.success(
        "✅ format_docx function found."
    )

    # --------------------------------------------------------
    # Create DOCX
    # --------------------------------------------------------

    if st.button("Create DOCX"):

        document_content = (
            f"Requirement:\n"
            f"{question}\n\n"
            f"Language:\n"
            f"{language}\n\n"
            f"Parties:\n"
            f"{parties}\n\n"
            f"Terms / Conditions:\n"
            f"{terms}\n\n"
            f"Effective Date:\n"
            f"{effective_date}"
        )

        try:

            docx_file = format_docx(
                title="LegalEase Legal Document",
                content=document_content
            )

            # Handle BytesIO result
            if hasattr(docx_file, "getvalue"):
                docx_data = docx_file.getvalue()
            else:
                docx_data = docx_file

            st.download_button(
                label="⬇️ Download DOCX",
                data=docx_data,
                file_name="LegalEase_Document.docx",
                mime=(
                    "application/"
                    "vnd.openxmlformats-officedocument."
                    "wordprocessingml.document"
                )
            )

            st.success(
                "✅ DOCX document created successfully."
            )

        except Exception as e:

            st.error(
                f"❌ DOCX creation failed: {e}"
            )

else:

    st.error(
        "❌ DOCX export module could not be loaded."
    )

    st.code(
        DOCX_ERROR
    )