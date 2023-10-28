#!bin/bash

mkdir templates
touch templates/_base.html

mkdir templates/include
touch templates/include/_css.html
touch templates/include/_js.html
touch templates/include/_nav.html
touch templates/include/_footer.html
touch templates/include/_pagination.html

mkdir home/templates
touch home/templates/index.html
touch home/urls.py

mkdir static
mkdir static/css
touch static/css/djangotailwindcss-ui.css

mkdir static/custom
touch static/custom/custom.css

mkdir static/tailwindcss
touch static/tailwindcss/input.css

mkdir static/img
