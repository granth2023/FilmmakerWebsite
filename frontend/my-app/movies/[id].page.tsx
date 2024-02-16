import { fetchMovieById } from '../utils/movieService';

export const getServerSideProps = async ({ params }) => {
    try {
        const movie = await fetchMovieById(params.id);
        return { props: { movie }};
    } catch (error) {
        return { props: { error: error.message}};
    }
};

const MovieDetailPage = ({ movie, error }) => {
    if (error) {
        return <div>Error: {error}</div>
    }
    return (
        <div> 
            <h1>{movie.title}</h1>
            
        </div>
    )
}