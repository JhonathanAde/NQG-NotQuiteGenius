import React from 'react';
import './Footer.css'


const Footer = () => {

    return (
        <div className="footer">
            <div className="title">
                NOT QUITE GENIUS...
            <div className="title-divider"></div>
            </div>
            <div className="about-nqg">
                <p>
                    A lyric site for the rest of us. Not Quite Genius was born 
                    from the quirkiness of our first impressions of lyrics.
                </p>
            </div>
            <div className="developers">
                <a href="https://github.com/achoi1225" >Andrew Choi </a>
                <a href="https://github.com/JhonathanAde" >Jhonathan Ade</a>
                <a href="https://github.com/Maximos-S">Maximos Salzman</a>
                <a href="https://github.com/scottgit" >Scott Smith</a>
            </div>
            <div className="phone-icon"></div>
        </div>
    );
};


export default Footer;