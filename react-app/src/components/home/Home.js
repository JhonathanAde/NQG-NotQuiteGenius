import React, {useState, useEffect} from 'react';
import ArtistTile from './ArtistTile';
import './home.css'
import SongTile from './SongTile';
import {getSongs} from '../../services/song'
import {getArtists} from '../../services/artists'

const Home = () => {
    const [songs, setSongs] = useState(false)
    const [artists, setArtists] = useState(false)

    useEffect(() => {
        (async () => {
            const resSongs = await getSongs()
            const resArtists = await getArtists()
            setSongs(resSongs.songs)
            setArtists(resArtists.artists)
        })()
    }, []);

    return (
        <div className="main-content">
            <div className="top-20">
                <div className="title-20">TOP 20</div>
                {songs ? songs.map((song, idx) => 
                    <SongTile key={idx} song={song} idx={idx + 1}/>
                ): "loading"}
            </div>
            <div className="artists-container">
                <div className="title-artist">TOP ARTISTS</div>
                <div className="top-artists">
                    {artists ? artists.map((artist, idx) => 
                        <ArtistTile key={idx} artist={artist} idx={idx + 1}/>
                    ): "loading"}
                </div>
            </div>
        </div>
    );
};

export default Home;