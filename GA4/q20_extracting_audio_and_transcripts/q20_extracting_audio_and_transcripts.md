# GA4 — Q20: Extracting Audio and Transcripts

## Problem Summary
MediaIndex requires extracting and transcribing a **30-second audio segment** from the YouTube video:

**Video:** https://www.youtube.com/watch?v=MPV7JXTWPWI  
**Title:** FFmpeg in 12 Minutes  

The required segment is:

Start time: **00:03:00**  
End time: **00:03:30**

The workflow consists of:
1. Downloading the audio from the video.
2. Trimming the audio to the specified time range.
3. Transcribing the extracted segment.
4. Submitting the spoken transcript.

---

## Step 1 — Download Audio Using yt-dlp

The following command downloads the audio stream from the YouTube video and converts it into MP3 format.

```bash
yt-dlp -f "ba[abr<50]/worstaudio" --extract-audio --audio-format mp3 --audio-quality 32k -o "audio.%(ext)s" "https://www.youtube.com/watch?v=MPV7JXTWPWI"
```

This produces:

```
audio.mp3
```

---

## Step 2 — Trim the Required Segment Using FFmpeg

We extract the audio segment between **00:03:00 and 00:03:30**.

```bash
ffmpeg -ss 00:03:00 -to 00:03:30 -i audio.mp3 -c copy segment.mp3
```

This generates:

```
segment.mp3
```

---

## Step 3 — Transcribe the Segment

The extracted audio segment can be transcribed using **faster-whisper**.

Install faster-whisper:

```bash
pip install faster-whisper
```

Transcribe:

```bash
faster-whisper segment.mp3 --model medium --language en
```

---

## Extracted Transcript (00:03:00 – 00:03:30)

```
link to it using the PATH variable. So what you're seeing onscreen right now are the steps I've used to do that. I do actually have things set up this way because well, it's just easier for me. Of course, this step is optional so if you don't want to do that, then make sure FFMPEG is in the same folder as the video files you want to work with. With that out of the way, let's move on to the fun part, and that is to actually convert files with FFMPEG! Now, previously to this I know I mentioned videos repeatedly, but as it turns out FFMPEG
```

---

## Final Answer Submitted to Portal

```
link to it using the PATH variable. So what you're seeing onscreen right now are the steps I've used to do that. I do actually have things set up this way because well, it's just easier for me. Of course, this step is optional so if you don't want to do that, then make sure FFMPEG is in the same folder as the video files you want to work with. With that out of the way, let's move on to the fun part, and that is to actually convert files with FFMPEG! Now, previously to this I know I mentioned videos repeatedly, but as it turns out FFMPEG
```

---
