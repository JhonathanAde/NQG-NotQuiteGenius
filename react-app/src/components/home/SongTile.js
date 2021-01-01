import React from 'react';
import {useHistory, BrowserRouter} from 'react-router-dom'
import PlayButton from '../audioPlayer/PlayButton';

const SongTile = ({song, idx}) => {
    let history = useHistory()

    const songReroute = () => {
        history.push(`/songs/${song.id}`)
    }
    const artistReroute = () => {

        history.push(`/artists/${song.artist.id}`)
    }

    return (
        <>
            <div className="song-tile">
                <div className="song-link" onClick={songReroute}>
                    <div className="song-number">{idx}</div>
                    <img className="song-image" src={song.image} alt="album cover"/>
                    <div className="song-title">{song.title}</div>
                </div>
                    {/* <PlayButton song={song}/> */}
                <div className="artist-link" onClick={artistReroute}>
                    <div className="song-artist">{song.artist.name}</div>
                </div>
            </div>
            <div className="divider-container">
                <div className="divider"></div>
            </div>
        </>
    );
};


export default SongTile;