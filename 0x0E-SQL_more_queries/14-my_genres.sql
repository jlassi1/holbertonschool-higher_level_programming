-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT tv_genres.name
FROM tv_genres
INNER JOIN tv_show_genres
INNER JOIN tv_shows
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_shows.title = 'Dexter'
GROUP BY name
ORDER BY name ASC;
