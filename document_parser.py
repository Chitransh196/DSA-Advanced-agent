from pypdf import PdfReader


def parse_uploaded_file(uploaded_file):

    content = ""

    # TXT
    if uploaded_file.type == "text/plain":

        content = uploaded_file.read().decode("utf-8")

    # PDF
    elif uploaded_file.type == "application/pdf":

        reader = PdfReader(uploaded_file)

        for page in reader.pages:

            text = page.extract_text()

            if text:
                content += text + "\n"

    return content