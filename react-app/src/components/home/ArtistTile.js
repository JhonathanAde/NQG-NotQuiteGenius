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
                <div className="artist-number">{idx}</div>
                <img className="artist-image" src={artist.image} alt="artist"/>
            </div>
            <div className="artist-link">
                <div className="artist-title">{artist.name}</div>
            </div>
        </div>
    );
};


export default ArtistTile;