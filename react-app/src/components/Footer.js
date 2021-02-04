import React from 'react';
import {AiFillLinkedin, AiFillGithub} from 'react-icons/ai'
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
                <p>
                    Andrew Choi  
                    <a href="https://github.com/achoi1225" target="_blank" rel="noopener noreferrer"><AiFillGithub /></a>
                    <a href="https://www.linkedin.com/in/andrew-choi-340162201/" target="_blank" rel="noopener noreferrer"><AiFillLinkedin /></a>
                </p>
                <p>
                    Jhonathan Ade
                    <a href="https://github.com/JhonathanAde" target="_blank" rel="noopener noreferrer"><AiFillGithub /></a>
                    <a href="https://www.linkedin.com/in/jhonathan-ade-358b9b66/" target="_blank" rel="noopener noreferrer"><AiFillLinkedin /></a>
                </p>
                <p>
                    Maximos Salzman
                    <a href="https://github.com/Maximos-S" target="_blank" rel="noopener noreferrer"><AiFillGithub /></a>
                    <a href="https://www.linkedin.com/in/maximos-salzman-5a7050171/" target="_blank" rel="noopener noreferrer"><AiFillLinkedin /></a>
                </p>
                    
                <p>
                    Scott Smith
                    <a href="https://github.com/scottgit" target="_blank" rel="noopener noreferrer"><AiFillGithub /></a>
                    <a href="https://www.linkedin.com/in/one-scott-smith/" target="_blank" rel="noopener noreferrer"><AiFillLinkedin /></a>
                </p>
            </div>

            <div className="phone-icon"></div>
        </div>
    );
};


export default Footer;
