from flask import redirect
from rauth import OAuth2Service
import requests

from app import app


class VKSingIn():
    def __init__(self):
        self.service = OAuth2Service(
            name='vk',
            client_id=app.config['CLIENT_ID'],
            client_secret=app.config['CLIENT_SECRET'],
            authorize_url='https://oauth.vk.com/authorize',
            base_url='https://vk.com/'
        )

    def authorize(self):
        return redirect(self.service.get_authorize_url(
            scope='offline, friends',
            response_type='code',
            redirect_uri=app.config['REDIRECT_URI'],
            v=5.122
        ))

    def get_token(self, code):
        return requests.get(
            'https://oauth.vk.com/access_token?client_id={client_id} \
            &client_secret={client_secret}&redirect_uri={redirect_uri}&code={code}&v={v}'.format(
            client_id=app.config['CLIENT_ID'],
            client_secret=app.config['CLIENT_SECRET'],
            redirect_uri=app.config['REDIRECT_URI'],
            code=code,
            v=5.122
        ))