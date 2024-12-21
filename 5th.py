from docx import Document

def create_word_document():
    file_name = "CompanyOverview.docx"
    content = ("This document provides information about the operations of a fictional company, XYZ Enterprises. "
               "It highlights key achievements, operational goals, and strategies to maintain excellence in "
               "customer service and innovation. The document serves as an overview for stakeholders, "
               "showcasing XYZ Enterprises' dedication to quality, sustainability, and market leadership.")

    # Create a document and add content
    document = Document()
    document.add_paragraph(content)

    # Save the document
    document.save(file_name)
    print(f"Word document created: {file_name}")

create_word_document()
