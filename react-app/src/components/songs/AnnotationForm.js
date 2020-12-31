import React, {useState} from 'react';
import { annotate } from '../../services/song';

const AnnotationForm = ({lyricKey, songId, userId}) => {
    const [content, setContent] = useState("")

    const addAnnotation = async (e) => {
        e.preventDefault()
        const data = new FormData();

        data.append("lyric_key", lyricKey)
        data.append("user_id", userId)
        data.append("content", content)

        setContent("")
        const annotation = await annotate(songId, data)
    }

    const updateContent = (e) => {
        setContent(e.target.value)
    }

    return (
        <div>
            <form method="post" action={`/api/songs/${songId}/annotation`}>
                <input type="hidden" name="lyric_key" value={lyricKey} />
                <textarea name="content" placeholder="Add Annotation" value={content} onChange={updateContent}/>
                <button type="submit" onClick={addAnnotation}>Add</button>
            </form>
        </div>
    );
};

export default AnnotationForm;