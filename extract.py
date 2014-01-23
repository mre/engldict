from pdftables.pdf_document import PDFDocument as pdfdoc
from pdftables.pdftables import page_to_tables
from pdftables.display import to_string


filepath = 'irregular-verbs-de.pdf'
fileobj = open(filepath, 'rb')

doc = pdfdoc.from_fileobj(fileobj)

page = doc.get_page(0)
tables = page_to_tables(page)
for table in tables:
  print to_string(table.data)
