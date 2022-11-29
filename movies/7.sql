select title, rating from movies
JOIN ratings on movies.id = ratings.movie_id
where year =2010 order by rating desc, title;