import React, {useState, useEffect} from 'react';
import ArtistTile from './ArtistTile';
import './home.css'
import SongTile from './SongTile';
import {getSongs} from '../../services/song'

const Home = () => {
    const [songs, setSongs] = useState(false)

    useEffect(() => {
        (async () => {
            const res = await getSongs()
            setSongs(res.songs)
        })()
    }, []);

    return (
        <div className="main-content">
            <div className="top-20">
                <div className="title-20">TOP 20</div>
                {songs? songs.map((song, idx) => 
                    <SongTile key={idx} song={song} idx={idx + 1}/>
                ): "loading"}
            </div>
            <div className="top-artists">
                <div className="title-artist">TOP ARTISTS</div>
                <ArtistTile />
                <ArtistTile />
                <ArtistTile />
                <ArtistTile />
            </div>
        </div>
    );
};

export default Home;