import React from 'react';
import ArtistTile from './ArtistTile';
import './home.css'
import SongTile from './SongTile';

const Home = () => {
    return (
        <div className="main-content">
            <div className="top-20">
                <div className="title-20">TOP 20</div>
                <SongTile>Song 1</SongTile>
                <SongTile>Song 2</SongTile>
                <SongTile>Song 3</SongTile>
                <SongTile>Song 4</SongTile>
                <SongTile>Song 5</SongTile>
                <SongTile>Song 6</SongTile>
                <SongTile>Song 6</SongTile>
                <SongTile>Song 7</SongTile>
                <SongTile>Song 8</SongTile>
                <SongTile>Song 9</SongTile>
                <SongTile>Song 10</SongTile>
                <SongTile>Song 11</SongTile>
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