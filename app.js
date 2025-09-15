function sendMessage() {
    const input = document.getElementById('user-input');
    const messages = document.getElementById('messages');
    const userMsg = input.value.trim();
    if (!userMsg) return;
    messages.innerHTML += `<div><b>Você:</b> ${userMsg}</div>`;
    input.value = '';
        fetch('http://192.168.0.8:5000/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: userMsg })
        })
        .then(response => response.json())
        .then(data => {
            messages.innerHTML += `<div><b>Chatbot:</b> ${data.reply}</div>`;
        })
        .catch(() => {
            messages.innerHTML += `<div><b>Chatbot:</b> Erro ao conectar ao servidor.</div>`;
        });
}
