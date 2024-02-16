import { useEffect, useState } from 'react';
import { fetchMovies } from '../utils/movieService';

interface Movie {
    id: string;
    title: string;
}

const MoviesPage = () => {
    const [movies, setMovies] = useState<Movie[]>([]);

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

export default MoviesPage;