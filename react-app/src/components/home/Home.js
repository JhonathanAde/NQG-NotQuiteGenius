import React from 'react';
import './home.css'
import SongTile from './SongTile';

const Home = () => {
    return (
        <div className="main-content">
            <div className="top-20">Top 20
                <SongTile>Song 1</SongTile>
                <SongTile>Song 2</SongTile>
                <SongTile>Song 3</SongTile>
                <SongTile>Song 4</SongTile>
                <SongTile>Song 5</SongTile>
                <SongTile>Song 6</SongTile>
            </div>
        </div>
    );
};

export default Home;