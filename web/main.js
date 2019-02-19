// Create WebSocket connection.
const socket = new WebSocket('ws://localhost:8090');

// Connection opened
socket.addEventListener('open', function (event) {
  
});

// Listen for messages
socket.addEventListener('message', function (event) {
  let reply = JSON.parse(event.data);
  console.log('Message from server ', reply);
  document.getElementById('message-reply').innerText = reply.message;
});

let inputEl = document.getElementById('message-input');
function sendMessage(event) {
  if (event.key === 'Enter') {
    socket.send(JSON.stringify({
      type: 'question',
      message: inputEl.value
    }));
  }
}
