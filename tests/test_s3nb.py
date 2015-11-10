import datetime
from s3nb.jupyter4 import S3ContentsManager

def test_s3nb():
    s3cm = S3ContentsManager(s3_base_uri='s3://jorgemarsal-notebook/')
    dirs = s3cm.list_dirs('/')
    files = s3cm.list_files('/')
    notebooks = s3cm.list_notebooks()
    '''[D 11:11:00.302 NotebookApp] save: {'path': 'Untitled3.ipynb', 'model': {'type': 'notebook', 'content': {'cells': [], 'nbformat_minor': 0, 'metadata': {}, 'nbformat': 4}, 'writable': True, 'format': 'json', 'last_modified': datetime.datetime(2015, 11, 10, 19, 10, 58, 289524), 'name': 'Untitled3.ipynb', 'created': datetime.datetime(2015, 11, 10, 19, 10, 58, 289520), 'path': '/Untitled3.ipynb', 'mimetype': None}, 'self': <s3nb.jupyter4.S3ContentsManager object at 0x7f6e490a7048>}
[D 11:11:00.311 NotebookApp] _save_notebook: {'nb': {'cells': [], 'nbformat_minor': 0, 'metadata': {}, 'nbformat': 4}, 'path': 'Untitled3.ipynb', 'self': <s3nb.jupyter4.S3ContentsManager object at 0x7f6e490a7048>}
'''
    s3cm.save(path='Untitled3.ipynb',model={'type': 'notebook', 'content': {'cells': [], 'nbformat_minor': 0, 'metadata': {}, 'nbformat': 4}, 'writable': True, 'format': 'json', 'last_modified': datetime.datetime(2015, 11, 10, 19, 10, 58, 289524), 'name': 'Untitled3.ipynb', 'created': datetime.datetime(2015, 11, 10, 19, 10, 58, 289520), 'path': '/Untitled3.ipynb', 'mimetype': None})
    pass


