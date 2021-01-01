import React, { useEffect } from 'react';

const Lyrics = ({lyricsHTML, activateAnnotation}) => {

  useEffect(() => {
    console.log('in effect', activateAnnotation)
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
  console.log('rendering lyrics')
  return (
    <p>
      {
      lyricsHTML
      }
    </p>
  )
}

export default Lyrics
