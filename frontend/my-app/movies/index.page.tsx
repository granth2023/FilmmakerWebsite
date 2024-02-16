import { useEffect, useState } from 'react';
import { fetchMovies } from '../utils/movieService';

const MoviesPage = () => {
    const [movies, setMovies] = useState([]);

    useEffect(() => {
        fetchMovies().then(setMovies).catch(console.error);
    }, []);

    return ( 
        <div>
            <h1>Movies</h1>
            <ul>
                {movies.map(movies => (
                    <li key={movies.id}>{movies.title}</li>
                ))}
            </ul>
        </div>
    );
};