# Import Flask modules
from flask import Flask, render_template, request

# Create Flask application
app = Flask(__name__)


# Home route
@app.route("/", methods=["GET", "POST"])
def index():

    result = ""
    student_data=None

    # Run when form is submitted
    if request.method == "POST":

        # Get student information
        name = request.form.get("name")
        cgpa = float(request.form.get("cgpa"))
        year = int(request.form.get("year"))
        branch = request.form.get("branch")

        # Get selected skills
        skills = request.form.getlist("skills")

        # Get other skills
        other_skills = request.form.get("other_skills")

        # Career information
        github = request.form.get("github")
        internship_type = request.form.get("internship_type")

        # Eligibility conditions
        if cgpa >= 7.0 and year >= 2 and len(skills) > 0:

            # Stipend rule
            if other_skills.strip():
                result = "Eligible for Internship with Stipend"
            else:
                result = "Eligible for Internship"

        else:
            result = "Currently Not Eligible for Internship"


        student_data={
            "name":name,
            "cgpa":cgpa,
            "year":year,
            "branch":branch,
            "skills":skills,
            "other_skills":other_skills,
            "github":github,
            "internship_type":internship_type
        }

    return render_template(
          "index.html",
          result=result,
          student_data=student_data
          )


# Run application
if __name__ == "__main__":
    app.run(debug=True)