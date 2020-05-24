from time import time

from students_tracker.models import Logger


class LoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time()
        path = request.path
        logger = Logger(method=request.method, path=path, execution_time=start_time)
        response = self.get_response(request)
        end_time = time()
        logger.execution_time = end_time - start_time
        if str(path).startswith('/admin/'):
            logger.save()
        return response
