import xml.sax, xml.sax.handler
class SaxHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.name = ""
        self.price = ""
        self.supplier = ""
        self.article= {}
        
    def startElement(self,tag,attributes):
        self.CurrentData = tag
        if tag == "article":
            print("--Article--")
            name1 = attributes["id"]
            print("ID: ",name1)
    def endElement(self,tag):
        if self.CurrentData == "name":
            print("Name: ",self.name)
        elif self.CurrentData == "price":
            print("Price: ", self.price)
        elif self.CurrentData =="supplier":
            print("Supplier: ", self.supplier)
        self.CurrentData = ""
    def charecters(self, content):
        if self.CurrentData == "name":
            self.name = content
        elif self.CurrentData == "price":
            self.price = content
        elif self.CurrentData =="supplier":
            self.supplier = content
if (__name__ == "__main__"):
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    Handler = SaxHandler()
    parser.setContentHandler(Handler)
    
    parser.parse("example.xml")
  





