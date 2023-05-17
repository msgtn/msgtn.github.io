#%%
links = '''

assets/photos/grad/DSCF6622.jpg

assets/photos/grad/FXP23897.jpg

assets/photos/grad/FXT24422-2.jpg

assets/photos/grad/FXT27030.jpg

assets/photos/grad/FXT27802.jpg

assets/photos/grad/FXP20023.jpg
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
# %%
