import React from 'react';

interface ImageBoxProps {
    altText: string;
}

const ImageBox: React.FC<ImageBoxProps> = ({ altText }) => {
    console.log('rendering imagbox', altText)
    return(
        <div className="m-4 shadow-log broder-4 border-black" style={{ width: '300px', height: '300px' }}>
            <div className="bg-red-500 h-full w-full" aria-label={altText}></div>
        </div>
    )
};
export default ImageBox;