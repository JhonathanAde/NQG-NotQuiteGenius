import React, {useState} from 'react';
import { annotate } from '../../services/song';

const AnnotationForm = ({ setAnnotations, annotations, lyricKey, songId, userId, clearNewAnnotationKey, setActivateAnnotation}) => {
    const [content, setContent] = useState("")

    const addAnnotation = async (e) => {
        e.preventDefault()
        const data = new FormData();

        data.append("lyric_key", lyricKey)
        data.append("user_id", userId)
        data.append("content", content)

        setContent("")
        const annotation = await annotate(songId, data)

        //Using current annotations length will result in the right
        //index for the new annotation that is added
        setActivateAnnotation(annotations.length)
        setAnnotations([...annotations, annotation])
    }

    const updateContent = (e) => {
        setContent(e.target.value)
    }

    return (
        <form className="annotation-form" method="post" onSubmit={addAnnotation}>
            <input type="hidden" name="lyric_key" value={lyricKey} />
            <textarea className="content-textarea" name="content" placeholder="Add Annotation..." value={content} onChange={updateContent}/>
            <div className="annotationButtons">
                <button type="submit">Add</button>
                <button type="button" onClick={clearNewAnnotationKey}>Cancel</button>
            </div>
        </form>
    );
};

export default AnnotationForm;
