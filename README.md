# Ehentai Favor Migrate / E站账号收藏迁移

***using python version: 3.7***

this is a project to migrate your favor item from e-hentai to exhentai

(if you require like e-hentai -> e-hentai, you can modify the code to finish the goal)

this project use **selenium** to simulate the whole process

please replace the **yourAccount** and **yourPassword** string in the files (getBookURL.py and AddFavorite.py)

the sequence of running these scripts is:

getBookURL.py -> replaceURL.ipynb -> AddFavorite.py



As the result, the different type of books will be archived to different favorite folder in e-/xhentai

| Tag       | favorites |
| --------- | --------- |
| Doujinshi | favorite0 |
| Manga     | favorite1 |
| Artist CG | favorite2 |
| Game CG   | favorite3 |
| Western   | favorite4 |
| Non-H     | favorite5 |
| Image Set | favorite6 |
| Cosplay   | favorite7 |
| Misc      | favorite8 |

you can modify this mapping in **favorMap.txt**

该脚本使用selenium帮助您迁移您的E站收藏到目标账号的收藏夹中（表站->里站您也可以自行修改代码以实现表站->表站，里站->里站）
