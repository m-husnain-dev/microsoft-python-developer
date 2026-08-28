from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Posts collection initialized as a list
posts = []


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/posts", methods=["GET"])
def get_posts():
    # STEP 3: Return posts encoded as JSON with a 200 OK status code
    return jsonify(posts), 200


@app.route("/posts", methods=["POST"])
def create_post():
    data = request.get_json()

    # STEP 4.2: Validate data
    if not data or "title" not in data or "content" not in data:
        return jsonify({"error": "Invalid data"}), 400

    # STEP 4.3: Create new post dictionary
    new_post = {
        "id": len(posts) + 1,
        "title": data["title"],
        "content": data["content"],
    }

    # Append new post to global posts list
    posts.append(new_post)

    # Return created post as JSON with 201 Created status
    return jsonify(new_post), 201


if __name__ == "__main__":
    app.run(debug=True)