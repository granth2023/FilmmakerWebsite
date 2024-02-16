import { useEffect, useState } from 'react';
import { fetchMovies } from '../utils/movieService';

const MoviesPage = () => {
    const [movies, setMovies] = useState([]);

    useEffect(() => {
        fetchMovies().then(setMovies).catch(console.error);
    }, []);
    