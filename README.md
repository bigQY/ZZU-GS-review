# 项目说明

该脚本用于郑州大学研究生平台一键评教

## 使用方法

1. 获取authToken
   控制台执行``` localStorage.getItem('USER_TOKEN') ```
   ![image](https://github.com/bigQY/ZZU-GS-review/assets/52437374/f8a1a598-fdc5-4795-b7da-b226016a92ad)
2. 修改```main.py```中的参数
   ```python
    # 用于身份验证的token，自己抓包获取
    # 登录之后控制台执行 localStorage.getItem('USER_TOKEN') 也可以获取，注意去掉多余的引号
    authToken ='Bearer eyJhbGxxxxxxxxxxxxxxx.xxxxxxxxxxxxxxxxxx.xxxxxxxxxxxxxxxxxxxxxxxxxxx'
    # 用于筛选课程的参数，kkxn为学年，kkxqm为学期，其他参数不用管
    kcListSelect = 'kkxn=2023-2024&kkxqm=2&pageNo=1&pageSize=1000&pageNum=1&'
    # 分数，范围0-100，但是实际上可以是0-999
    score = '999'
   ```
    


## 贡献指南

- 如果您发现了bug，请提交issue
- 如果您有改进的建议，请提交pull request
