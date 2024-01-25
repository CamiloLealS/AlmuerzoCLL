from AlmuerzoCLL.wsgi import application


if __name__ == '__main__':
    from waitress import serve
    serve(application, host = '0.0.0.0', port= 8000)