from scrapy import cmdline
name = 'tutorial'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())