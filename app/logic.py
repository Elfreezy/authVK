from app import db
from app.models import User

import vk_api
import random


def vk_auth(token):
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()
    return vk


# Можно без формирования нового токена т.к. offline
def get_vk_user(res):
    vk = vk_auth(res.get('access_token'))
    user_vk_info = vk.users.get(fields='photo_200')[0]
    user = User.query.filter_by(user_id=user_vk_info['id']).first()
    if not user:
        user = User(first_name=user_vk_info.get('first_name'),
                    last_name=user_vk_info.get('last_name'),
                    user_id=user_vk_info.get('id'))
    setattr(user, 'token', res.get('access_token'))
    setattr(user, 'image', user_vk_info.get('photo_200'))
    db.session.add(user)
    db.session.commit()
    return user


def get_friends(toke):
    vk = vk_auth(toke)
    friends_id = vk.friends.get(fields='photo_200').get('items')
    return random.sample(friends_id, 5)
