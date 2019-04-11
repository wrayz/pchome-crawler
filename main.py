from custom_crawler.pchome import PChome

pchome = PChome('xxx')
page = pchome.get_page()

print(page.prettify())
