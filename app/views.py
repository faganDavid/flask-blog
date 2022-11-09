from flask import Blueprint, render_template, request
import requests

response = requests.get("https://api.npoint.io/9edee6102b84d2334596").json()

views = Blueprint('views', __name__)


@views.route('/')
def get_all_posts():
    return render_template("index.html", response=response)


@views.route("/about")
def about():
    return render_template("about.html")


@views.route("/contact", methods=["GET", "POST"])
def contact():
    error = None
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]

        data_sent = True

        return render_template("contact.html", data_sent=data_sent)

    else:
        error = "invalid"

    return render_template("contact.html", error=error)


@views.route("/post/<int:index>")
def post(index):
    requested_post = None
    for blog_post in response:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)
