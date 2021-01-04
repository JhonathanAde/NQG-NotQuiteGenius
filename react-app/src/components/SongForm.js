import React, { useState, useEffect } from "react";
import { createSong } from "../services/song";
import "./SongForm.css"
import {useHistory} from 'react-router-dom'
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
      setArtists(res.artists)
    })()
  }, []);

  let history = useHistory();
  
  const songDataSubmitHandler = async (e) => {
    e.preventDefault();
    const loadBar = document.getElementById("loadBarHidden")
    const progressBar = document.getElementById("progressBar")
    loadBar.classList.add("loadBar")
    let artistId;
    
    let lineBreaks = lyrics.split('\n').join('<br >')
    progressBar.style.width = "30%"

    if(!existingArtist) {
      const artistData = new FormData()
      artistData.append('name', newArtist)
      artistData.append('image', image)
  
      const artist = await createArtist(artistData)
      artistId = artist.id
    } else {
      artistId = existingArtist
    }
    progressBar.style.width = "60%"
    const data = new FormData();
    data.append('title', title);
    data.append('artist_id', artistId);
    data.append('lyrics', lineBreaks);
    data.append('image', image);
    data.append('audio_file', audioFile);

    progressBar.style.width = "90%"
    const song = await createSong(data);
    // const song = await editSong(data, 6);
    progressBar.style.width = "100%"
    if (!song.errors) {
      console.log("Submit successful! ", song);
    } else {
      setErrors(song.errors);
    }
    console.log("Submit successful! ", song);
    history.push("/")
  };

  const prevent = (e) => {
    e.preventDefault();
  }

  const updateTitle = (e) => {
    setTitle(e.target.value);
  };

  const updateArtistId = (e) => {
    setExistingArtist(e.target.value);
    setNewArtist("")
  };

  const updateNewArtist = (e) => {
    setNewArtist(e.target.value)
    setExistingArtist("");
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
    <div className="form-container-song">
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
          <button className="file-button" onClick={prevent}>Upload File</button>
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
            <button className="file-button" onClick={prevent}>Upload File</button>
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
            <div id="loadBarHidden">
              <div className="progressBar" id="progressBar"></div>
            </div>
        </div>
      </form>
    </div>
  );
};

export default SongForm;
