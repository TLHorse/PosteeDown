<p align="center"><img src="https://raw.githubusercontent.com/TLHorse/PosteeDown/master/img/PDPNGIcon.png" alt="PosteeDown" width="100" height="100"></p>

# PosteeDown

A classic integrated handwritten-poster downloader, in **Chinese**.

# Scenarios
- When you want to draw a poster but you've got no idea;
- When your teacher/boss let you draw a poster but you don't want to.

# Usage

## Preparation
- An iPhone/iPad. You can run on a computer, though.
- Pythonista (or any software that can run Python 3) installed.

## Step
1. Clone or download this project, and delete everything except the 'src' directory.
2. Import 'src' into Pythonista, then rename 'src' to 'PosteeDown'.
3. Run 'PosteeDownUI.py', then a GUI window will popup.
4. Change arguments by manipulating the `TextField` and the `Button`s.
5. Tap download to download, and you can see the images in directory `~/下载的手抄报`.

If you are not running in iOS, then you can call the download function manually, but please note that you need to change the download path in the code. (MobilePaths.py)

# Todo
- Adapt computers.
- Change `.pyui` framework to PySimpleGUI.
- Not only crawl the images, but generate it.
