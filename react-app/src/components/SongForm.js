import React, { useState, useEffect } from "react";
import { createSong } from "../services/song";
import "./SongForm.css"
import {useHistory} from 'react-router-dom'
import {createArtist, getArtists} from '../services/artists'

const SongForm = () => {
  const [errors, setErrors] = useState([]);
  const [title, setTitle] = useState("");
  const [existingArtist, setExistingArtist] = useState('');
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

      const artist = await createArtist(artistData);

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
      // console.log("Submit successful! ", song);
    } else {
      loadBar.classList.remove("loadBar")
      setErrors(song.errors);
      return
    }
    // console.log("Submit successful! ", song);
    history.push("/")
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
    setExistingArtist("");
  };

  const updateLyrics = (e) => {
    setLyrics(e.target.value);
  };

  const persistLastImageSelection = (e) => {
    if (image) {
      const dataTransfer = new ClipboardEvent('').clipboardData || new DataTransfer();
      dataTransfer.items.add(new File(['album cover'], `${image.name}`));
      e.target.files = dataTransfer.files;
    }
  }

  const handleImageUpdate = (e) => {
    e.preventDefault();
    document.getElementById('image-upload').click();
  }

  const updateImage = (e) => {
    setImage(e.target.files[0]);
    getAndSetFilePath(e.target.value, 'image-file-path');
    console.log('image file', e.target.files[0])
  };

  const persistLastSongSelection = (e) => {
    if (audioFile) {
      const dataTransfer = new ClipboardEvent('').clipboardData || new DataTransfer();
      dataTransfer.items.add(new File(['song sample'], `${audioFile.name}`));
      e.target.files = dataTransfer.files;
    }
  }

  const handleSongUpdate = (e) => {
    e.preventDefault();
    document.getElementById('song-sample-upload').click();
  }

  const updateSong = (e) => {
    setAudioFile(e.target.files[0]);
    getAndSetFilePath(e.target.value, 'song-file-path');
  }

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

  return (
    <div className="form-container-song">
      <form onSubmit={songDataSubmitHandler} encType="multipart/form-data">
        <div className="form-inputs">
          <div>
            {errors.map((error) => (
              <div key={error}>{error}</div>
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
                  <option key={artist.id} value={artist.id}>{artist.name}</option>
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
          <label htmlFor="image-upload" className="file-upload">
            <div className="file-label">Album Cover</div>
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
          <label htmlFor="song-sample-upload" className="file-upload">
            <div className="file-label">Song Sample</div>
            <input
                id="song-sample-upload"
                data-last-path=""
                className="custom-file-input"
                name="song-sample-upload"
                type="file"
                onChange={updateSong}
                onClick={persistLastSongSelection}
              />
            <div className="form-input-file">
              <div id="song-file-path" className="file-path">No file</div>
              <button className="file-button" type="button" onClick={handleSongUpdate}>Upload File</button>
            </div>
          </label>
          <label htmlFor="lyrics">Lyrics</label>
          <div className="form-input">
            <textarea
              id="lyrics"
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
