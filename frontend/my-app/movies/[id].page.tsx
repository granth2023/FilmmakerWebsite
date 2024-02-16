import { fetchMovieById } from '../utils/movieService';

export const getServerSideProps = async ({ params }) => {
    try {
        const movie = await fetchMovieById(params.id);
        return { props: { movie }};
    } catch (error) {
        return { props: { error: error.message}};
    }
};