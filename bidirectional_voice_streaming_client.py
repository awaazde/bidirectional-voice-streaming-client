import asyncio
import websockets
import os
import base64
import wave
import sys
import json
from io import BytesIO

# Arguments
recording_path = sys.argv[1] if len(sys.argv) > 1 else '/tmp/py_audio.wav'
port = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else 3001

# Log details
print(f"Listening on port {port}, writing incoming audio to WAV file {recording_path}")

# WebSocket Server
async def handle_connection(websocket):
    print(f"Received connection from {websocket.remote_address[0]}")
    
    # WAV file parameters (assumptions based on your code)
    sample_rate = 8000  # The sample rate (Hz)
    num_channels = 1    # Assuming mono audio
    sample_width = 2    # 16-bit PCM (2 bytes per sample)
    frame_rate = sample_rate

    # Create a wave file for writing audio
    wstream = wave.open(recording_path, 'wb')
    wstream.setnchannels(num_channels)
    wstream.setsampwidth(sample_width)
    wstream.setframerate(sample_rate)

    try:
        async for message in websocket:
            if isinstance(message, bytes):
                print(f"Buffer size: {len(message)}")
                wstream.writeframes(message)  # Write raw PCM audio data to the WAV file
            else:
                # Read and encode the WAV file
                wav_path = '/usr/local/freeswitch/sounds/en/us/callie/ivr/8000/ivr-welcome.wav'
                if os.path.exists(wav_path):
                    with open(wav_path, 'rb') as f:
                        wav_buffer = f.read()
                        base64_data = base64.b64encode(wav_buffer).decode('utf-8')
                        response = {
                            "type": "playAudio",
                            "data": {
                                "audioContentType": "wav",
                                "sampleRate": 8000,
                                "audioContent": base64_data,
                                "textContent": "Hi there! How can we help?"
                            }
                        }
                        await websocket.send(json.dumps(response))
                else:
                    print(f"Error: WAV file not found at {wav_path}")
                    
    except websockets.exceptions.ConnectionClosed as e:
        print(f"Socket closed {e.code}:{e.reason}")
    finally:
        wstream.close()

# Start the WebSocket server
async def main():
    server = await websockets.serve(handle_connection, "localhost", port)
    print(f"WebSocket server started on port {port}")
    await server.wait_closed()

# Run the server
if __name__ == "__main__":
    asyncio.run(main())
