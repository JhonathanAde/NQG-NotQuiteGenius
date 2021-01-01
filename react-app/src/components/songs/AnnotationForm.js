import React, {useState} from 'react';
import { annotate } from '../../services/song';

const AnnotationForm = ({ setAnnotations, annotations, lyricKey, songId, userId, clearNewAnnotationKey}) => {
    const [content, setContent] = useState("")

    const addAnnotation = async (e) => {
        e.preventDefault()
        const data = new FormData();

        data.append("lyric_key", lyricKey)
        data.append("user_id", userId)
        data.append("content", content)

        setContent("")
        const annotation = await annotate(songId, data)
        console.log("passes annotation", annotation)
        setAnnotations([...annotations, annotation])
    }

    const updateContent = (e) => {
        setContent(e.target.value)
    }

    const clearSelection = () => {
        //bandaid fix
        clearNewAnnotationKey(false)
    }

    return (
        <div>
            <form className="annotation-form" method="post" onSubmit={addAnnotation}>
                <input type="hidden" name="lyric_key" value={lyricKey} />
                <textarea className="content-textarea" name="content" placeholder="Add Annotation..." value={content} onChange={updateContent}/>
                <div className="annotationButtons">
                    <button type="submit">Add</button>
                    <button type="button" onClick={clearSelection}>Cancel</button>
                </div>
            </form>
        </div>
    );
};

export default AnnotationForm;