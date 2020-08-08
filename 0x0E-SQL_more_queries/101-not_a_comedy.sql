-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT title
FROM tv_shows
WHERE id NOT IN (SELECT show_id FROM tv_show_genres AS sg JOIN
      tv_genres AS g ON g.id = sg.genre_id WHERE g.name = 'Comedy')
GROUP BY title
ORDER BY title ASC;
