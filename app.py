from flask import Flask, render_template, request, redirect, url_for
from DAL import get_projects, insert_project, init_db, seed

app = Flask(__name__)

# Ensure DB exists (and optionally seed) when app starts
with app.app_context():
    init_db()
    seed()  # uncomment once if you want demo rows

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

@app.route("/projects")
def projects():
    projects_list = get_projects()
    return render_template("projects.html", projects=projects_list)

@app.route("/projects/new")
def new_project():
    return render_template("add_project.html")

@app.route("/projects", methods=["POST"])
def create_project():
    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()
    image_filename = request.form.get("image_filename", "").strip()

    # Minimal validation
    if not title or not description or not image_filename:
        # In a real app you'd flash a message; for simplicity just re-render with an error
        return render_template("add_project.html", error="All fields are required.", 
                               form={"title": title, "description": description, "image_filename": image_filename})

    insert_project(title, description, image_filename)
    return redirect(url_for("projects"))

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")

if __name__ == "__main__":
    app.run(debug=True)