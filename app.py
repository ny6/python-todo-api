from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': 'Buy milk',
        'description': 'Milk, Cheese, Pizza',
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Start Python Advanced',
        'done': False
    }
]


@app.route('/tasks')
def get_tasks():
    return jsonify(status=True, data={'tasks': tasks})


@app.route('/tasks/<int:task_id>')
def get_task_by_id(task_id: int):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return jsonify(status=False, message='No task found!')

    return jsonify(status=True, data={'task': task})


if __name__ == '__main__':
    app.run()
