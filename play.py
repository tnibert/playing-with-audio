#! /usr/bin/env python3
import pyaudio

print(pyaudio.get_portaudio_version())
pa = pyaudio.PyAudio()
print(pa.get_default_host_api_info())

for id in range(pa.get_host_api_count()):
    print(pa.get_host_api_info_by_index(id))

print(pa.get_default_output_device_info())

for id in range(pa.get_device_count()):
  dev_dict = pa.get_device_info_by_index(id)
  for key, value in dev_dict.items():
      print(key, value)
