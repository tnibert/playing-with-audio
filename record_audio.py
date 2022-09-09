#! /usr/bin/env python3
import pyaudio
import wave

FNAME = 'audio-recording.wav'

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
print("recording...")
stream_in = pa.open(
    rate=48000,
    channels=2,
    format=pyaudio.paInt16,
    input=True,                   # input stream flag
    input_device_index=pa.get_default_input_device_info()["index"],         # input device index
    frames_per_buffer=1024
)

# read 5 seconds of the input stream
input_audio = stream_in.read(5 * 48000)

# save the recorded audio
wav_file = wave.open(FNAME, 'wb')

# define audio stream properties
wav_file.setnchannels(2)        # number of channels
wav_file.setsampwidth(2)        # sample width in bytes
wav_file.setframerate(48000)    # sampling rate in Hz

# write samples to the file
wav_file.writeframes(input_audio)

"""play it back"""
# todo: play directly from input_audio
print(type(input_audio))
print("playing back...")

wav_file = wave.open(FNAME)

stream_out = pa.open(
    rate=wav_file.getframerate(),     # sampling rate
    channels=wav_file.getnchannels(), # number of output channels
    format=pa.get_format_from_width(wav_file.getsampwidth()),  # sample format and length
    output=True,             # output stream flag
    output_device_index=pa.get_default_output_device_info()["index"],   # output device index
    frames_per_buffer=1024,  # buffer length
)

output_audio = wav_file.readframes(5 * wav_file.getframerate())
stream_out.write(output_audio)
