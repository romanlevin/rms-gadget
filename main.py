class WSGIApplication(object):
    def __call__(self, environ, start_response):
        return ' '

application = WSGIApplication()
