#! /usr/bin/env python3
import pyaudio
import wave

# print some info about the environment
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

# record some audio
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
output_filename = 'audio-recording.wav'
wav_file = wave.open(output_filename, 'wb')

# define audio stream properties
wav_file.setnchannels(2)        # number of channels
wav_file.setsampwidth(2)        # sample width in bytes
wav_file.setframerate(48000)    # sampling rate in Hz

# write samples to the file
wav_file.writeframes(input_audio)
