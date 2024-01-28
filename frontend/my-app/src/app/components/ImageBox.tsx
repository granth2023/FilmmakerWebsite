import React from 'react';

interface ImageBoxProps {
    altTexT: string;
}

const ImageBox: React.FC<ImageBoxProps> = ({ altText }) => {
    console.log('rendering imagbox', altText)
    return(
        <div className="m-4 shadow-log broder-4 border-black" style={{ width: '300px', height: '300px' }}>
            <di
        </div>
    )
    
    </ImageBoxProps>