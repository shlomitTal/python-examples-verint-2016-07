#commited by Shlomit
class Widget:
    def __init__(self, st):
        self.st = st
        self.myObjlist=[]
        self.myStrlist=[]
        self.doneBuild=0
        self.depSet = set()

    def add_dependency(self,*_list):
        for obj in _list:
            self.myObjlist.append(Widget(obj))
            st1= obj.st
            self.myStrlist.append(st1)

    def PreBuild(self, obj):
        list=[]
        if not obj.doneBuild:
            obj.doneBuild = 1
            st1 = obj.st.st
            self.depSet.add(st1)
            for a in obj.st.myObjlist:
                list.append(self.PreBuild(a))
               # 
           
        return list

    
    def build(self):
        uniqe = set()
        lis=[]
        for a in self.myObjlist:
            lis.append(self.PreBuild(a))
        return self.depSet

    
            



#luka =Widget("luka")
#hansolo =Widget("han solo")
#liea=Widget("leia")
#yoda=Widget("yoda")
#padam=Widget("padam amili")
#anakin=Widget("anakin sysler")
#obi=Widget("obi-wan")
#darth=Widget("darth vad")
#_all = Widget("All")
#luka.add_dependency(hansolo, liea,yoda)
#liea.add_dependency(padam,anakin)
#darth.add_dependency(anakin)
#_all.add_dependency(luka,hansolo,liea,yoda,padam,anakin,obi,darth)
#a = _all.build()
#print a