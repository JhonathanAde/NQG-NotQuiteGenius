
export const createSong = async (title, image, lyrics) => {
  const response = await fetch('/api/songs/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      title,
      image,
      lyrics
    })
  });
//   const res = await response.json();
//   console.log("RESULT: ", res)
  return await response.json();
}

export const getSongs = async () => {
  const response = await fetch("/api/songs/")
  return await response.json();
}