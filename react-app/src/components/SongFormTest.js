import React, { useState } from "react";
import { Redirect } from "react-router-dom";
import { createSong } from "../services/song";

const SongForm = () => {
  const [errors, setErrors] = useState([]);
  const [title, setTitle] = useState("");
  const [lyrics, setLyrics] = useState("");
  const [image, setImage] = useState("");

  const songDataSubmitHandler = async (e) => {
    e.preventDefault();
    const song = await createSong(title, image, lyrics);
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

  const updateLyrics = (e) => {
    setLyrics(e.target.value);
  };

  const updateImage = (e) => {
    setImage(e.target.value);
  };


  return (
    <form onSubmit={songDataSubmitHandler}>
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
        <label htmlFor="image">Album Art</label>
        <input
          name="file"
          type="file"
          placeholder="Album art"
          value={image}
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
