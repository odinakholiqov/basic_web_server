import sys
sys.path.insert(0, "./hello")


from hello import wsgi

app = wsgi.application