import requests
content= requests.get("https://raw.githubusercontent.com/shailu-coder/checkerss/master/head.py").text
print(content)
if content != "hello world!!":
    with open("code_changer.py", "w") as file:
        file.write(content)
else:
    print("safe")
