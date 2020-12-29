import React from 'react';
import {useHistory} from 'react-router-dom'

const SongTile = ({song, idx}) => {
    let history = useHistory()

    const songReroute = () => {
        history.push(`songs/${song.id}`)
    }

    return (
        <div className="song-tile">
            <div className="song-link" onClick={songReroute}>
                <div className="song-number">{idx}</div>
                <div className="song-image">{song.image}</div>
                <div className="song-title">{song.title}</div>
            </div>
            <div className="artist-link">
                <div className="song-artist">{song.artist.name}</div>
            </div>
        </div>
    );
};


export default SongTile;