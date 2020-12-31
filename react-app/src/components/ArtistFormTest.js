import React, { useState } from "react";
import { Redirect } from "react-router-dom";
import { createArtist, editArtist } from "../services/artists";

const ArtistForm = () => {
  const [errors, setErrors] = useState([]);
  const [name, setName] = useState("");
  const [image, setImage] = useState("");

  const artistDataSubmitHandler = async (e) => {
    e.preventDefault();
    const data = new FormData();

    data.append('name', name);
    data.append('image', image);

    // const artist = await createArtist(data);
    const artist = await editArtist(data, 30);
    // const song = await editSong(data, 6);
    // if (!song.errors) {
    //   console.log("Submit successful! ", song);
    // } else {
    //   setErrors(song.errors);
    // }
    console.log("fetch result", artist);
    
  };

  const updateName = (e) => {
    setName(e.target.value);
  };

  const updateImage = (e) => {
    setImage(e.target.files[0]);
  };


  return (
    <form onSubmit={artistDataSubmitHandler} encType="multipart/form-data">
      <div>
        {errors.map((error) => (
          <div>{error}</div>
        ))}
      </div>
      <div>
        <label htmlFor="name">Name</label>
        <input
          name="name"
          type="text"
          placeholder="Name"
          value={name}
          onChange={updateName}
        />
      </div>
      <div>
        <label htmlFor="image">Artist image</label>
        <input
          name="Artist image"
          type="file"
          placeholder="Artist image"
          onChange={updateImage}
        />
        <button type="submit">Submit</button>
      </div>
    </form>
  );
};

export default ArtistForm;
