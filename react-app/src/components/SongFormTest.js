import React, { useState } from "react";
import { Redirect } from "react-router-dom";
import { createSong, editSong } from "../services/song";

const SongForm = () => {
  const [errors, setErrors] = useState([]);
  const [title, setTitle] = useState("");
  const [artistId, setArtistId] = useState("");
  const [lyrics, setLyrics] = useState("");
  const [image, setImage] = useState("");
  const [audioFile, setAudioFile] = useState("");

  const songDataSubmitHandler = async (e) => {
    e.preventDefault();
    console.log("ARTIST ID", artistId)
    const data = new FormData();

    data.append('title', title);
    data.append('artist_id', artistId);
    data.append('lyrics', lyrics);
    data.append('image', image);
    data.append('audio_file', audioFile);

    const song = await createSong(data);
    // const song = await editSong(data, 6);
    // if (!song.errors) {
    //   console.log("Submit successful! ", song);
    // } else {
    //   setErrors(song.errors);
    // }
      console.log("Submit successful! ", song);
    
  };

  const updateTitle = (e) => {
    setTitle(e.target.value);
  };

  const updateArtistId = (e) => {
    setArtistId(e.target.value);
  };

  const updateLyrics = (e) => {
    setLyrics(e.target.value);
  };

  const updateImage = (e) => {
    setImage(e.target.files[0]);
  };


  return (
    <form onSubmit={songDataSubmitHandler} encType="multipart/form-data">
      <div>
        {errors.map((error) => (
          <div>{error}</div>
        ))}
      </div>
      <div>
        <label htmlFor="title">Title</label>
        <input
          name="title"
          type="text"
          placeholder="Title"
          value={title}
          onChange={updateTitle}
        />
      </div>
      <div>
        <label htmlFor="artistId">Artist ID</label>
        <input
          name="artistId"
          type="number"
          placeholder="Artist ID"
          value={artistId}
          onChange={updateArtistId}
        />
      </div>
      <div>
        <label htmlFor="image">Album Art</label>
        <input
          name="file"
          type="file"
          placeholder="Album art"
          onChange={updateImage}
        />
      </div>
      <div>
        <label htmlFor="lyrics">Lyrics</label>
        <textarea
          name="lyrics"
          placeholder="Lyrics"
          value={lyrics}
          onChange={updateLyrics}
        />
        <button type="submit">Submit</button>
      </div>
    </form>
  );
};

export default SongForm;
