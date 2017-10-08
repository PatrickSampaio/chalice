from chalice import Chalice
from chalice import UnauthorizedError

app = Chalice(app_name='helloworld')
app.debug = True


@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/cities/{city}')
def state_of_city(city):
    if city == 'portland':
        raise
    return {'state': city }

#* BadRequestError - return a status code of 400
#* UnauthorizedError - return a status code of 401
#* ForbiddenError - return a status code of 403
#* NotFoundError - return a status code of 404
#* ConflictError - return a status code of 409
#* TooManyRequestsError - return a status code of 429
#* ChaliceViewError - return a status code of 500
















