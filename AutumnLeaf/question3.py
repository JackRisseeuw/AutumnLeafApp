import requests
import bs4

times = 0
site = requests.get('https://9gag.com')
while times < 6:
	if site:
		times += 1
		print("instance no.",times)
	print('instance elapsed time: ',site.elapsed)

page = bs4.BeautifulSoup(site.text, features="html.parser")
print('Site Name : ', page.title.text)

