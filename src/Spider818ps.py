# PosteeDown | 海报下载器
# 作者：马天来
# 于2020年1月19日创建

import urllib.request
import re
from termcolor import colored, cprint
import mobilePaths as mpath
from xpinyin import Pinyin

class Spider818ps:
	
	def __init__(self, keyword = '', count = 1, path = '', suffix = 'jpg', isTest = False, condition = ""):
		self.keyword = ''
		self.count = 1
		self.path = ''
		self.suffix = 'jpg'
		self.isTest = False
		self.condition = ''
		self.images = []
	
	def infoIsCorrect(self, printReason = False):
		if printReason == False:
			if self.keyword == '' or type(self.count) != int or self.path == '' or self.suffix == '' or self.condition != '':
				return False
			else:
				return True
		else:
			correct = True
			if self.keyword == '':
				cprint('Reason: ', 'red', end = '')
				print('Keyword missing', end = ' / ')
				correct = False
			if type(self.count) != int:
				print('Count error', end = ' / ')
				correct = False
			if self.suffix == '':
				print('Missing suffix', end = ' / ')
				correct = False
			if self.path == '':
				print('Path missing', end = ' / ')
				correct = False
			if self.condition != '':
				print('Condition shoud be nil while initializing')
				correct = False
			
			return correct
			
	def download(self):
		global condition
		condition = ""
		# 定义爬取信息
		pinyin = Pinyin().get_pinyin(self.keyword)
		pinyinList = pinyin.split("-")
		keywordPinyin = "".join(pinyinList)
		URLToScrap = "https://818ps.com/muban/0-0-0-0-%s-null-52_24_0_0-0-0-0.html?route_id=&route=&after_route=" % str(keywordPinyin)
		URLData = urllib.request.urlopen(URLToScrap).read().decode("utf-8", "ignore")
		imageExp = "/pic/(.*?).html"
		imageURLList = re.compile(imageExp).findall(URLData)
		imageURLList = list(set(imageURLList))
		
		# 处理信息填写及错误
		if len(imageURLList) == 0:
			print("没有搜索到相关海报")
			condition = "img:none"
		elif self.count > len(imageURLList):
			print("数量过多\n最多%s张" % len(imageURLList))
			condition = "img:overflow"
		elif not self.infoIsCorrect():
			print('下载信息填写错误！')
			condition = "info:error"
			print(infoIsCorrect(printReason = True))
		else:
			# 网站请求错误处理
			try:
				# 重复下载需要的图片
				imageCount = self.count
				if self.count == 0: # 规则：如果数量为0，下载全部
					imageCount = len(imageURLList)
					
				for imgSerial in range(imageCount):
					imgNumber = str(imageURLList[imgSerial])
					detailImgURL = "https://818ps.com/detail/" + imgNumber + ".html"
					detailData = urllib.request.urlopen(detailImgURL).read().decode("utf-8", "ignore")
					detailImageExp = 'https://img.tuguaishou.com/ips_templ_preview/(.*?)"'
					detailImgURLArg = re.compile(detailImageExp).findall(detailData)
					
					for i in range(len(detailImgURLArg)):
						finalImageURL = "https://img.tuguaishou.com/ips_templ_preview/" + str(detailImgURLArg[i])
						finalImgFileID = str(imgSerial) + '-' + str(imgNumber)
						print("正在下载：编号为%s的图片..." % finalImgFileID)
						
						# 保存图片
						file = self.path + str(self.keyword) + "-" + finalImgFileID + "." + self.suffix
						if self.isTest == False:
							self.images.append(file)
							urllib.request.urlretrieve(finalImageURL, filename = file)
							print("下载完成！目录：", file)
						else:
							print("测试完成！测试伪目录：", file)
			# 错误处理
			except urllib.error.URLError as e:
				if hasattr(e, 'code'):
					print(e.code)
				if hasattr(e, "reason"):
					print(e.reason)
