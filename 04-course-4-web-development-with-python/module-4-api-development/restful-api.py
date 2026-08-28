from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for demonstration
posts = [
    {"id": 1, "title": "First Post", "content": "This is the first post."},
    {"id": 2, "title": "Second Post", "content": "This is the second post."}
]

@app.route('/api/posts', methods=['GET'])
def get_posts():   
  """Retrieves all posts."""
  return jsonify({'posts': posts})

@app.route('/api/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
  """Retrieves a specific post by ID."""
  post = next((post for post in posts if post['id'] == post_id), None)
  if post:
    return jsonify({'post': post})
  return jsonify({'message': 'Post not found'}), 404

@app.route('/api/posts', methods=['POST'])
def create_post():
  """Creates a new post."""
  new_post = request.get_json()  # Get post data from request body
  new_post['id'] = len(posts) + 1
  posts.append(new_post)
  return jsonify({'post': new_post}), 201

@app.route('/api/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
  """Updates a post with a new representation."""
  post = next((post for post in posts if post['id'] == post_id), None)
  if not post:
    return jsonify({'message': 'Post not found'}), 404
  updated_post = request.get_json()
  updated_post['id'] = post_id  # Ensure ID remains the same
  posts[post_id - 1] = updated_post
  return jsonify({'post': updated_post})

@app.route('/api/posts/<int:post_id>', methods=['PATCH'])
def partial_update_post(post_id):
  """Partially updates a post."""
  post = next((post for post in posts if post['id'] == post_id), None)
  if not post:
    return jsonify({'message': 'Post not found'}), 404
  updates = request.get_json()
  post.update(updates)  # Apply partial updates
  return jsonify({'post': post})

@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
  """Deletes a post."""
  post = next((post for post in posts if post['id'] == post_id), None)
  if not post:
    return jsonify({'message': 'Post not found'}), 404
  posts.remove(post)
  return jsonify({'message': 'Post deleted'}), 204

if __name__ == '__main__':
  app.run(debug=True)
