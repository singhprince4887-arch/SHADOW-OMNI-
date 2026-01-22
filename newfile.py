<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SHADOW ARCHITECTURE | GLOBAL CORE</title>
    <style>
        :root { --glow: #0ea5e9; --bg: #020617; }
        * { box-sizing: border-box; }
        body { background: var(--bg); color: #f8fafc; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; overflow: hidden; }
        
        /* Premium Glass Design */
        .container { 
            width: 95%; max-width: 450px; height: 85vh; 
            background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(20px); border-radius: 30px; display: flex; flex-direction: column;
            box-shadow: 0 0 40px rgba(0, 0, 0, 0.8), inset 0 0 20px rgba(14, 165, 233, 0.05);
            animation: startUp 1s ease-out;
        }

        .header { padding: 25px; text-align: center; border-bottom: 1px solid rgba(255,255,255,0.05); }
        .header h2 { margin: 0; font-size: 16px; letter-spacing: 5px; color: var(--glow); font-weight: 300; text-transform: uppercase; }
        .status { font-size: 10px; color: #22c55e; margin-top: 5px; letter-spacing: 1px; }

        #chat { flex: 1; overflow-y: auto; padding: 25px; display: flex; flex-direction: column; gap: 20px; scrollbar-width: none; }
        #chat::-webkit-scrollbar { display: none; }

        .msg { padding: 14px 18px; border-radius: 20px; font-size: 14px; max-width: 85%; line-height: 1.6; position: relative; animation: slideIn 0.4s ease forwards; }
        .ai { background: rgba(255,255,255,0.03); align-self: flex-start; border: 1px solid rgba(255,255,255,0.08); border-bottom-left-radius: 2px; }
        .user { background: var(--glow); color: #fff; align-self: flex-end; border-bottom-right-radius: 2px; font-weight: 500; box-shadow: 0 4px 15px rgba(14, 165, 233, 0.3); }

        .input-box { padding: 25px; display: flex; gap: 12px; background: rgba(0,0,0,0.2); border-bottom-left-radius: 30px; border-bottom-right-radius: 30px; }
        input { flex: 1; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); color: white; padding: 15px; border-radius: 15px; outline: none; transition: 0.3s; font-size: 14px; }
        input:focus { border-color: var(--glow); background: rgba(255,255,255,0.08); }
        button { background: var(--glow); border: none; width: 50px; height: 50px; border-radius: 15px; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: 0.3s; }
        button:hover { transform: scale(1.05); box-shadow: 0 0 20px var(--glow); }

        @keyframes startUp { from { opacity: 0; transform: scale(0.95); } to { opacity: 1; transform: scale(1); } }
        @keyframes slideIn { from { opacity: 0; transform: translateY(15px); } to { opacity: 1; transform: translateY(0); } }
    </style>
</head>
<body>

<div class="container">
    <div class="header">
        <h2>SHADOW CORE V3</h2>
        <div class="status">● BRAZIL NODE ACTIVE</div>
    </div>
    <div id="chat">
        <div class="msg ai">Connection Secure. System is initialized. I am ready to learn.</div>
    </div>
    <div class="input-box">
        <input type="text" id="userInput" placeholder="Teach me something..." autocomplete="off">
        <button onclick="send()">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
        </button>
    </div>
</div>

<script>
    let memory = {
        "hello": "Greetings. The Brazil-India neural bridge is stable.",
        "hi": "System online. Waiting for your input.",
        "who are you": "I am a custom neural engine architected by Shadow.",
        "project": "This is a collaborative AI framework designed for global scaling.",
        "status": "All systems operational. Latency: 42ms."
    };

    function send() {
        const input = document.getElementById("userInput");
        const chat = document.getElementById("chat");
        const val = input.value.trim();
        if(!val) return;

        chat.innerHTML += `<div class="msg user">${val}</div>`;
        const text = val.toLowerCase();

        setTimeout(() => {
            let reply = "";
            if (text.startsWith("sikho |")) {
                const parts = val.split("|");
                if(parts.length === 3) {
                    memory[parts[1].trim().toLowerCase()] = parts[2].trim();
                    reply = "Intelligence node updated. I have learned this.";
                } else {
                    reply = "Training Error. Use syntax: sikho | key | value";
                }
            } else {
                reply = memory[text] || "Data not found. Use 'sikho' command to train my neural network.";
            }
            chat.innerHTML += `<div class="msg ai">${reply}</div>`;
            chat.scrollTop = chat.scrollHeight;
        }, 600);
        input.value = "";
    }

    document.getElementById("userInput").addEventListener("keypress", function(e) {
        if (e.key === "Enter") send();
    });
</script>

</body>
</html>