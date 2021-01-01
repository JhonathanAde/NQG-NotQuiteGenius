import React, { useEffect } from 'react';

const Lyrics = ({lyricsHTML, activateAnnotation}) => {

  useEffect(() => {

    if (activateAnnotation) {
      clickActiveAnnotation(activateAnnotation)
    }

  }, [])

  const clickActiveAnnotation = (index) => {
    const annotation = document.querySelector(`[data-index="${index}"]`);
    console.log(annotation)
    if (annotation) {
      annotation.click();
    }
  }

  return (
    <p>
      {
      lyricsHTML
      }
    </p>
  )
}

export default Lyrics
