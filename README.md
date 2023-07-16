# GetQPlayerUid
一套超级简单的通过「玩家qq」获取「玩家uid」的方案，基于http协议

示例代码：

保存绑定
`py
def save_data(user_id, uid, server):
  url = 'http://127.0.0.1:17140/api/data?mode=save&user_id={}&uid={}&server={}'.format(user_id, uid, server)
  response = requests.get(url)
  return response.text`
  
获取数据
`py
def get_data(user_id, server):
  url = 'http://127.0.0.1:17140/api/data?mode=get&user_id={}&server={}'.format(user_id, server)
  response = requests.get(url)
  print(response.text)
  return response.text`
