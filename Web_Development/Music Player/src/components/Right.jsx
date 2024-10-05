import { FaPlay, FaPause } from "react-icons/fa";
import { MdClose } from "react-icons/md";

const Right = ({ songs, setCurrSong, currSong, isOpen, setIsOpen, isPlaying, setIsPlaying }) => {

  const handleSongClick = (song) => {
    if (song.id === currSong.id) {
      // Toggle pause/play for the current song
      setIsPlaying(!isPlaying);
    } else {
      // Set new song and play it
      setCurrSong(song);
      setIsPlaying(true);  // Always play the new song
    }
    setIsOpen(false);
  };

  return (
    <div className={`lg:w-1/2 w-full flex fixed lg:relative lg:right-0 top-0 ${isOpen ? "right-0" : "-right-full"} lg:bg-transparent z-50 bg-white songlist h-screen items-center justify-center`}>
      <div className="flex flex-col gap-5 w-full p-5">
        {songs.map((song) => (
          <div
            key={song.id}
            onClick={() => handleSongClick(song)}
            className="cursor-pointer flex items-center gap-2 song px-4 py-2 rounded-lg bg-white w-full"
          >
            {song.id === currSong.id && isPlaying ? <FaPause /> : <FaPlay />}
            <p>{song.name}</p>
          </div>
        ))}
        <button
          className="lg:hidden absolute top-3 right-3 border rounded-full p-2"
          onClick={() => setIsOpen(false)}
        >
          <MdClose size={20} />
        </button>
      </div>
    </div>
  );
};

export default Right;
