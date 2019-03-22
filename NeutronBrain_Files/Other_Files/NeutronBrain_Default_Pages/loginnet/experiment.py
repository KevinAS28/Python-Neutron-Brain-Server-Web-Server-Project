import os
def file_reader(name, mode="rb"):
    with open(name, mode) as baca:
        return baca.readlines()
class POST_page:
    def __init__(self, berkas):
        #cuma ke init filenya kok...
        #self.init_page = os.path.split(berkas)[-1] + default_web_page_extension
        self.init_page = berkas
        #berkas = os.path.join(berkas, self.init_page)
        self.data = file_reader(berkas, "r")
        #auto detect variable in web page
        with open(self.init_page, "r") as oke:
            eko = oke.read().split("\n")
            oke = oke.readlines()
        line_post_characteristic = ["input", "name"]
        post_characteristic = ["form"]
        possibilty = 0
        #check line per line
        for i in eko:
         for a in list_post_characteristic:
          if a in i:
           possibilty += 1
        #check all
         for a in post_characteristic:
          if a in oke:
           possibilty += 1        
    def get_input(self, data):
            print("data from get input function")

POST_page("loginnet.html")
