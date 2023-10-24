import requests
import json
import notify

#填写下面的信息，loca应填的数字请自行去和风官网查找，使用青龙自带的推送
api = "你的和风天气API key"
loca = "数字，代表你所在位置"
location = "经纬度，代表你所在的位置"

# 和风天气获取
api_url = f"https://devapi.qweather.com/v7/weather/now?location={loca}&key={api}"
apim_url = f"https://devapi.qweather.com/v7/minutely/5m?location={location}&key={api}"
apiw_url = f"https://devapi.qweather.com/v7/warning/now?location={loca}&key={api}"
apii_url = f"https://devapi.qweather.com/v7/indices/1d?type=3,5,7,13,14,16&location={loca}&key={api}"
apid_url = f"https://devapi.qweather.com/v7/weather/7d?location={loca}&key={api}"

response = requests.get(api_url)
data = json.loads(response.text)
fxLink = data['fxLink']
weather = data['now']
# 未来2小时每5分钟降雨预报
responsem = requests.get(apim_url)
datam = json.loads(responsem.text)
weatherm = datam['summary']
# 实时天气灾害预警
responsew = requests.get(apiw_url)
dataw = json.loads(responsew.text)
weatherw = dataw['warning']
# 天气生活指数预报
responsei = requests.get(apii_url)
datai = json.loads(responsei.text)
weatheri = datai['daily']
# 7 天的天气预报
responsed = requests.get(apid_url)
datad = json.loads(responsed.text)
weatherd = datad['daily']

if weatherw:
  tip = "预警：" + weatherw[0]['text']
else:
  tip = ""

#汇总信息
info = f"""
【预测】{weatherm}
【实时天气】
{weather['text']}，{weather['windDir']} {weather['windScale']} 级
温度：{weather['temp']}°C，体感温度：{weather['feelsLike']}°C
大家好，今天的天气播报员。
今天 {weatherd[0]['textDay']}，最低气温 {weatherd[0]['tempMin']}°C，最高气温 {weatherd[0]['tempMax']}，{weatherd[0]['windDirDay']}，{weatheri[0]['text']}
【紫外线指数】{weatheri[1]['text']}
【花粉过敏指数】{weatheri[2]['text']}
【晾晒指数】{weatheri[4]['text']}
{tip}
【未来 6 天的天气】
【{weatherd[1]['fxDate']}】{weatherd[1]['textDay']}，{weatherd[1]['tempMin']}-{weatherd[1]['tempMax']}°C，{weatherd[1]['windDirDay']}
【{weatherd[2]['fxDate']}】{weatherd[2]['textDay']}，{weatherd[2]['tempMin']}-{weatherd[2]['tempMax']}°C，{weatherd[2]['windDirDay']}
【{weatherd[3]['fxDate']}】{weatherd[3]['textDay']}，{weatherd[3]['tempMin']}-{weatherd[3]['tempMax']}°C，{weatherd[3]['windDirDay']}
【{weatherd[4]['fxDate']}】{weatherd[4]['textDay']}，{weatherd[4]['tempMin']}-{weatherd[4]['tempMax']}°C，{weatherd[4]['windDirDay']}
【{weatherd[5]['fxDate']}】{weatherd[5]['textDay']}，{weatherd[5]['tempMin']}-{weatherd[5]['tempMax']}°C，{weatherd[5]['windDirDay']}
【{weatherd[6]['fxDate']}】{weatherd[6]['textDay']}，{weatherd[6]['tempMin']}-{weatherd[6]['tempMax']}°C，{weatherd[6]['windDirDay']}
【详细天气信息】
{fxLink}"""

infot = f"""{weather['obsTime']}"""

notify.send(infot, info)
