#%%
links = '''

assets/photos/film/DSCF0820-2.jpg

assets/photos/film/DSCF1540-2.jpg

assets/photos/film/DSCF1684-2.jpg

assets/photos/film/DSCF0807.jpg

assets/photos/film/FXT28811.jpg

assets/photos/film/DSCF1823-2.jpg

assets/photos/film/DSCF1654-2.jpg

'''

tag = ''
for link in links.split():
    # print(link)
    if 'jpg' not in link: continue
    # if len(link)<: continue
    _link = link.split()[-1]
    tag += (f'''
    <a data-lightbox="img" href="{_link}" width="95%">
        <img src="{_link}" width="95%">
    </a>\n
    ''')
# %%
print(tag)
with open('.scratch.txt','w') as _file:
    _file.write(tag)
# %%
