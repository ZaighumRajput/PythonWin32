# coding: utf-8
import os, stat, time
os.stat('c:\\')
def getfileinfo(filename)
def getfileinfo(filename):
    stats = os.stat(filename)
    size = stats[sat.ST_SIZE]
    print 'File size is %d bytes' % size
    accessed = stats[stat.ST_ATIME]
    modified = stats[stat.ST_MTIME]
    print 'Last accessed: ' + time.ctime(accessed)
    print 'Last modified: ' + time.ctime(modified)
    
stats = os.stat('c:\\')
stats[stat.ST_SIZE]
getfileinfo('C:\\')
get_ipython().magic(u'save 1-8')
