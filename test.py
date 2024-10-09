from nbconvert import HTMLExporter
from nbformat import read
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/notebook")
def display_notebook():
    # Load the notebook
    with open("poc.ipynb") as f:
        notebook_content = read(f, as_version=4)

    # Convert the notebook to HTML
    html_exporter = HTMLExporter()
    (body, resources) = html_exporter.from_notebook_node(notebook_content)

    return render_template_string(body)

if __name__ == "__main__":
    app.run(debug=True)