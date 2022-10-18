from flask import Flask, abort, request, Response
import os
import smtp
import config
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['POST'])
def post():
    auth_code = request.headers['Authorization']
    if auth_code != config.AUTH_KEY:
        print("Попытка сторонней авторизации. Ввели некорректн ый код: %s" % auth_code)
        abort(400)

    body = request.json

    title = body['title']
    message = body['message']
    mail_to = body['mail_to']
    smtp_auth_key = body['smtp_auth_key']

    try:
        smtp.sendEMail(smtp_auth_key, config.MAIL_FROM, mail_to, title, message)
    except Exception as e:
        print(e)
        abort(400)

    resp = Response()
    resp.status_code = 200

    return resp


if __name__ == '__main__':
    port = int(os.environ.get("PORT", config.PORT))
    app.run(host=config.HOST, port=port, debug=config.DEBUG)
