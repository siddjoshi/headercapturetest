#!/usr/bin/env python3

from flask import Flask, jsonify, abort, make_response, request
# from urllib.parse import urlparse
# import datetime
# import time
# import html
# import os
# import json

app = Flask(__name__)


@app.errorhandler(400)  # 400 Bad Request
def error_400(error):
    return make_response(jsonify({
        'error': str(error)
    }), 400)


@app.errorhandler(404)  # 404 Not Found
def error_404(error):
    return make_response(jsonify({
        'error': str(error)
    }), 404)


@app.errorhandler(405)  # 405 Method Not Allowed
def error_405(error):
    return make_response(jsonify({
        'error': str(error),
    }), 405)


@app.route('/', methods=['GET'])
def csp_receiver():
    f = open("/home/LogFiles/headerlogs.txt", "a")

    ## Get Remote IP Address
    ip_address = request.remote_addr
    f.write("Remote IP Address is : " + ip_address)    

    ## Get X-Forwarded-For 
    if request.headers.has_key('X-Forwarded-For'):
        clientip = request.headers['X-Forwarded-For']
        f.write("X-Forwarded header is: " + clientip)
        #return make_response('', 200)
    
    ## Get True Client IP
    if request.headers.has_key('True-Client-IP'):
        trueclientip = request.headers['True-Client-IP']
        f.write("True Client IP header is: " + trueclientip)
        #return make_response('', 200)

    f.close()
    return make_response('ok', 200)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
