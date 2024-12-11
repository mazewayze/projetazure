# Création du contenu HTML
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python HTML</title>
</head>
<body>
    <h1>Hello</h1>
</body>
</html>
"""

# Nom du fichier HTML
file_name = "hello.html"

# Écriture du contenu dans le fichier
with open(file_name, "w") as file:
    file.write(html_content)

# Ouverture de la page dans le navigateur
import webbrowser
webbrowser.open(file_name)
