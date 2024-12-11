const WebSocket = require('ws');
const fs = require('fs');
const argv = require('minimist')(process.argv.slice(2));
const recordingPath = argv._.length ? argv._[0] : '/tmp/audio.raw';
const port = argv.port && parseInt(argv.port) ? parseInt(argv.port) : 3001
let wstream;

console.log(`listening on port ${port}, writing incoming raw audio to file ${recordingPath}`);

const wss = new WebSocket.Server({
    port
});

wss.on('connection', (ws, req) => {
    console.log(`received connection from ${req.connection.remoteAddress}`);
    wstream = fs.createWriteStream(recordingPath);

    ws.on('message', (message) => {
        
        if (typeof message === 'string') {
            console.log(`received message: ${message}`);
        } else if (message instanceof Buffer && message.length==320) {
            console.log(`Buffer size: ${message.length}`);
            wstream.write(message);
        }
	else{
	    console.log(typeof message);
            const wavPath = '/usr/local/freeswitch/sounds/en/us/callie/ivr/8000/ivr-welcome.wav';
            const wavBuffer = fs.readFileSync(wavPath);
	    const base64Data = wavBuffer.toString('base64');
            response = {
		"type": "playAudio",
		"data": {
			"audioContentType": "wav",
			"sampleRate": 8000,
			"audioContent": base64Data,
			"textContent": "Hi there!  How can we help?"
			}
		}
	    const data = JSON.stringify(response);
            ws.send(data);
        }
    });

    ws.on('close', (code, reason) => {
        console.log(`socket closed ${code}:${reason}`);
        wstream.end();
    });
});
