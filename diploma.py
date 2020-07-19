import json
import time
from User import User


def uncommon_group(user_id):
    """
    функция запускает сканирование пользователей и проверяет их по группам
    """
    main_user = User(user_id)
    time.sleep(1/3)
    friends_set = main_user.get_friends()
    time.sleep(1/3)
    group_set = main_user.group_set()
    print('Начинаем сканирование пользователей')
    counter = 1

    for friend_id in friends_set:
        user = User(friend_id)
        time.sleep(1/3)
        try:
            new_group_set = user.group_set()
        except KeyError:
            print(f'Пользователь с id{friend_id} закрыт или заблокирован')
            print(f'{counter}/{len(friends_set)}')
            counter += 1
            continue
        group_set = set(group_set) - set(new_group_set)
        print(f'{counter}/{len(friends_set)}')
        counter += 1
    return group_set


def get_data():
    """
    функция формирует список групп и параметры, а именно id группы, название группы, кол-во участников в группе
    """
    data = []
    user = User(USER_ID)
    unique_groups = uncommon_group(USER_ID)

    for group in user.get_user_groups()['response']['items']:
        if group['id'] in unique_groups:
            try:
                data.append({'name': group['name'], 'gid': group['id'], 'members_count': group['members_count']})
            except KeyError:
                continue
    return data


def dump_json():
    """
    функция записывает в .json файл запрашиваемые свойства из функции  get_data
    """
    with open('groups.json', 'w', encoding='utf-8') as fo:
        json.dump(DATA, fo, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    USER_ID = input('Введите ID пользователя: ')
    DATA = get_data()
    dump_json()