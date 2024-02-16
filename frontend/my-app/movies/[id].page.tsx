import { fetchMovie } from '../utils/movieService';
import { GetServerSideProps } from 'next';
import { ParsedUrlQuery} from 'querystring';


interface IParams extends ParsedUrlQuery {
    id: string;
}

interface Movie {
    id: string;
    title: string;
}

interface MovieDetailProps {
    movie?: Movie;
    error?: string;
}

export const getServerSideProps: GetServerSideProps = async (context) => {
    const { id } = context.params as IParams;
    
    try {
      const movie = await fetchMovie;
      return { props: { movie } };
    } catch (error) {
      return { props: { error: (error as Error).message } };
    }
  };
const MovieDetailPage = ({ movie, error }: MovieDetailProps ) => {
    if (error) {
        return <div>Error: {error}</div>
    }
    return (
        <div> 
            <h1>{movie?.title}</h1>
            
        </div>
    )
}

export default MovieDetailPage;