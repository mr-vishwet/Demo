def download_audio(audio_url, quality, file_name):
    yt = YouTube(audio_url)
    st.image(yt.thumbnail_url)
    st.write(" Title : " + yt.title)

    audio_streams = yt.streams.filter(type="audio")
    audio_stream = None
    for quality_option in ["256kbps", "192kbps", "128kbps", "64kbps"]:
        if quality_option == quality:
            audio_stream = audio_streams.filter(abr=quality).first()
            break
    if audio_stream is None:
        # Find the closest available audio stream and download it
        diffs = [abs(int(s.abr[:-4]) - int(quality[:-4]))
                 for s in audio_streams]
        closest_stream = audio_streams[diffs.index(min(diffs))]
        st.write(
            f"Selected audio quality {quality} is not available. Downloading closest quality {closest_stream.abr}.")
        audio_stream = closest_stream

    audio_size = audio_stream.filesize / (1024 * 1024)
    st.write(f"Audio size: {audio_size:.2f} MB")
    audio_stream.download(
        output_path=".", filename=file_name + "." + audio_stream.subtype)

    if audio_stream.subtype != "mp3":
        # Convert the audio to MP3 if it's not already in that format
        st.write("Converting audio to MP3 format...")
        audio_file = AudioSegment.from_file(
            file_name + "." + audio_stream.subtype)
        audio_file.export(file_name + ".mp3", format="mp3")
        os.remove(file_name + "." + audio_stream.subtype)
        file_name += ".mp3"

    return yt.title
