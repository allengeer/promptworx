import os.path
from pypdf import PdfReader




def call(filename):
    try:
        extension = os.path.splitext(filename)[1]
        if extension.lower() == ".pdf":
            reader = PdfReader(filename)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            return text
        else:
            with open(filename, 'r') as file:
                data = file.read()
                return data
    except Exception as e:
        return f"ERROR: {e}"

definition = {
            "name": "READFILE",
            "description": "Reads a file from the local filesystem.",
            "format": "READFILE <filename>",
            "call": call
}