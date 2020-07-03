import requests
import time

TOKEN = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'


class User:

    def __init__(self, USER_ID):
        if str(USER_ID).isdigit():
            self.user_id = USER_ID
        else:
            time.sleep(1 / 3)
            self.params = {
                'access_token': TOKEN,
                'v': 5.89,
                'screen_name': USER_ID
            }
            response = requests.get('https://api.vk.com/method/utils.resolveScreenName', params=self.params).json()
            self.USER_ID = response['response']['object_id']
        self.params = {
            'access_token': TOKEN,
            'v': 5.89,
            'user_id': self.user_id,
        }

    def get_user_groups(self):
        self.params['extended'] = 1
        self.params['fields'] = 'members_count'
        response = requests.get('https://api.vk.com/method/groups.get', params=self.params).json()
        return response

    def group_set(self):
        groups_set = [item['id'] for item in User.get_user_groups(self)['response']['items']]
        return groups_set

    def get_friends(self):
        response = requests.get('https://api.vk.com/method/friends.get', params=self.params).json()
        friends_id = [item for item in response['response']['items']]
        return friends_id
