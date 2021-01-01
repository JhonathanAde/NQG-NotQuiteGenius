import React from 'react';
import AudioPlayer from 'react-h5-audio-player';
import 'react-h5-audio-player/lib/styles.css';
import './AudioPlayer.css'
// import 'react-h5-audio-player/lib/styles.less' Use LESS
// import 'react-h5-audio-player/src/styles.scss' Use SASS

const Player = ({song, exit}) => (
    <div className="audio-player__container">
        <div className="audio-player__album-container">
            <div className="audio-player__album-art">
                <img className="album-art" src={song.image} alt="album art" />
            </div>
            <div className="audio-player__album-details">
                <span className="audio-player__song-title">{song.title}</span>
                <span className="audio-player__artist-name">{song.artist.name}</span>
            </div>
            <div className="x-out" onClick={exit}>X</div>
        </div>
        <AudioPlayer
            autoPlay={false}
            layout="horizontal"
            customAdditionalControls={[]}
            showJumpControls={false}
            src={song.audioFile}

            // style={{ width: '90%', height: '60px' }} 
            // onPlay={e => console.log("onPlay")}
            // other props here
        />
    </div>
);

export default Player