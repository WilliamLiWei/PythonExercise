from HTMLParser import HTMLParser
# markupbase

class MyParser(HTMLParser):
    def handle_decl(self, decl):
        HTMLParser.handle_decl(self, decl)
        print('handle_decl: %s' % decl)

    def handle_starttag(self, tag, attrs):
        HTMLParser.handle_starttag(self, tag, attrs)
        print('handle_starttag:  <' + tag + '>')

    def handle_endtag(self, tag):
        HTMLParser.handle_endtag(self, tag)
        print('handle_endtag: </' + tag + '>')

    def handle_data(self, data):
        HTMLParser.handle_data(self, data)
        print('handle_data: %s' % data)

    #<br/>
    def handle_startendtag(self, tag, attrs):
        HTMLParser.handle_startendtag(self, tag, attrs)
        print("handle_startendtag:%s" % tag)

    def handle_comment(self, data):
        HTMLParser.handle_comment(self, data)
        print('handle_comment: %s' % data)

    def close(self):
        HTMLParser.close(self)
        print('Close')

demo = MyParser()
demo.feed(open('test.html').read())
demo.close()
