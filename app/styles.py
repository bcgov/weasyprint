import os
from weasyprint import CSS
from weasyprint.text.fonts import FontConfiguration

font_config = FontConfiguration()

current_directory = os.path.dirname(os.path.abspath(__file__))

default_fonts = f"""
/* Normal */
@font-face {{
  font-family: "BCSans";
  src: url("file://{current_directory}/fonts/bcsans/2023_01_01_BCSans-Regular_2f.woff2") format("woff2"),
       url("file://{current_directory}/fonts/bcsans/2023_01_01_BCSans-Regular_2f.woff") format("woff");
  font-weight: normal;
  font-style: normal;
}}

/* Light */
@font-face {{
  font-family: "BCSans";
  src: url("file://{current_directory}/fonts/bcsans/2023_03_14_BCSans-Light_2g.woff2") format("woff2"),
       url("file://{current_directory}/fonts/bcsans/2023_03_14_BCSans-Light_2g.woff") format("woff");
  font-weight: 300;
  font-style: normal;
}}

/* Bold */
@font-face {{
  font-family: "BCSans";
  src: url("file://{current_directory}/fonts/bcsans/2023_01_01_BCSans-Bold_2f.woff2") format("woff2"),
       url("file://{current_directory}/fonts/bcsans/2023_01_01_BCSans-Bold_2f.woff") format("woff");
  font-weight: bold;
  font-style: normal;
}}

/* Italic */
@font-face {{
  font-family: "BCSans";
  src: url("file://{current_directory}/fonts/bcsans/2023_01_01_BCSans-Italic_2f.woff2") format("woff2"),
       url("file://{current_directory}/fonts/bcsans/2023_01_01_BCSans-Italic_2f.woff") format("woff");
  font-weight: normal;
  font-style: italic;
}}

/* Light Italic */
@font-face {{
  font-family: "BCSans";
  src: url("file://{current_directory}/fonts/bcsans/2023_01_01_BCSans-LightItalic_2f.woff2") format("woff2"),
       url("file://{current_directory}/fonts/bcsans/2023_01_01_BCSans-LightItalic_2f.woff") format("woff");
  font-weight: 300;
  font-style: italic;
}}

/* Bold Italic */
@font-face {{
  font-family: "BCSans";
  src: url("file://{current_directory}/fonts/bcsans/2023_01_01_BCSans-BoldItalic_2f.woff2") format("woff2"),
       url("file://{current_directory}/fonts/bcsans/2023_01_01_BCSans-BoldItalic_2f.woff") format("woff");
  font-weight: bold;
  font-style: italic;
}}
"""

default_css = CSS(string=default_fonts, font_config=font_config)
