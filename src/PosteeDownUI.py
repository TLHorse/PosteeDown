import ui
from console import hud_alert

import Spider818ps as 818ps
import mobilePaths as mpath
import HelpDoc as HD

def downloadAction(sender):
	v = sender.superview
	keyword = v['searchTF'].text
	number = int(v['numTF'].text)
	path = v['pathTF'].text
	suffix = v['suffixTF'].text
	isTest = v['testSW'].value
	v['recordText'].text = ""
	
	if path == "/路径/示例":
		path = mpath.kAppPath('PosteeDown/下载的手抄报/')
		
	downloader = 818ps.Spider818ps()
	downloader.keyword = keyword
	downloader.path = path
	downloader.count = number
	downloader.suffix = suffix
	downloader.isTest = isTest
	downloader.download()
	
	if isTest == False:
		hud_alert('下载成功')
		v['recordText'].text = "\n".join(downloader.images)
	else:
		hud_alert('测试成功')
		v['recordText'].text = "".join(downloader.images)

def clearRecord(sender):
	v = sender.superview
	v['recordText'].text = ""
	
def helpAction(sender):
	v = sender.superview
	clearRecord(v['clearRecordBT'])
	help = HD.helpDoc
	v['recordText'].text = v['recordText'].text + help
	
v = ui.load_view('PosteeDownUI')

if ui.get_screen_size()[1] >= 768:
	# iPad
	v.present('sheet')
else:
	# iPhone
	v.present()
