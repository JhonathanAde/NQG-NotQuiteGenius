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
    console.log("song", song)
    return (
        <>
            <button onClick={playSong}>
                <i class="fas fa-play"></i>
            </button>
            {playing && <Player song={song} exit={exit}/>}
        </>
    );
};


export default PlayButton;