from app.infrastructure.parsers.pypdf import PyPDFParser

def test_parse_pdf():
    parser = PyPDFParser()

    document = parser.parse("tests/sample.pdf")

    assert document is not None
    assert document.text != ""
    assert isinstance(document.tables, list)
    assert isinstance(document.images, list)