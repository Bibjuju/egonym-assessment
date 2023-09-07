import React, { useState } from 'react';
import axios from "axios";

const YoloAnnotator = () => {
    /**
     * Component allowing image selection and detection.
     */


    // Image shown on the browser
    const [selectedImage, setSelectedImage] = useState(null);

    const [isFetching, setIsFetching] = useState(false);
    const [detectedAnnotationText, setDetectedAnnotationText] = useState('');
    const [canSubmit, setCanSubmit] = useState(false)

    const handleImageUpload = (event) => {
        const file = event.target.files[0];
        const reader = new FileReader();

        try {
            reader.onload = () => {
                setCanSubmit(true)
                setDetectedAnnotationText('')
                setSelectedImage(reader.result);
            };

            reader.readAsDataURL(file);
        } catch (error) {
            console.log(error)
        }

    };

    const handlePostRequest = async () => {
        setIsFetching(true)
        setCanSubmit(false)
        axios.post('http://127.0.0.1:5000/predict', { image: selectedImage }).then(response => {
            setDetectedAnnotationText(response.data.raw_result.length + ' annotation(s) detected.')
            setSelectedImage(`data:image/jpeg;base64,${response.data.image}`)
            setIsFetching(false)
        }).catch(error => {
            console.log(error)
        })

    };

    return (
        <div>
            <input disabled={isFetching} type="file" accept="image/*" onChange={handleImageUpload} />
            {selectedImage && <img style={{ maxHeight: window.innerHeight * 0.8 }} src={selectedImage} />}
            <button disabled={isFetching || !canSubmit} onClick={handlePostRequest}>Send POST Request</button>
            <text>{detectedAnnotationText}</text>
        </div>
    );
}

export default YoloAnnotator