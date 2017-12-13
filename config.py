# coding=utf-8
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db') # путь к нашей базе данных
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository') # это папка, где мы будем хранить файлы SQLAlchemy-migrate

CSRF_ENABLED = True #активирует предотвращение поддельных межсайтовых запросов
SECRET_KEY = '12345'
OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]