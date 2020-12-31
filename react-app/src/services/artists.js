export const getArtists = async () => {
  const response = await fetch("/api/artists/")
  return await response.json();
}

export const getArtist = async (id) => {
    const response = await fetch(`/api/artists/${id}`)
    return await response.json();
}

export const createArtist = async (payload) => {
    const response = await fetch('/api/artists/', {
        method: 'POST',
        body: payload
    })
    return await response.json();
}