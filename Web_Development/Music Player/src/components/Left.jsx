import React, { useEffect, useRef } from 'react';
import ReactAudioPlayer from 'react-audio-player';

const Left = ({ currSong, isPlaying }) => {
  const audioRef = useRef(null);

  useEffect(() => {
    if (isPlaying) {
      audioRef.current.audioEl.current.play();
    } else {
      audioRef.current.audioEl.current.pause();
    }
  }, [currSong, isPlaying]); 

  return (
    <div className="lg:w-1/2 w-full flex items-center justify-center">
      <div className="flex flex-col items-center gap-3">
        
        <img src={currSong.cover} alt={currSong.name} className="max-w-sm w-full rounded-lg" />
       
        <ReactAudioPlayer
          src={currSong.songPath}
          ref={audioRef}
          
        />
        <h2 className="text-2xl text-white font-semibold text-center">{currSong.name}</h2>
        <p className="text-xl font-semibold text-white text-center">Singer: {currSong.singer}</p>
      </div>
    </div>
  );
};

export default Left;
