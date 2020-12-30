import React, { useState } from "react";
import { createSong } from "../services/song";
import "./SongForm.css"

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
    <div className="form-container">
      <form onSubmit={songDataSubmitHandler} encType="multipart/form-data">
        <div className="form-inputs">
          <div>
            {errors.map((error) => (
              <div>{error}</div>
            ))}
          </div>
          <label htmlFor="title">Title</label>
          <div className="form-input">
            <input
              name="title"
              type="text"
              placeholder="Title"
              value={title}
              onChange={updateTitle}
            />
          </div>
          <label htmlFor="image">Album Art</label>
          <div className="form-input">
            <input
              name="Album art"
              type="file"
              placeholder="Album art"
              onChange={updateImage}
            />
          </div>
          <label htmlFor="">Song Sample</label>
          <div className="form-input">
            <input
              name="Song sample"
              type="file"
              placeholder="Song_sample"
              onChange={updateImage}
            />
          </div>
          <label htmlFor="lyrics">Lyrics</label>
          <div className="form-input">
            <textarea
              name="lyrics"
              placeholder="Lyrics"
              value={lyrics}
              onChange={updateLyrics}
            />
          </div>
            <button className="form-input" type="submit">Submit</button>
        </div>
      </form>
    </div>
  );
};

export default SongForm;
