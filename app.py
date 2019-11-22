from flask import Flask, jsonify, request

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


def get_tasks():
    return jsonify(status=True, data={'tasks': tasks})


def create_task(task):
    tasks.append(task)
    return jsonify(status=True, message='Task created successfully!', data={'task': task})


@app.route('/tasks', methods=['GET', 'POST'])
def tasks_route():
    if request.method == 'POST':
        if not request.json or not 'title' in request.json:
            return jsonify(status=True, message='Title is missing!')

        task = {
            'id': tasks[-1]['id'] + 1,
            'title': request.json['title'],
            'description': request.json.get('description', ''),
            'done': False,
        }
        return create_task(task)

    return get_tasks()


@app.route('/tasks/<int:task_id>')
def get_task_by_id(task_id: int):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return jsonify(status=False, message='No task found!')

    return jsonify(status=True, data={'task': task})


if __name__ == '__main__':
    app.run()
