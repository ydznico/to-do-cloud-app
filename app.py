from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config["tasks"] = []


@app.route("/")
def home():
    tasks = app.config["tasks"]
    pending = sum(1 for task in tasks if not task["completed"])
    completed = sum(1 for task in tasks if task["completed"])

    return render_template(
        "index.html",
        tasks=tasks,
        pending=pending,
        completed=completed
    )


@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title", "").strip()

    if title:
        tasks = app.config["tasks"]
        new_id = max((task["id"] for task in tasks), default=0) + 1
        tasks.append({
            "id": new_id,
            "title": title,
            "completed": False
        })

    return redirect(url_for("home"))


@app.route("/toggle/<int:task_id>", methods=["POST"])
def toggle_task(task_id):
    for task in app.config["tasks"]:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
            break

    return redirect(url_for("home"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    app.config["tasks"] = [
        task for task in app.config["tasks"]
        if task["id"] != task_id
    ]
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
