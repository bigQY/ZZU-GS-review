import requests

# 用于身份验证的token，自己抓包获取
# 登录之后控制台执行 localStorage.getItem('USER_TOKEN') 也可以获取，注意去掉多余的引号
authToken ='Bearer eyJhbGxxxxxxxxxxxxxxx.xxxxxxxxxxxxxxxxxx.xxxxxxxxxxxxxxxxxxxxxxxxxxx'
# 用于筛选课程的参数，kkxn为学年，kkxqm为学期，其他参数不用管
kcListSelect = 'kkxn=2023-2024&kkxqm=2&pageNo=1&pageSize=1000&pageNum=1&'
# 分数，范围0-100，但是实际上可以是0-999
score = '999'

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'authorization': authToken,
    'content-type': 'application/x-www-form-urlencoded',
    'dnt': '1',
    'origin': 'https://gs2.v.zzu.edu.cn',
    'priority': 'u=1, i',
    'referer': 'https://gs2.v.zzu.edu.cn/stu/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
}

def PingJiao(tkxsmdId,score='999'):
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'authorization': authToken,
    'content-type': 'application/json',
    'dnt': '1',
    'origin': 'https://gs2.v.zzu.edu.cn',
    'priority': 'u=1, i',
    'referer': 'https://gs2.v.zzu.edu.cn/stu/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
    }
    json_data = {
        'tkxsmdId': tkxsmdId,
        'pjnl': '无',
        'dfList': [
            {
                'kcpjzbId': 'PJ01',
                'dfList': [
                    {
                        'kcpjzbId': 'PJ0101',
                        'df': score,
                    },
                    {
                        'kcpjzbId': 'PJ0102',
                        'df': score,
                    },
                    {
                        'kcpjzbId': 'PJ0103',
                        'df': score,
                    },
                    {
                        'kcpjzbId': 'PJ0104',
                        'df': score,
                    },
                    {
                        'kcpjzbId': 'PJ0105',
                        'df': score,
                    },
                ],
            },
            {
                'kcpjzbId': 'PJ02',
                'dfList': [
                    {
                        'kcpjzbId': 'PJ0201',
                        'df': score,
                    },
                    {
                        'kcpjzbId': 'PJ0202',
                        'df': score,
                    },
                    {
                        'kcpjzbId': 'PJ0203',
                        'df': score,
                    },
                    {
                        'kcpjzbId': 'PJ0204',
                        'df': score,
                    },
                ],
            },
            {
                'kcpjzbId': 'PJ03',
                'dfList': [
                    {
                        'kcpjzbId': 'PJ0301',
                        'df': score,
                    },
                    {
                        'kcpjzbId': 'PJ0302',
                        'df': score,
                    },
                    {
                        'kcpjzbId': 'PJ0303',
                        'df': score,
                    },
                    {
                        'kcpjzbId': 'PJ0304',
                        'df': score,
                    },
                    {
                        'kcpjzbId': 'PJ0305',
                        'df': score,
                    },
                ],
            },
            {
                'kcpjzbId': 'PJ04',
                'dfList': [
                    {
                        'kcpjzbId': 'PJ0401',
                        'df': score,
                    },
                    {
                        'kcpjzbId': 'PJ0402',
                        'df': score,
                    },
                    {
                        'kcpjzbId': 'PJ0403',
                        'df': score,
                    },
                    {
                        'kcpjzbId': 'PJ0404',
                        'df': score,
                    },
                    {
                        'kcpjzbId': 'PJ0405',
                        'df': score,
                    },
                ],
            },
        ],
    }
    response = requests.post('https://gs2.v.zzu.edu.cn/api/studentClient/kcpjzbXs/add', headers=headers, json=json_data)
    return response.json()

if __name__ == '__main__':
    response = requests.post('https://gs2.v.zzu.edu.cn/api/studentClient/kcpjzbXs/list', headers=headers, data=kcListSelect)
    responseJson = response.json()
    kcList = responseJson['data']['rows']
    for kc in kcList:
        print(kc['tkxsmdId'])
        print(kc['kcmc'])
        print(PingJiao(kc['tkxsmdId'],score=score))