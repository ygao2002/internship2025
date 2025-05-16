import requests

url = "https://api.va.landing.ai/v1/tools/agentic-object-detection"
files = {
    "image": open("cars.png", "rb")  # 图像路径
}
data = {
    "prompts": "a yellow car",  # 目标描述
    "model": "agentic"
}
headers = {
    "Authorization": "Basic MGZ1bDNxMDZ6dHc2N2p5ZmR0NDBlOnFUSnFYQ2V6d3dsQUdiRFdWSjh4VzljWWpqcEFleFBC"  # API_KEY
}

response = requests.post(url, files=files, data=data, headers=headers)

# 输出结果
print(response.json())
