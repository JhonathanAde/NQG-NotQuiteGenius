
export const createSong = async (payload) => {
  const response = await fetch('/api/songs/', {
    method: 'POST',
    body: payload
  });

  return await response.json();
}

export const editSong = async (payload, id) => {
  const response = await fetch(`/api/songs/${id}`, {
    method: 'PATCH',
    body: payload
  });

  return await response.json();
}

export const getSongs = async () => {
  const response = await fetch("/api/songs/")
  return await response.json();
}

export const annotate = async (songId, payload) => {
  const response = await fetch(`/api/songs/${songId}/annotations`,{
    method: 'POST',
    body: payload
  });

  return await response.json();
}