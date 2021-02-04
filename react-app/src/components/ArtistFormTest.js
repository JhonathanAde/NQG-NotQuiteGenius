import React, { useState } from "react";
import { Redirect } from "react-router-dom";
import { createArtist, editArtist } from "../services/artists";
import "./ArtistForm.css"

const ArtistForm = ({setNewArtistForm}) => {
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

  const getAndSetFilePath = (path, id) => {
    const pathField = document.getElementById(id);
    if (path) {
      let segments = path.split('/');
      if (segments.length === 1) {
        segments = path.split("\\")
      }
      const lastSegment = segments[segments.length - 1];
      pathField.innerHTML = lastSegment;
      pathField.setAttribute('title', lastSegment);
    } else {
      pathField.innerHTML = "No file";
    }
  }

  const updateImage = (e) => {
    setImage(e.target.files[0]);
    getAndSetFilePath(e.target.value, 'image-file-path');
    console.log('image file', e.target.files[0])
  };

  const handleImageUpdate = (e) => {
    e.preventDefault();
    document.getElementById('image-upload').click();
  }

  const persistLastImageSelection = (e) => {
    if (image) {
      const dataTransfer = new ClipboardEvent('').clipboardData || new DataTransfer();
      dataTransfer.items.add(new File(['album cover'], `${image.name}`));
      e.target.files = dataTransfer.files;
    }
  }


  return (
    <div className="new-artist-form-wrapper">
      <div className="new-artist-form-container">
        <form onSubmit={artistDataSubmitHandler} encType="multipart/form-data">
          <div className="artist-form-inputs">
            <div className="artist-form-header">Create Artist</div>
            <div>
              {errors.map((error) => (
                <div>{error}</div>
              ))}
            </div>
              <label htmlFor="name">Name</label>
              <input
                name="name"
                type="text"
                placeholder="Name"
                value={name}
                onChange={updateName}
              />
              <label htmlFor="image-upload" className="file-upload">
              <div className="file-label">Artist Image</div>
              <input
                  id="image-upload"
                  className="custom-file-input"
                  name="image-upload"
                  type="file"
                  onChange={updateImage}
                  onClick={persistLastImageSelection}
                />
              <div className="form-input-file">
                <div id="image-file-path" className="file-path">No file</div>
                <button className="file-button" type="button" onClick={handleImageUpdate}>Upload File</button>
              </div>
            </label>
              <div>
                <button className="nav-button" type="submit">Submit</button>
                <button className="nav-button" onClick={() => setNewArtistForm(false)}>Cancel</button>
              </div>
          </div>
        </form>
      </div>
    </div>
  );
};

export default ArtistForm;
