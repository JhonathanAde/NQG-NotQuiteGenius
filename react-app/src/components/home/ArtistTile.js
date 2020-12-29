import React from 'react';
import {useHistory} from 'react-router-dom'

const ArtistTile = ({artist, idx}) => {
    let history = useHistory();

    const songReroute = () => {
        history.push(`artists/${artist.id}`)
    }

    return (
        <div className="artist-tile" onClick={songReroute}>
            <div className="song-link">
                <div className="song-number">{idx}</div>
                <div className="artist-image">{artist.image}</div>
            </div>
            <div className="artist-link">
                <div className="song-title">{artist.name}</div>
            </div>
        </div>
    );
};


export default ArtistTile;