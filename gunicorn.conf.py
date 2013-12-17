import multiprocessing

bind = "unix:/tmp/gunicorn.sock"
workers = multiprocessing.cpu_count() * 2 + 1
name = "ifiltr"
user = "webapps"
group = "webapps"
