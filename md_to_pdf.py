import markdown2
import pdfkit

# Convert Markdown file to HTML
with open('Linux_Basics_and_Commands.md', 'r', encoding='utf-8') as f:
    markdown_text = f.read()
html = markdown2.markdown(markdown_text)

# Convert HTML to PDF
pdfkit.from_string(html, 'Linux_Basics_and_Commands.pdf')
print('PDF created successfully: Linux_Basics_and_Commands.pdf')
