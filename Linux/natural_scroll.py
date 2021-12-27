#!/usr/bin/python3
import os
import re

def get_pointers():
    p = os.popen('xinput list')
    res = p.read()
    lines = res.split('\n')
    ret = {}
    pt = False
    re_id = re.compile(r'id=(\d+)')
    for s in lines:
        if 'pointer' in s:
            pt = True
        elif 'keyboard' in s:
            pt = False
        if pt and (('id=' in s)):
            g = re_id.search(s)
            if g:
                ret[g.group(1)] = s
    return ret

def get_natural(id):
    p = os.popen('xinput list-props ' + id)
    res = p.read()
    lines = res.split('\n')
    re_id = re.compile(r'Natural Scrolling Enabled \((\d+)\)')
    for s in lines:
        g = re_id.search(s)
        if g:
            return g.group(1)
    return None

def set_natural(id, key, val):
    p = os.popen('xinput set-prop ' + id + ' ' + key + ' ' + str(val))
    res = p.read()

if __name__ == '__main__':
    r = get_pointers()
    print(r)
    print('start')
    for id in r:
        natural = get_natural(id)
        if natural:
            print('set', id, r[id])
            set_natural(id, natural, 1)
            
    print('done')
