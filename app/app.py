from flask import Flask, render_template, request, jsonify
import redis
import os
import platform

app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST', 'localhost')
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    if request.method == 'POST':
        task = request.json.get('task')
        if task:
            r.lpush('tasks', task)
            return jsonify({'status': 'added', 'task': task})
    else:
        tasks = r.lrange('tasks', 0, -1)
        return jsonify({'tasks': tasks})

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'hostname': platform.node(),
        'redis_connected': r.ping()
    })

@app.route('/metrics')
def metrics():
    tasks_count = r.llen('tasks')
    return jsonify({
        'tasks_total': tasks_count,
        'redis_connected': 1 if r.ping() else 0
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
