import React, {useState} from 'react';
import Player from './AudioPlayer';


const PlayButton = ({song}) => {

    const [playing, setPlaying] = useState(false)

    const playSong = () => {
        setPlaying(true)
    }

    const exit = () => {
        setPlaying(false)
    }
    return (
        <>
            <button onClick={playSong}>
                <i className="fas fa-play"></i>
            </button>
            {playing && <Player song={song} exit={exit}/>}
        </>
    );
};


export default PlayButton;
