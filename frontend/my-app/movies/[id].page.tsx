import { fetchMovieById } from '../utils/movieService';

export const getServerSideProps = async ({ params }) => {
    try {

    } catch (error) {
        return { props: { error: error.message}};
    }
};