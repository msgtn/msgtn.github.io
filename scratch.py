#%%
import os
links = '''

assets/photos/film/DSCF0820-2.jpg

assets/photos/film/DSCF1540-2.jpg

assets/photos/film/DSCF1684-2.jpg

assets/photos/film/DSCF0807.jpg

assets/photos/film/FXT28811.jpg

assets/photos/film/DSCF1823-2.jpg

assets/photos/film/DSCF1654-2.jpg

'''
links = '''
assets/photos/241103_nyc-marathon/mjps_001_picam_241103_151801.jpg


assets/photos/241103_nyc-marathon/mjps_002_picam_241103_150541.jpg

assets/photos/241103_nyc-marathon/mjps_003_picam_241103_173649.jpg

assets/photos/241103_nyc-marathon/mjps_004_picam_241103_153452.jpg

assets/photos/241103_nyc-marathon/mjps_005_picam_241103_171946.jpg

assets/photos/241103_nyc-marathon/mjps_006_picam_241103_175206.jpg

assets/photos/241103_nyc-marathon/mjps_007_picam_241103_180633.jpg

assets/photos/241103_nyc-marathon/mjps_008_picam_241103_181358.jpg

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
