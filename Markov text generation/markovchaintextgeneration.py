!pip install markovify
!pip install weasyprint

import markdown
import random
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration
import markovify

"""## Building the Model"""

with open("/content/001-Game of Thrones Boxed Set A Game of Thrones, a Clatorm of Swords, and a Feast for Crows ( PDFDrive ).txt") as f:
  text = f.read()

with open("/content/001-Harry Potter The complete Collection ( PDFDrive ).txt") as f:
  text += f.read()

with open("/content/001-LordOfTheRings.txt") as f:
  text += f.read()
  
text_model = markovify.Text(text)

novel = ''
while (len( novel.split(" ")) < 10000):
  for i in range(random.randrange(3,9)):
    novel += text_model.make_sentence() + " "
  novel += "\n\n"
  #print(text_model.make_sentence()

print(novel)

"""## Saving the Novel as a PDF"""

novel_html = markdown.markdown(novel)
font_config = FontConfiguration()
html = HTML(string=novel_html)
css = CSS(string="""
@import url('https://fonts.googleapis.com/css2?family=Goudy+Bookletter+1911&display=swap');
body {font-family: 'Goudy Bookletter 1911'}
""", font_config=font_config)
html.write_pdf('/content/GOT+HarryPotter+LordOfRings-30-2.pdf',stylesheets=[css],font_config=font_config)

