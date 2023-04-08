import os.path
from pypdf import PdfReader
import docx



def call(filename):
    try:
        extension = os.path.splitext(filename)[1]
        if extension.lower() == ".pdf":
            reader = PdfReader(filename)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            text += "\n[ENDOFFILE]"
            return text
        if extension.lower() == ".docx":
            doc = docx.Document(filename)
            fullText = []
            for para in doc.paragraphs:
                fullText.append(para.text)
            fullText.append("[ENDOFFILE]")
            return '\n'.join(fullText)
        else:
            with open(filename, 'r') as file:
                data = file.read()
                data += "\n[ENDOFFILE]"
                return data
    except Exception as e:
        return f"ERROR: {e}"

definition = {
            "name": "READFILE",
            "description": "Reads a file from the local filesystem. The end of the file is marked by the token [ENDOFFILE]",
            "format": "READFILE <filename>",
            "call": call
}