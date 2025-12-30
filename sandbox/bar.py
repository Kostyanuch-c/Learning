import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

results = cur.execute('''
-- Вернуть поле title из таблицы video_products и поле title из original_titles
SELECT video_products.title,
       original_titles.title
-- ...из двух таблиц
FROM video_products,
     original_titles
-- Выводить только те значения полей, для которых верно условие
WHERE video_products.original_title_id = original_titles.id;
''')

print(*results, sep='\n')
con.commit()
con.close()