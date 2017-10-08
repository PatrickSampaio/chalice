from chalice import Chalice, Response, ChaliceViewError, BadRequestError
from chalice import UnauthorizedError
from chalice import NotFoundError

OBJECTS = {}

app = Chalice(app_name='helloworld')
app.debug = True


@app.route('/')
def index():
    return Response(body='hello world!',
                    status_code=200,
                    headers={'Content-Type': 'text/plain'})

@app.route('/cities/{city}')
def state_of_city(city):
    if city == 'portland':
        raise BadRequestError("error message")
    return {'state': city }

@app.route('/objects/{key}', methods=['GET','PUT'])
def myobject(key):
    request = app.current_request
    if request.method == 'PUT':
        OBJECTS[key] = request.json_body
    if request.method == 'GET':
        try:
            return {key: OBJECTS[key]}
        except KeyError:
            raise NotFoundError(key)

#* BadRequestError - return a status code of 400
#* UnauthorizedError - return a status code of 401
#* ForbiddenError - return a status code of 403
#* NotFoundError - return a status code of 404
#* ConflictError - return a status code of 409
#* TooManyRequestsError - return a status code of 429
#* ChaliceViewError - return a status code of 500

#Use the Response class when you want to return non-JSON content,
# or when you want to inject custom HTTP headers to your response.














