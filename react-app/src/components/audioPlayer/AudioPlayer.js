import React from 'react';
import AudioPlayer from 'react-h5-audio-player';
import 'react-h5-audio-player/lib/styles.css';
import './AudioPlayer.css'
// import 'react-h5-audio-player/lib/styles.less' Use LESS
// import 'react-h5-audio-player/src/styles.scss' Use SASS

const Player = () => (
    <div className="audio-player__container">
        <div className="audio-player__album-container">
            <div className="audio-player__album-art">

            </div>
            <div className="audio-player__album-details">
                <span className="audio-player__song-title">Song Title Here</span>
                <span className="audio-player__artist-name">Artist Name Here</span>
            </div>
        </div>
        <AudioPlayer
            autoPlay
            layout="horizontal"
            customAdditionalControls={[]}
            showJumpControls={false}
            src="http://example.com/audio.mp3"
            // style={{ width: '90%', height: '60px' }} 
            // onPlay={e => console.log("onPlay")}
            // other props here
        />
    </div>
);

export default Player