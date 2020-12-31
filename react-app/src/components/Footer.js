import React from 'react';
import './Footer.css'


const Footer = () => {
    return (
        <div className="footer">
            <div className="title">
                NOT QUITE GENIUS...
            </div>
            <div className="about-nqg">
                <p>
                    A lyric site for the rest of us. Not Quite Genius was born 
                    from the quirkiness of our first impressions of lyrics.
                </p>
            </div>
            <div className="developers">
                <h1>Andrew Choi </h1>
                <h1>Jhonathan Ade</h1>
                <h1>Maximos Salzman</h1>
                <h1>Scott Smith</h1>
            </div>
            <div className="phone-icon"></div>
        </div>
    );
};


export default Footer;