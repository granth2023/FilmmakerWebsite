import { fetchMovieById } from '../utils/movieService';
import { GetServerSideProps } from 'next';

interface Movie {
    id: string;
    title: string;
}

interface MovieDetailProps {
    movie?: Movie;
    error?: string;
}


export const getServerSideProps: GetServerSideProps = async ({ params }) => {
    if (typeof params?.id === 'string'){
    try {
        const movie = await fetchMovieById(params.id);
        return { props: { movie }};
    } catch (error) {
        return { props: { error: error.message}};
    }
};
};
const MovieDetailPage = ({ movie, error }: MovieDetailProps ) => {
    if (error) {
        return <div>Error: {error}</div>
    }
    return (
        <div> 
            <h1>{movie.title}</h1>
            
        </div>
    )
}