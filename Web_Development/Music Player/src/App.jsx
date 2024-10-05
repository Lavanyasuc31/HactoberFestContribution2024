import { useState } from "react";
import songs from "./songs";
import "./App.css";
import Navbar from './components/Navbar';
import Footer from "./components/Footer";
import Right from "./components/Right";
import Left from "./components/Left";

const App = () => {
  const [songList, setSongList] = useState(songs);
  const [currSong, setCurrSong] = useState(songList[0]);
  const [isOpen, setIsOpen] = useState(false);
  const [isPlaying, setIsPlaying] = useState(false);

  return (
    <>
      <Navbar setIsOpen={setIsOpen} />
      <main className="max-w-7xl p-5 mx-auto flex lg:flex-row flex-col items-center h-[80vh]">
        <Left currSong={currSong} isPlaying={isPlaying} setCurrSong={setCurrSong} songList={songList} setIsPlaying={setIsPlaying} />
        <Right songs={songList} setCurrSong={setCurrSong} currSong={currSong} isOpen={isOpen} setIsOpen={setIsOpen} isPlaying={isPlaying} setIsPlaying={setIsPlaying} />
      </main>
      <Footer />
    </>
  );
};

export default App;
