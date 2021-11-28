import xml.sax
 
class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData=""
        self.width=""
        self.height=""
        self.xmin=""
        self.ymin=""
        self.xmax=""
        self.ymax=""
    def startElement(self, tag, attributes):
        self.CurrentData = tag

   # 元素结束事件处理
    def endElement(self, tag):
        if self.CurrentData=="width":
            print("width:", self.width)
        elif self.CurrentData=="height":
            print("height:", self.height)
        elif self.CurrentData=="xmin":
            print("xmin:", self.xmin)
        elif self.CurrentData=="ymin":
            print("ymin:", self.ymin)
        elif self.CurrentData=="xmax":
            print("xmax:", self.xmax)
        elif self.CurrentData=="ymax":
            print("ymax:", self.ymax)
        self.CurrentData=""
 
   # 内容事件处理
    def characters(self, content):
        if self.CurrentData=="width":
            self.width=content
        elif self.CurrentData=="height":
            self.height=content
        elif self.CurrentData=="xmin":
            self.xmin=content
        elif self.CurrentData=="ymin":
            self.ymin=content
        elif self.CurrentData=="xmax":
            self.xmax=content
        elif self.CurrentData=="ymax":
            self.ymax=content
  
if ( __name__ == "__main__"):
   
   # 创建一个 XMLReader
    parser=xml.sax.make_parser()
   # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
 
   # 重写 ContextHandler
    Handler=MovieHandler()
    parser.setContentHandler( Handler )
   
    parser.parse("000001.xml")
