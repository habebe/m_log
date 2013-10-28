import os

os.system("mkdir -p DATA")

def get_rate(fileName):
    f = file(fileName,"r")
    data = f.read()
    data = eval(data)
    return data["data"]["rate"]
    
def generate_page_size():
    page_size_path = "log/IB/page_size"
    f = file("DATA/ib.page_size.data","w")
    for i in [12,13,14,15,16]:
        fileName = os.path.join(page_size_path,"p.{0}.benchmark.profile".format(i))
        rate = get_rate(fileName)
        print >>f,"{0},{1}".format(i,rate)
        pass
    f.close()
    pass

def generate_page_size_local():
    page_size_path = "log/LOCAL/page_size"
    f = file("DATA/local.page_size.data","w")
    for i in [12,13,14,15,16]:
        fileName = os.path.join(page_size_path,"p.{0}.benchmark.profile".format(i))
        if os.path.exists(fileName):
            rate = get_rate(fileName)
            print >>f,"{0},{1}".format(i,rate)
            pass
        pass
    f.close()
    pass


def generate_processes():
    path = "log/IB/processes"
    f = file("DATA/ib.processes.data","w")
    for i in [1,2,3,4,5,6,7,8]:
        rates = 0
        for j in xrange(i):
            fileName = os.path.join(path,"p.{0}.{1}.benchmark.profile".format(i,j+1))
            rate = get_rate(fileName)
            rates += rate
            pass
        print >> f,"{0},{1}".format(i,rates)
        pass
    f.close()
    pass

def generate_local_processes():
    path = "log/LOCAL/processes"
    f = file("DATA/local.processes.data","w")
    for i in [1,2,3,4,5,6,7,8]:
        rates = 0
        for j in xrange(i):
            fileName = os.path.join(path,"p.{0}.{1}.benchmark.profile".format(i,j+1))
            if os.path.exists(fileName):
                rate = get_rate(fileName)
                rates += rate
                pass
            pass
        if rates > 0:
            print >> f,"{0},{1}".format(i,rates)
            pass
        pass
    f.close()
    pass

generate_page_size()
generate_page_size_local()
generate_processes()
generate_local_processes()
