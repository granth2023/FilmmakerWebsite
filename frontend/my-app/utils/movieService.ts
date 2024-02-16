const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL;

export const fetchMovies = async () => {
    const response = await fetch(`${API_BASE_URL}/movies`);
    if (!response.ok) {
        throw new Error('Failed to fetch movies');
    }
    return response.json();
};