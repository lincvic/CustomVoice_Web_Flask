# -*- coding: utf-8 -*-
# @Time    : 2018/7/29 14:49
# @Author  : Lincvic
# @Email   : lincvic@yahoo.com
# @File    : custom_voice_Config.py
# @SoftwareName: PyCharm
import uuid

# CustomVoice Endpoint
URL = "https://westus.voice.speech.microsoft.com/cognitiveservices/v1?deploymentId=25279e50-f61d-481e-a0e2-761ffc066dad"

# 认证地址
HOST_NAME = "https://westus.api.cognitive.microsoft.com/sts/v1.0/issueToken"

# Azure speech SUB Key
SUB_KEY = "a37bd3a0a56746efaf342f1f311ce079"

# 返回的音频编码格式
ENCODE_TYPE = "audio-16khz-32kbitrate-mono-mp3"

#GUID
GUID = str(uuid.uuid1())



