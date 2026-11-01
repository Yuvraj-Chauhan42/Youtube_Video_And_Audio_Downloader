# YouTube Video and Audio Downloader

A Python-based command-line application that allows users to download YouTube videos and audio using the `yt-dlp` library.

## Features

- Download YouTube videos.
- Choose video quality (144p, 240p, 360p, 480p, 720p, 1080p, or Best Quality).
- Download YouTube audio.
- Choose audio bitrate (64, 96, 128, 192, 256, or 320 kbps).
- Download individual videos without downloading entire playlists.
- Simple and interactive command-line interface.

## Requirements

- Python 3
- yt-dlp
- FFmpeg (required for merging separate video and audio streams and certain audio conversions)

## Installation

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Install the required package:

   ```bash
   pip install -r requirements.txt
   ```

4. Install FFmpeg and make sure it is available in your system PATH.

## Usage

Run the following command:

```bash
python main.py
```

Choose whether to download a video or audio, select your preferred quality, and enter the YouTube URL.

## Project Structure

```text
Youtube_Video_And_Audio_Downloader/
│
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

**Yuvraj Chauhan**
