#%%
links = '''

assets/mpi_imgs/pictures/MJS_019_20230222_2990.jpg

assets/mpi_imgs/pictures/MJS_025_20230222_3117.jpg

assets/mpi_imgs/pictures/MJS_023_20230222_2975.jpg

assets/mpi_imgs/pictures/MJS_010_20230221_1602.jpg


'''

tag = ''
for link in links.split():
    # print(link)
    if 'jpg' not in link: continue
    # if len(link)<: continue
    _link = link.split()[-1]
    tag += (f'''
    <a data-lightbox="blossom" href="{_link}" width="95%">
        <img src="{_link}" width="95%">
    </a>\n
    ''')
# %%
print(tag)
# %%
