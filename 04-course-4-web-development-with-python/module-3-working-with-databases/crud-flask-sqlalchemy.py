from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# 1. Flask App Setup
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# 2. Database Model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    is_completed = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "is_completed": self.is_completed
        }

with app.app_context():
    db.create_all()

# ==========================================
# CRUD ROUTES
# ==========================================

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if not data or not data.get('title'):
        return jsonify({"error": "Title zaroori hai!"}), 400

    new_task = Task(
        title=data['title'],
        description=data.get('description', '')
    )
    
    db.session.add(new_task)
    db.session.commit()
    
    return jsonify({"message": "Task add ho gaya!", "task": new_task.to_dict()}), 201


@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks]), 200


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get_or_404(task_id, description="Task nahi mila")
    return jsonify(task.to_dict()), 200


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get_or_404(task_id, description="Task nahi mila")
    data = request.get_json()

    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.is_completed = data.get('is_completed', task.is_completed)

    db.session.commit()
    return jsonify({"message": "Task update ho gaya!", "task": task.to_dict()}), 200


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id, description="Task nahi mila")
    
    db.session.delete(task)
    db.session.commit()
    
    return jsonify({"message": f"Task #{task_id} delete kar diya gaya hai"}), 200



if __name__ == '__main__':
    app.run(debug=True)