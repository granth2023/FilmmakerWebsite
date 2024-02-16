const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL;

export const fetchMovies = async (id: string) => {
    const response = await fetch(`${API_BASE_URL}/movies/${id}`);
    if (!response.ok) {
        throw new Error('Failed to fetch movies');
    }
    return response.json();
};