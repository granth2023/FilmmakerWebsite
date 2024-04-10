const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL;

 interface Movie {
    id: string;
    title: string;
 }
export const fetchMovie = async (): Promise<Movie[]> => {
    const response = await fetch(`${API_BASE_URL}/movies/`);
    if (!response.ok) {
        throw new Error('Failed to fetch movies');
    }
    return response.json();
};