import requests
import re
from fake_useragent import UserAgent

class SpiderOoopic:
	
	def __init__(self, keyword = '', count = 1, path = '', suffix = 'jpg', isTest = False, condition = ""):
		self.keyword = ''
		self.count = 1
		self.path = ''
		self.suffix = 'jpg'
		self.isTest = False
		self.condition = ''
		self.images = []
		
	def println(self, list):
		for i in list:
			print(i, "\n")
	
	def download(self):
		
		# 进入搜索后的浏览页面处理
		headers = {
			'User-Agent': UserAgent().ie
		}
		
		requester1 = requests.get(
			"https://so.ooopic.com/search-%s-117-0_0_pres_0__97_ooo_0_1_.html" % self.keyword,
			headers = headers
		)
		requester1.encoding = 'GBK'
		
		# 网站图片序列号过滤&生成列表
		imageExp1 = 'href="https://weili.ooopic.com/weili_(.*?).html"'
		imageSerialList = re.compile(imageExp1).findall(requester1.text)
		imageSerialList = list(set(imageSerialList))
		
		# 搜索结果的每一个链接的列表
		imageURLList = []
		
		try:
			# 填充列表
			for img in range(self.count):
				URLstr = "https://weili.ooopic.com/weili_%s.html" % imageSerialList[img]
				imageURLList.append(URLstr)
		except IndexError:
			# 错误处理（数组越界错误）
			print('数量过多！')
		
		# 进入搜索后单一图片链接开始处理
		
		# 循环爬取上一个步骤中的每张图片的详细网页
		for imgNum in range(self.count): 
			requester2 = requests.get(
				imageURLList[imgNum],
				headers = headers,
			)
			requester2.encoding = 'GBK'
			
			# 过滤每张图片的详细网页中，带有bpic cdn的图片
			imageExp2 = 'src="//bpic.wotucdn.com/(.*?)"'
			imageInHTMLList = re.compile(imageExp2).findall(requester2.text)
			imageInHTMLList = list(set(imageInHTMLList))
			
			# 把列表中的每一个url补充完整
			for i in range(len(imageInHTMLList)):
				imageInHTMLList[i] = "https://bpic.wotucdn.com/" + imageInHTMLList[i]
				
			self.println(imageInHTMLList)
			
			# 使用循环来尝试解析上一步爬到的每个图片URL
			for imgUrlIndex in range(len(imageInHTMLList)):
				RefererHeader = {
					'User-Agent': UserAgent().ie,
					'Referer': imageURLList[imgNum],
					# 'Content-Type': 'application/x-www-form-urlencoded'
				}
				requester3 = requests.get(
					imageInHTMLList[imgUrlIndex],
					headers = headers
				)
				requester3.encoding = 'GBK'
				print(requester3.text)
			
		
d = SpiderOoopic()
d.keyword = 'b4babdda'
d.count = 1
d.download()
