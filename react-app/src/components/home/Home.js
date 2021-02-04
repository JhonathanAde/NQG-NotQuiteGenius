import React, {useState, useEffect} from 'react';
import ArtistTile from './ArtistTile';
import './home.css'
import SongTile from './SongTile';
import {getSongs} from '../../services/song'
import {getArtists} from '../../services/artists'
import LoadingWheel from './LoadingWheel';

const Home = () => {
    const [songs, setSongs] = useState(false)
    const [artists, setArtists] = useState(false)
    // const [loading, setLoading] = useState("hploading-hidden")

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
            {/* <LoadingWheel /> */}
                <div className="title-20">TOP SONGS</div>
            <div className="top-20">
                    {songs ? songs.map((song, idx) =>
                            <SongTile key={`song_${song.id}`} song={song} idx={idx + 1}/>
                    ):
                    <div className="hp-loadsongs">
                        <LoadingWheel className="hp-loadsongs"/>
                    </div>
                    }
            </div>
            <div className="artists-container">
                <div className="title-artist">TOP ARTISTS</div>
                    <div className="top-artists">
                        {artists ? artists.map((artist, idx) =>
                            <ArtistTile key={`artist_${artist.id}`} artist={artist} idx={idx + 1}/>
                        ): 
                        <div className="hp-loadartists">
                            <LoadingWheel />
                        </div>
                        }
                    </div>
            </div>
        </div>
    );
};

export default Home;
