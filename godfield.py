import requests
import json
import time
import threading
tokens = []
def create_token():
    params = {
        'key': 'AIzaSyCBvMvZkHymK04BfEaERtbmELhyL8-mtAg',
    }
    json_data = {
        'returnSecureToken': True,
    }
    response = requests.post(
        'https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser',
        params=params,
        json=json_data,
    )
    if response.status_code == 200:
        response_data = response.json()
        idtoken = response_data['idToken']
        tokens.append(idtoken)
        print('[+]垢作成成功！')
    else:
        print('[-]失敗じゃｗ')

headers = {
    'authority': 'www.googleapis.com',
    'accept': '*/*',
    'accept-language': 'ja-JP,ja;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://godfield.net',
    'referer': 'https://godfield.net/',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'x-client-version': 'Chrome/JsCore/8.10.0/FirebaseCore-web',
}
accname = input('名前を入力してください。:')
accountcount = input('いくつトークンを作成しますか？(デフォルト10):')
count = 0

threads = []
for i in range(int(accountcount)):
    t = threading.Thread(target=create_token)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print('トークンの作成が完了しました。')
print(' ')
print('メニュー')
print('1: 公衆乱闘\n\n2: 隠れ乱闘\n\n3: 部屋作成')
input_data2 = str(input("select: "))
if input_data2 =="1":
    print('乱闘ねおおけー')
    headers = {
        'authority': 'asia-northeast1-godfield.cloudfunctions.net',
        'accept': '*/*',
        'accept-language': 'ja-JP,ja;q=0.9',
        'authorization': f'Bearer {tokens[0]}',
        'content-type': 'application/json',
        'origin': 'https://godfield.net',
        'referer': 'https://godfield.net/',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }
    json_data = {
        'mode': 'open',
        'lang': 'ja',
    }

    response = requests.post('https://asia-northeast1-godfield.cloudfunctions.net/openRooms', headers=headers, json=json_data)
    data = json.loads(response.text)

    print("ルーム情報:")
    for i, room in enumerate(data["openRooms"]):
        id = room["id"]
        name = room["name"]
        host_user_name = room["hostUserName"]
        user_count = room["userCount"]
        print(f"{i + 1}: 名前{name}\n   ホストの名前{host_user_name}\n   ユーザー数{user_count}\n   ルームid{id}\n")
    selection = int(input("どの部屋を選択しますか？ "))
    room = data["openRooms"][selection - 1]
    id = room["id"]
    name = room["name"]
    host_user_name = room["hostUserName"]
    user_count = room["userCount"]
    print(f"\n{name} が選択されました！")
    message = input('メッセージを入力してください:')
    print('Join...')
    session = requests.Session()
    count2 = 0
    for token in tokens:
        headers = {
            'authority': 'asia-northeast1-godfield.cloudfunctions.net',
            'accept': '*/*',
            'accept-language': 'ja-JP,ja;q=0.9',
            'authorization': f'Bearer {token}',
            'content-type': 'application/json',
            'origin': 'https://godfield.net',
            'referer': 'https://godfield.net/',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        }
        json_data = {
            'mode': 'open',
            'roomId': f'{id}',
            'userName': f'{accname}{count2}',
        }
        response = session.post('https://asia-northeast1-godfield.cloudfunctions.net/addRoomUser', headers=headers, json=json_data)

        if response.status_code==200:
            print('join完了！')
            count2 += 1
        else:
            print('ルームが満員か、失敗')
    print('Spamします')
    count3 = 0
    while True:
        for token in tokens:
            count4 = 0
            while True:
                headers = {
                    'authority': 'asia-northeast1-godfield.cloudfunctions.net',
                    'accept': '*/*',
                    'accept-language': 'ja-JP,ja;q=0.9',
                    'authorization': f'Bearer {token}',
                    'content-type': 'application/json',
                    'origin': 'https://godfield.net',
                    'referer': 'https://godfield.net/',
                    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'cross-site',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                }
                json_data = {
                    'mode': 'open',
                    'roomId': id,
                    'text': f"{message}{count3}",
                }

                response = session.post('https://asia-northeast1-godfield.cloudfunctions.net/setComment', headers=headers, json=json_data)
                if response.status_code==200:
                    print('メッセージを送信しました')
                    count3 += 1
                    count4 += 1
                    if count4==3:
                        break
                    else:
                        continue # 内側のwhileループのみを抜けて、次のトークンに移る
                else:
                    print('失敗')
                    break
if input_data2 =="2":
    print('隠れ乱闘ねおけええー')
    heyaaikotoba = input('部屋の合言葉を入力してね～')
    message = input('メッセージを入力してください')
    print('ルームidを特定します')
    session = requests.Session()
    headers = {
        'authority': 'asia-northeast1-godfield.cloudfunctions.net',
        'accept': '*/*',
        'accept-language': 'ja-JP,ja;q=0.9',
        'authorization': f'Bearer {tokens[0]}',
        'content-type': 'application/json',
        'origin': 'https://godfield.net',
        'referer': 'https://godfield.net/',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }
    json_data = {
        'mode': 'hidden',
        'password': heyaaikotoba,
        'userName': accname,
    }

    response = requests.post('https://asia-northeast1-godfield.cloudfunctions.net/createRoom', headers=headers, json=json_data)
    roomid = response.json()['roomId']
    print(f'特定が完了しました。id:{roomid}')
    print('Join...')
    count2 = 0
    for token in tokens:
        headers = {
            'authority': 'asia-northeast1-godfield.cloudfunctions.net',
            'accept': '*/*',
            'accept-language': 'ja-JP,ja;q=0.9',
            'authorization': f'Bearer {token}',
            'content-type': 'application/json',
            'origin': 'https://godfield.net',
            'referer': 'https://godfield.net/',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        }
        json_data = {
            'mode': 'hidden',
            'roomId': f'{roomid}',
            'userName': f'{accname}{count2}',
        }
        response = session.post('https://asia-northeast1-godfield.cloudfunctions.net/addRoomUser', headers=headers, json=json_data)

        if response.status_code==200:
            print('join完了！')
            count2 += 1
        else:
            print('ルームが満員か、失敗')
            print(response)
            print(response.text)
    print('Spamします')
    count3 = 0
    while True:
        for token in tokens:
            count4 = 0
            while True:
                headers = {
                    'authority': 'asia-northeast1-godfield.cloudfunctions.net',
                    'accept': '*/*',
                    'accept-language': 'ja-JP,ja;q=0.9',
                    'authorization': f'Bearer {token}',
                    'content-type': 'application/json',
                    'origin': 'https://godfield.net',
                    'referer': 'https://godfield.net/',
                    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'cross-site',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                }
                json_data = {
                    'mode': 'hidden',
                    'roomId': roomid,
                    'text': f"{message}{count3}",
                }

                response = session.post('https://asia-northeast1-godfield.cloudfunctions.net/setComment', headers=headers, json=json_data)
                if response.status_code==200:
                    print('メッセージを送信しました')
                    count3 += 1
                    count4 += 1
                    if count4==3:
                        break
                    else:
                        continue # 内側のwhileループのみを抜けて、次のトークンに移る
                else:
                    print('失敗')
                    break
if input_data2 =="3":
    print('部屋作成ねおけえええー')
    roomids = []
    roomname = input('部屋の名前を入力してねー')
    count2 = 0
    session = requests.Session()
    for token in tokens:
        headers = {
            'authority': 'asia-northeast1-godfield.cloudfunctions.net',
            'accept': '*/*',
            'accept-language': 'ja-JP,ja;q=0.9',
            'authorization': f'Bearer {token}',
            'content-type': 'application/json',
            'origin': 'https://godfield.net',
            'referer': 'https://godfield.net/',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        }
        json_data = {
            'mode': 'open',
            'lang': 'ja',
            'userName': accname + str(count2),
        }

        response = session.post('https://asia-northeast1-godfield.cloudfunctions.net/createRoom', headers=headers, json=json_data)
        responsea = response.json()
        roomid = responsea['roomId']
        if response.status_code==200:
            print('作成完了！')
            roomids.append(roomid)
            count2 += 1
        else:
            print('失敗')
            print(response)
            print(response.text)
    print('部屋の名前を変更します。')
    count5 = 0
    for token, roomid in zip(tokens, roomids):
        headers = {
            'authority': 'asia-northeast1-godfield.cloudfunctions.net',
            'accept': '*/*',
            'accept-language': 'ja-JP,ja;q=0.9',
            'authorization': f'Bearer {token}',
            'content-type': 'application/json',
            'origin': 'https://godfield.net',
            'referer': 'https://godfield.net/',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        }
        json_data = {
            'mode': 'open',
            'roomId': roomid,
            'roomName': roomname + str(count5),
        }

        response = session.post('https://asia-northeast1-godfield.cloudfunctions.net/setRoomName', headers=headers, json=json_data)
        if response.status_code==200:
            print('変更完了！')
            count5 += 1
            print(roomname + str(count5))
        else:
            print('失敗')
            print(response)
            print(response.text)
            print(roomname + str(count5))
    print('公開設定にします！')
    for token, roomid in zip(tokens, roomids):
        headers = {
            'authority': 'asia-northeast1-godfield.cloudfunctions.net',
            'accept': '*/*',
            'accept-language': 'ja-JP,ja;q=0.9',
            'authorization': f'Bearer {token}',
            'content-type': 'application/json',
            'origin': 'https://godfield.net',
            'referer': 'https://godfield.net/',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        }
        json_data = {
            'mode': 'open',
            'roomId': roomid,
            'team': 0,
        }

        response = session.post('https://asia-northeast1-godfield.cloudfunctions.net/setEntryUser', headers=headers, json=json_data)
        if response.status_code==200:
            print('設定完了！')
        else:
            print('失敗')
            print(response)
            print(response.text)
    print('おわり')