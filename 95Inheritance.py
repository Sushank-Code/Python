class Website:                           # single Inheritance
    web = "Google.com"

    def showDetail(self):
        print("This is Website")

class app(Website):
    app = "Youtube"

    def printDetail(self):
        print("This is app")

    # def showDetail(self):
    #     print("This is Dynamic Website")

w=Website()
# w.showDetail()

a=app()
a.showDetail()
print(a.web)