
export const createSong = async (payload) => {
  const response = await fetch('/api/songs/', {
    method: 'POST',
    // headers: {
    //   'Content-Type': 'application/json'
    // },
    body: payload
  });
//   const res = await response.json();
//   console.log("RESULT: ", res)
  return await response.json();
}

export const getSongs = async () => {
  const response = await fetch("/api/songs/")
  return await response.json();
}