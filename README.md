# ehentai Favor Migrate

this is a project to migrate your favor item from e-hentai to exhentai

(if you require like e-hentai -> e-hentai, you can modify the code to finish the goal)

this project use **selenium** to simulate the whole process

please replace the **yourAccount** and **yourPassword** string in the files

the sequence of running these scripts is:

getBookURL.py -> replaceURL.ipynb -> AddFavorite.py



the result, the different type of books will be archived to different favorite folder in e-/xhentai

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
