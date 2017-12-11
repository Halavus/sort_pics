def get(cachefile):
    print "Reading the cache file"
    ls = []
    with open(cachefile,'r') as f:
        for i in f:
            ls.append(i.replace('\n',''))
    return ls

def add(cachefile, string):
    with open(cachefile,'a') as f:
        f.write('\n')
        f.write(string)
        print string+" cached"
