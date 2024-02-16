import { fetchMovieById } from '../utils/movieService';

export const getServerSideProps = async ({ params }) => {
    try {
        const movie = await fetchMovieById(params.id);

    } catch (error) {
        return { props: { error: error.message}};
    }
};