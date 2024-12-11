# Bidirectional Voice Streaming Clients

This repository contains clients for bidirectional voice streaming using WebSockets. 
The clients are designed to establish a connection with a WebSocket server to facilitate real-time voice communication. 

## Features
- Bidirectional audio streaming over WebSockets.
- Supports both receiving and sending audio streams in real-time.
- Can be easily integrated into your own applications requiring WebSocket-based audio streaming.
- Supports WAV format.

## Installation

### Prerequisites
To run the WebSocket clients, make sure you have the following installed:

- Python 3.7 or higher (for Python-based clients).
- Node.js (for Node.js-based clients).
- WebSocket server set up to handle connections.

### Python Client
1. Clone the repository:
   ```bash
   git clone https://github.com/awaazde/bidirectional-voice-streaming-clients.git
   cd bidirectional-voice-streaming-clients```
2. Install the required Python dependencies:
   ``` pip install websockets asyncio```
3. Run the Python WebSocket client:
   ``` python bidirectional_voice_streaming_client.py ```

### Javascript Client
1. Clone the repository:
   ```bash
   git clone https://github.com/awaazde/bidirectional-voice-streaming-clients.git
   cd bidirectional-voice-streaming-clients```
2. Install the required Javascript dependencies:
   ``` npm install```
3. Run the Javascript WebSocket client:
   ``` node bidirectional_voice_streaming_client.js ```
