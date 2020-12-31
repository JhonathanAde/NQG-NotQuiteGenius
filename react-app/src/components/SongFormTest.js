import React, { useState, useEffect } from "react";
import { createSong } from "../services/song";
import "./SongForm.css"
import {createArtist, getArtists} from '../services/artists'

const SongForm = () => {
  const [errors, setErrors] = useState([]);
  const [title, setTitle] = useState("");
  const [existingArtist, setExistingArtist] = useState(null);
  const [newArtist, setNewArtist] = useState("");
  const [lyrics, setLyrics] = useState("");
  const [image, setImage] = useState("");
  const [audioFile, setAudioFile] = useState("");
  const [artists, setArtists] = useState(null);

  useEffect(() => {
    (async () => {
      const res = await getArtists()
      console.log(res)
      setArtists(res.artists)
    })()
  }, []);
  
  console.log("hits", artists)
  const songDataSubmitHandler = async (e) => {
    e.preventDefault();
    let artistId;

    if(!existingArtist) {
      const artistData = new FormData()
      artistData.append('name', newArtist)
      artistData.append('image', image)
  
      const artist = await createArtist(artistData)
      artistId = artist.id
    } else {
      artistId = existingArtist
    }

    const data = new FormData();

    data.append('title', title);
    data.append('artist_id', artistId);
    data.append('lyrics', lyrics);
    data.append('image', image);
    data.append('audio_file', audioFile);

    // const song = await createSong(data);
    // const song = await editSong(data, 6);
    // if (!song.errors) {
    //   console.log("Submit successful! ", song);
    // } else {
    //   setErrors(song.errors);
    // }
    // console.log("Submit successful! ", song);
    
  };

  const updateTitle = (e) => {
    setTitle(e.target.value);
  };

  const updateArtistId = (e) => {
    setExistingArtist(e.target.value);
    setNewArtist("")
  };

  const updateNewArtist = (e) => {
    setNewArtist(e.target.value)
    setExistingArtist(null);
  };

  const updateLyrics = (e) => {
    setLyrics(e.target.value);
  };

  const updateImage = (e) => {
    setImage(e.target.files[0]);
  };

  const updateSong = (e) => {
    setAudioFile(e.target.files[0])
  }


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
          <label htmlFor="title">Select Artist</label>
            <div className="form-input">
              <select 
                name="artist_id"
                type="text"
                placeholder="Artist"
                value={existingArtist}
                onChange={updateArtistId}
              >
                <option value={null}>Choose an Artist</option>
                {artists && 
                artists.map((artist, id) => (
                  <option value={artist.id}>{artist.name}</option>
                  ))
                }
              </select>
            </div>
            <div className="form-input">-or-</div>
          <label htmlFor="title">Create New Artist</label>
            <div className="form-input">
              <input
                name="artist_id"
                type="text"
                placeholder="Artist"
                value={newArtist}
                onChange={updateNewArtist} 
              />
            </div>
          {/* <div className="form-input">
            <input
              name="artist_id"
              type="text"
              list="artists"
              placeholder="Artist"
              value={artistId}
              onChange={updateArtistId}
            />
            <datalist id="artists">
              {artists && 
              artists.map((art, id) => (
                <option value={art.id}>{art.name}</option>
              ))
              }
            </datalist>
          </div> */}

          <label htmlFor="image">Album Cover</label>
          <div className="form-input-file">
            <input
              className="custom-file-input"
              name="Album art"
              type="file"
              placeholder="Album art"
              onChange={updateImage}
            />
          <div className="file-button">Upload File</div>
          </div>
          <label htmlFor="">Song Sample</label>
          <div className="form-input-file">
            <input
              className="custom-file-input"
              name="Song sample"
              type="file"
              placeholder="Song_sample"
              onChange={updateSong}
            />
            <div className="file-button">Upload File</div>
          </div>
          <label htmlFor="lyrics">Lyrics</label>
          <div className="form-input">
            <textarea
              className="lyrics-field"
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
