# -*- coding:utf-8 -*-
# @FileName  :myhtml.py
# @Time      :2023/12/16 13:47
# @Author    :dzz
# @Function  :
from flask import Blueprint

myhtml = Blueprint('myhtml', __name__)


@myhtml.route('/template01')
def template01():
    resp = '''
    <ul>
        <li>1</li>
        <li>2</li>
        <li>3</li>
    </ul>
    '''
    return resp


@myhtml.route('/template02')
def template02():
    username = "woniu"
    resp = '''
    <ul>
        <li>1</li>
        <li>2</li>
        <li>%s</li>
    </ul>
    ''' % username
    return resp


@myhtml.route('/template03')
def template03():
    username = "woniu"
    with open('template/myhtml.html', encoding='utf-8') as file:
        html = file.read()
    return html


@myhtml.route('/template04')
def template04():
    username = "woniu"
    with open('template/myhtml.html', encoding='utf-8') as file:
        html = file.read()
    return html.replace('{{username}}', username)


if __name__ == "__main__":
    run_code = 0
