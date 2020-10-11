# !/usr/bin/env python3
# -*- coding: utf-8 -*-


def expecation(value, toBe, desc=''):
    if desc != '':
        print(desc)
    if value is toBe:
        # 符合预期
        print('It is forecast for the result✔️')
    else:
        print('It is out of expectation❌')
    print()
