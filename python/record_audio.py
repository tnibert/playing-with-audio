#! /usr/bin/env python3
import pyaudio
import wave

FNAME = 'audio-recording.wav'
SECONDS = 2
RATE = 48000
CHANNELS = 2
FORMAT = pyaudio.paInt16
FRAMES_PER_BUFFER = 1024

"""print some info about the environment"""

#print(pyaudio.get_portaudio_version())
pa = pyaudio.PyAudio()
#print(pa.get_default_host_api_info())

#for id in range(pa.get_host_api_count()):
#    print(pa.get_host_api_info_by_index(id))

#print(pa.get_default_output_device_info())
print(pa.get_default_input_device_info())

for id in range(pa.get_device_count()):
  dev_dict = pa.get_device_info_by_index(id)
  print(" ")
  for key, value in dev_dict.items():
      print(key, value)

"""record some audio"""

print("\n\nrecording...")
stream_in = pa.open(
    rate=RATE,
    channels=CHANNELS,
    format=FORMAT,
    input=True,                   # input stream flag
    input_device_index=pa.get_default_input_device_info()["index"],         # input device index
    frames_per_buffer=FRAMES_PER_BUFFER
)

# read 5 seconds of the input stream
input_audio: bytes = stream_in.read(SECONDS * RATE)

# save the recorded audio
wav_file = wave.open(FNAME, 'wb')

# define audio stream properties
wav_file.setnchannels(2)        # number of channels
wav_file.setsampwidth(2)        # sample width in bytes
wav_file.setframerate(RATE)    # sampling rate in Hz

# write samples to the file
wav_file.writeframes(input_audio)

"""play it back"""

print("playing back...")

#wav_file = wave.open(FNAME)
#print(type(wav_file))

stream_out = pa.open(
    rate=RATE, #wav_file.getframerate(),     # sampling rate
    channels=CHANNELS, #wav_file.getnchannels(), # number of output channels
    format=FORMAT, #pa.get_format_from_width(wav_file.getsampwidth()),  # sample format and length
    output=True,             # output stream flag
    output_device_index=pa.get_default_output_device_info()["index"],   # output device index
    frames_per_buffer=FRAMES_PER_BUFFER  # buffer length
)

#output_audio = wav_file.readframes(5 * wav_file.getframerate())
#print(type(output_audio))
#stream_out.write(output_audio)
stream_out.write(input_audio)
