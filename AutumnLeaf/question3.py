import requests
import bs4

it = 0
x = requests.get('https://9gag.com')
while it < 6:
	if x:
		it += 1
		print("instance no.",it)
	print('instance elapsed time: ',x.elapsed)

page = bs4.BeautifulSoup(x.text, features="html.parser")
print('Site Name : ', page.title.text)

