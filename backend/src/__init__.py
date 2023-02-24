from flask import Flask,render_template,request,jsonify
from os import getenv
from  redis import from_url
from rq import Queue
from rq.job import Job

app = Flask(__name__)
app.secret_key = 'random string'
app.static_folder = 'static'
app.config['JSON_AS_ASCII'] = False
app.template_folder='templates'


def __get_redis_con():
    redis_url = getenv('redis_url')
    return from_url(redis_url)  

def __get_queue(queue_name='default'):
    conn = __get_redis_con()
    return Queue(name=queue_name,connection=conn)
    
def __sheduled_tasks_count(queue_name='default'):
    queue = __get_queue()
    return queue.count
    
def __add_task_to_queue(task,*args,**kwargs):
    queue = __get_queue()
    queue.enqueue(task,*args,**kwargs)    

def __finished_tasks():
    conn = __get_redis_con()
    queue = __get_queue()
    job_ids=queue.finished_job_registry.get_job_ids()
    _jobs=[Job.fetch(_job_id, connection=conn) for _job_id in job_ids]
    return _jobs     
    
@app.route("/", methods =["GET", "POST"])
def index_func():
    data={'title':'index'}
    task_param = request.form.get("task_param")
    if task_param is not None:
        __add_task_to_queue('tasks.simple_task',task_param)
    else:
        task_param='None'
    data={'title':'index',
          'queue_count':__sheduled_tasks_count(),
          'completed':len(__finished_tasks()),          
          'task_param':task_param}
    return render_template('index.html',data=data)
   
@app.route("/finished_tasks", methods =["GET", "POST"])
def acomplishments():
    return jsonify([ (_task.id,_task.result) for _task in __finished_tasks()])    